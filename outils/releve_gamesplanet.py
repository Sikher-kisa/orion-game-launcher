"""Releve le flux de prix de Gamesplanet et en tire un fichier compact.

Gamesplanet (distributeur officiel, partenaire d'ORION) publie tous ses prix
dans un flux XML d'une douzaine de mega-octets et autorise ORION a le garder
en cache pour le redistribuer a ses utilisateurs (courriel du 5 octobre
2026). Ce script, lance toutes les vingt minutes par GitHub, le lit une fois
pour tout le monde : aucun PC de joueur n'interroge Gamesplanet.

Sortie : un fichier JSON ou chaque numero Steam mene aux produits vendus par
Gamesplanet pour ce jeu (le jeu, ses editions) :

    {"v": 1, "releve": 1791200000, "boutique": "fr", "devise": "EUR",
     "jeux": {"2183900": [["Warhammer 40,000: Space Marine 2", 53.99, 59.99,
                            "warhammer-40-000-space-marine-2-steam-key--5451-1",
                            "steam", "", ""]]}}

Champs d'un produit : nom, prix, prix normal, fin de l'adresse de la fiche,
type de cle, pays autorises et pays exclus (limites a la zone euro, la seule
ou ORION affiche ces prix ; vide = pas de restriction).

Aucune dependance : bibliotheque standard de Python seulement.
"""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

FLUX = "https://fr.gamesplanet.com/api/v1/products/feed.xml"
AGENT = "ORION-Launcher (+https://orion-launcher.com)"
ZONE_EURO = {"FR", "BE", "LU", "DE", "AT", "ES", "IT", "PT", "NL", "IE", "FI", "GR",
             "MT", "CY", "EE", "LV", "LT", "SK", "SI", "HR", "MC"}
FICHE = re.compile(r"^https://fr\.gamesplanet\.com/game/([a-z0-9_-]{3,200})$")
STEAM = re.compile(r"^app/(\d{1,10})$")
#: en dessous, le flux est tronque ou vide : on ne publie rien plutot que de
#: faire disparaitre les prix chez tous les joueurs
MINIMUM = 2000


def _prix(texte) -> float | None:
    try:
        v = round(float(texte), 2)
    except (TypeError, ValueError):
        return None
    return v if 0 < v < 1000 else None


def _pays(texte) -> set[str]:
    return {c.strip().upper() for c in (texte or "").split(",") if c.strip()}


def lire(source) -> dict[str, list]:
    """`source` : fichier ou flux ouvert en binaire. Rend {numero Steam: [produits]}."""
    jeux: dict[str, list] = {}
    for _, e in ET.iterparse(source, events=("end",)):
        if e.tag != "product":
            continue
        try:
            steam = STEAM.match((e.findtext("steam_id") or "").strip())
            fiche = FICHE.match((e.findtext("link") or "").strip())
            prix, normal = _prix(e.findtext("price")), _prix(e.findtext("price_base"))
            nom = " ".join((e.findtext("name") or "").split())[:160]
            sur_pc = (e.findtext("platforms/pc") or "").strip().lower() == "true"
            if not (steam and fiche and prix and normal and nom and sur_pc) or prix > normal:
                continue
            autorises = _pays(e.findtext("country_whitelist"))
            exclus = _pays(e.findtext("country_blacklist")) & ZONE_EURO
            if autorises:
                # « EU » designe toute l'Union dans les listes de Gamesplanet
                autorises = ZONE_EURO if "EU" in autorises else autorises & ZONE_EURO
                if not autorises:
                    continue                      # pas vendu en zone euro
                if autorises == ZONE_EURO:
                    autorises = set()
            type_cle = re.sub(r"[^a-z0-9]", "", (e.findtext("delivery_type") or "").lower())[:20]
            jeux.setdefault(steam.group(1), []).append([
                nom, prix, normal, fiche.group(1), type_cle,
                ",".join(sorted(autorises)), ",".join(sorted(exclus))])
        finally:
            e.clear()
    for produits in jeux.values():
        produits.sort(key=lambda p: (p[2], p[1], p[0]))       # l'edition standard d'abord
    return dict(sorted(jeux.items(), key=lambda kv: int(kv[0])))


def construire(source, maintenant: float | None = None) -> dict:
    jeux = lire(source)
    return {"v": 1, "releve": int(maintenant or time.time()), "boutique": "fr",
            "devise": "EUR", "jeux": jeux}


def main(sortie: str) -> int:
    requete = urllib.request.Request(FLUX, headers={"User-Agent": AGENT})
    with urllib.request.urlopen(requete, timeout=120) as reponse:
        document = construire(reponse)
    n = sum(len(v) for v in document["jeux"].values())
    if n < MINIMUM:
        print(f"Flux trop court ({n} produits) : rien n'est publie.", file=sys.stderr)
        return 1
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(document, f, ensure_ascii=False, separators=(",", ":"))
    print(f"{len(document['jeux'])} jeux, {n} produits.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "gamesplanet-fr.json"))
