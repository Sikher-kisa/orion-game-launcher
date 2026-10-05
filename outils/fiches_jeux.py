"""Prepare les fiches des jeux pour les pages « /jeux » du site d'ORION.

Le site publie une page par jeu : configuration requise, reglages estimes
par carte graphique et prix chez Gamesplanet. Ce script choisit les jeux et
rassemble ce que la page affiche :

1. les jeux vendus en cle Steam par Gamesplanet (flux partenaire) ;
2. leur notoriete sur Steam (nombre d'avis), demandee par lots de cent : les
   DLC, les logiciels et les jeux reserves aux adultes sont ecartes ici ;
3. la fiche Steam des plus connus (configuration minimale et recommandee,
   genres, studio, date de sortie), une par une et sans se presser : Steam
   limite le nombre de fiches par minute.

Les fiches deja relevees sont gardees d'une fois sur l'autre (`ancien`) : un
passage interrompu reprend ou il s'etait arrete. Le fichier produit est lu
par le generateur du site ; aucun PC de joueur ne le lit.

Aucune dependance : bibliotheque standard de Python seulement.
"""
from __future__ import annotations

import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

FLUX = "https://fr.gamesplanet.com/api/v1/products/feed.xml"
ITEMS = "https://api.steampowered.com/IStoreBrowseService/GetItems/v1/"
DETAILS = "https://store.steampowered.com/api/appdetails"
AGENT = "ORION-Launcher (+https://orion-launcher.com)"
STEAM = re.compile(r"^app/(\d{1,10})$")

#: jeux dont la fiche Steam est demandee (les plus connus d'abord)
CANDIDATS = 1100
#: en dessous de ce nombre d'avis, le jeu est trop confidentiel pour une page
AVIS_MINIMUM = 500
#: Steam accepte environ 200 fiches par tranche de cinq minutes
PAUSE = 1.6
ATTENTE_REFUS = 310
#: une fiche est relue apres ce delai (configurations revues par l'editeur)
RELIRE = 30 * 86400
#: duree maximale d'un passage : le suivant reprend la ou celui-ci s'arrete
BUDGET = 50 * 60
#: descripteur de contenu Steam des jeux reserves aux adultes
ADULTE = 3
#: types d'articles Steam : 0 = jeu
JEU = 0


def _get(url: str, params: dict | None = None, delai: int = 40):
    if params:
        url += "?" + urllib.parse.urlencode(params)
    requete = urllib.request.Request(url, headers={
        "User-Agent": AGENT, "Accept-Language": "fr-FR,fr;q=0.9"})
    with urllib.request.urlopen(requete, timeout=delai) as reponse:
        return json.loads(reponse.read().decode("utf-8", "replace"))


# ---------------------------------------------------------------------------
# 1) les jeux vendus par Gamesplanet en cle Steam
# ---------------------------------------------------------------------------
def numeros_du_flux(source) -> list[str]:
    """Numeros Steam des produits PC vendus en cle Steam, sans doublon."""
    vus: dict[str, None] = {}
    for _, e in ET.iterparse(source, events=("end",)):
        if e.tag != "product":
            continue
        try:
            steam = STEAM.match((e.findtext("steam_id") or "").strip())
            cle = (e.findtext("delivery_type") or "").strip().lower()
            sur_pc = (e.findtext("platforms/pc") or "").strip().lower() == "true"
            if steam and cle == "steam" and sur_pc:
                vus.setdefault(steam.group(1))
        finally:
            e.clear()
    return list(vus)


# ---------------------------------------------------------------------------
# 2) notoriete, type et public de chaque article (cent par appel)
# ---------------------------------------------------------------------------
def lire_article(it: dict) -> dict | None:
    """Un article `GetItems` -> {avis, positifs, nom}, ou None s'il n'a pas
    sa place sur le site : introuvable, cache, DLC, logiciel, pour adultes."""
    if not isinstance(it, dict) or it.get("success", 1) != 1 or it.get("visible") is False:
        return None
    if it.get("type") != JEU or ADULTE in (it.get("content_descriptorids") or []):
        return None
    avis = ((it.get("reviews") or {}).get("summary_filtered") or {})
    try:
        return {"avis": int(avis.get("review_count") or 0),
                "positifs": int(avis.get("percent_positive") or 0),
                "nom": " ".join(str(it.get("name") or "").split())}
    except (TypeError, ValueError):
        return None


def classer(appids: list[str], appeler=_get) -> dict[str, dict]:
    """{numero: {avis, positifs, nom}} pour les jeux a garder."""
    out: dict[str, dict] = {}
    for i in range(0, len(appids), 100):
        lot = appids[i:i + 100]
        requete = json.dumps({
            "ids": [{"appid": int(a)} for a in lot],
            "context": {"language": "french", "country_code": "FR", "steam_realm": 1},
            "data_request": {"include_reviews": True, "include_basic_info": True}})
        try:
            items = ((appeler(ITEMS, {"input_json": requete}) or {}).get("response")
                     or {}).get("store_items") or []
        except Exception as exc:                      # un lot perdu n'arrete pas le releve
            print(f"Lot {i // 100} illisible : {exc}", file=sys.stderr)
            continue
        for it in items:
            a = str((it or {}).get("appid") or (it or {}).get("id") or "")
            fiche = lire_article(it) if a in lot else None
            if fiche:
                out[a] = fiche
        time.sleep(0.4 if appeler is _get else 0)
    return out


# ---------------------------------------------------------------------------
# 3) la fiche Steam d'un jeu
# ---------------------------------------------------------------------------
def texte_config(brut) -> str:
    """Configuration Steam (HTML) -> une ligne « Libelle : valeur » par point."""
    if not isinstance(brut, str) or not brut.strip():
        return ""
    t = re.sub(r"(?i)<br\s*/?>|</li>|</p>|</ul>", "\n", brut)
    t = html.unescape(re.sub(r"<[^>]+>", "", t)).replace("\xa0", " ")
    lignes = [" ".join(l.split()) for l in t.splitlines()]
    return "\n".join(l for l in lignes if l)[:1500]


def lire_fiche(data: dict) -> dict | None:
    """Reponse `appdetails` d'un jeu -> la fiche gardee pour le site, ou None
    (pas un jeu, reserve aux adultes, pas de configuration PC)."""
    if not isinstance(data, dict) or data.get("type") != "game":
        return None
    if ADULTE in ((data.get("content_descriptors") or {}).get("ids") or []):
        return None
    pc = data.get("pc_requirements")
    pc = pc if isinstance(pc, dict) else {}
    mini, reco = texte_config(pc.get("minimum")), texte_config(pc.get("recommended"))
    nom = " ".join(str(data.get("name") or "").split())
    if not nom or not mini:
        return None
    sortie = data.get("release_date") or {}
    return {
        "n": nom[:160],
        "d": "" if sortie.get("coming_soon") else str(sortie.get("date") or "")[:40],
        "g": [str(g.get("description"))[:40] for g in (data.get("genres") or [])
              if isinstance(g, dict) and g.get("description")][:4],
        "dev": ", ".join(str(d) for d in (data.get("developers") or [])[:2])[:80],
        "s": " ".join(html.unescape(re.sub(r"<[^>]+>", " ", str(
            data.get("short_description") or ""))).split())[:400],
        "min": mini, "rec": reco,
        "img": str(data.get("header_image") or "")[:300],
        "free": bool(data.get("is_free")),
    }


class Refus(Exception):
    """Steam demande de ralentir."""


def demander_fiche(appid: str, appeler=_get) -> dict | None:
    """La fiche d'un jeu, None si Steam n'en a pas. Leve `Refus` quand Steam
    limite les appels."""
    try:
        corps = appeler(DETAILS, {"appids": appid, "cc": "fr", "l": "french"})
    except urllib.error.HTTPError as exc:
        if exc.code in (403, 429):
            raise Refus(str(exc.code)) from None
        raise
    if corps is None:
        raise Refus("reponse vide")
    bloc = (corps or {}).get(str(appid)) or {}
    return lire_fiche(bloc.get("data")) if bloc.get("success") else None


def completer(notoriete: dict[str, dict], ancien: dict[str, dict], appeler=_get,
              maintenant=time.time, dormir=time.sleep, budget: float = BUDGET,
              candidats: int = CANDIDATS) -> dict[str, dict]:
    """Les fiches des jeux les plus connus. Reprend celles d'`ancien` encore
    fraiches ; s'arrete proprement si Steam refuse ou si le temps est ecoule."""
    choisis = sorted((a for a, n in notoriete.items() if n["avis"] >= AVIS_MINIMUM),
                     key=lambda a: -notoriete[a]["avis"])[:candidats]
    debut, jeux, refus = maintenant(), {}, 0
    for a in choisis:
        connu = ancien.get(a) or {}
        frais = connu and maintenant() - float(connu.get("le") or 0) < RELIRE
        if frais or maintenant() - debut > budget or refus >= 3:
            if connu:                               # on garde ce qu'on sait deja
                jeux[a] = dict(connu, avis=notoriete[a]["avis"],
                               positifs=notoriete[a]["positifs"])
            continue
        try:
            fiche = demander_fiche(a, appeler)
            refus = 0
        except Refus as exc:
            refus += 1
            print(f"Steam ralentit ({exc}) : pause.", file=sys.stderr)
            dormir(ATTENTE_REFUS)
            if connu:
                jeux[a] = connu
            continue
        except Exception as exc:
            print(f"Fiche {a} illisible : {exc}", file=sys.stderr)
            if connu:
                jeux[a] = connu
            dormir(PAUSE)
            continue
        # une fiche sans configuration est notee aussi : elle n'est pas redemandee
        jeux[a] = dict(fiche or {"err": 1}, le=int(maintenant()),
                       avis=notoriete[a]["avis"], positifs=notoriete[a]["positifs"])
        dormir(PAUSE)
    return jeux


def main(sortie: str, ancien_chemin: str = "") -> int:
    ancien: dict = {}
    if ancien_chemin:
        try:
            with open(ancien_chemin, encoding="utf-8") as f:
                ancien = (json.load(f) or {}).get("jeux") or {}
        except (OSError, ValueError):
            print("Pas de fiches precedentes : tout est a relever.")
    requete = urllib.request.Request(FLUX, headers={"User-Agent": AGENT})
    with urllib.request.urlopen(requete, timeout=120) as reponse:
        appids = numeros_du_flux(reponse)
    print(f"{len(appids)} produits en cle Steam chez Gamesplanet.")
    if len(appids) < 2000:
        print("Flux trop court : rien n'est publie.", file=sys.stderr)
        return 1
    notoriete = classer(appids)
    print(f"{len(notoriete)} jeux gardes (ni DLC, ni logiciel, ni pour adultes).")
    if len(notoriete) < 500:
        print("Steam n'a presque rien rendu : rien n'est publie.", file=sys.stderr)
        return 1
    jeux = completer(notoriete, ancien)
    lisibles = sum(1 for j in jeux.values() if not j.get("err"))
    document = {"v": 2, "releve": int(time.time()), "jeux": jeux}
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(document, f, ensure_ascii=False, separators=(",", ":"))
    print(f"{len(jeux)} fiches, dont {lisibles} avec une configuration.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "fiches-jeux.json",
                  sys.argv[2] if len(sys.argv) > 2 else ""))
