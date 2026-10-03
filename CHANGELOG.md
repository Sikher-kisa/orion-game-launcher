# Journal des versions d'ORION

ORION est en version d'essai : chaque version est testée sur une vraie machine de joueur avant de sortir. Les grandes étapes, de la plus récente à la première.

## 1.9.3 — Les accents sont de retour
- Toute l'interface affiche désormais les accents du français : menus, réglages, conseils, tuto et installateur.
- Site : le lien « Faire un don » ouvre une petite fenêtre par-dessus la page (code QR et lien PayPal) au lieu de la remplacer.

## 1.9.2 — Nouvelle adresse : orion-launcher.com
- Le site d'ORION déménage sur orion-launcher.com : l'aide, les réglages et le calendrier des sorties pointent vers la nouvelle adresse.
- Lien partenaire Gamesplanet, distributeur officiel (le prix ne change pas).

## 1.9.1 — Connexion GOG avec Google
- Comptes : nouveau bouton « Se connecter avec mon navigateur » pour GOG. Google refuse les fenêtres intégrées aux applications ; la connexion se fait donc dans votre navigateur habituel, puis ORION reconnaît l'adresse de fin de connexion dès que vous la copiez.
- Lecteur vidéo : la page de consentement de YouTube n'apparaît plus.
- Boutique : les lots de formations n'apparaissent plus parmi les jeux ; la fiche affiche « Chargement » pendant la recherche.
- Lien partenaire Kinguin ajouté (le prix ne change pas).
- Conseils : plus de faux conseil sur le chipset AMD d'un PC Intel, ni sur les périphériques audio virtuels.

## 1.9.0 — Une boutique, des fiches et des réglages entièrement repensés
- Boutique repensée : « À la une » pour les gros jeux du moment, « Pour vous » avec des suggestions tirées de votre bibliothèque (jamais un jeu déjà possédé), grosses promos, plus bas historique, gratuits, et une recherche avec images.
- Les jeux gratuits rejoignent la Boutique (onglet « Gratuits en ce moment »). Logiciels et formations sont masqués par défaut : case « Afficher les applications ».
- Fiche de jeu repensée : Infos (studio, éditeur, sortie, genres, avis, succès), succès compacts, captures et vidéos dans un lecteur intégré (gameplay en français, lives, bande-annonce). Plus de prix ni de marché gris pour un jeu déjà possédé ; le lien Boutique reste là.
- Nouveau profil « Recommandé » : le plus beau réglage qui tient environ 60 images par seconde sur votre PC, avec DLSS ou FSR quand le jeu le permet. Un curseur Performances ↔ Qualité pour ajuster.
- Réglages fiables : état honnête (« Réglages appliqués : 12 sur 14 »), relus juste avant le lancement, fichiers en lecture seule respectés, et plus de confirmation à chaque partie.
- Ma machine : « Ce que votre PC peut faire » en une seule liste claire, avec le niveau fluide de chaque jeu, les filtres Tous / Mes jeux / À acheter et le tri.
- Conseils : analyse de tous les pilotes (graphique, chipset, réseau, audio, stockage, USB, Bluetooth) et des réglages Windows et matériel : mode Jeu, planification GPU, alimentation, fréquence d'écran, XMP/EXPO, mémoire en simple canal, disque plein, jeux sur disque dur, redémarrage en attente, fichier d'échange.
- Stockage : « Sauvegarder sur un autre disque » (copie vérifiée, le jeu installé n'est jamais modifié, progression en %, restauration et suppression). « Recalculer » remesure vraiment. Les jeux déplacés avec l'ancienne fonction peuvent être ramenés.
- Page Sorties : les grosses sorties toutes plateformes avec compte à rebours, renouvelées toutes seules d'après les jeux Steam les plus suivis ; la liste des sorties consoles est mise à jour en ligne.
- Joueurs en ligne (Steam) dans la fiche des jeux en ligne, et valeur de la bibliothèque (prix actuels hors promotion, à titre d'information).
- Comptes : connexion Xbox sans clé de sécurité (le mot de passe est proposé), connexion Google sur GOG mieux gérée, avec un message clair si Google refuse les fenêtres intégrées.
- Titres reconnus sans tenir compte de la ponctuation (« RuneScape - Dragonwilds » = « RuneScape: Dragonwilds ») ; un jeu sans captures le dit au lieu de laisser un vide.
- Fiabilité : relecture complète du code ; installation et mises à jour plus sûres (jamais dans un dossier existant, ORION toujours relancé, mise à jour reportée après la partie) ; base de données et réglages protégés contre les fichiers abîmés ; aucun secret dans le journal.
- Liens partenaires sur certaines boutiques : le prix ne change pas, une petite commission finance ORION (désactivable dans Réglages).

## 1.8 — Vos comptes, vos succès et ce que votre PC peut faire
- Nouvelle page Comptes : Steam (connexion officielle), GOG et Xbox (connexions non officielles, signalées comme telles), dans une fenêtre intégrée. ORION ne voit jamais votre mot de passe : seul un jeton, chiffré par Windows, est gardé sur ce PC.
- Profil de chaque plateforme : niveau, XP, badges, Gamerscore, tous les jeux du compte et leur temps de jeu.
- Succès dans la fiche de chaque jeu : obtenus, manquants (les plus accessibles d'abord) et rareté mondiale.
- Les jeux de vos comptes rejoignent la bibliothèque (non installés) et leur temps de jeu est repris.
- Déplacer un jeu vers un autre disque (page Stockage) : copie vérifiée avant de libérer la place, le jeu reste visible pour son launcher. Retour sur le disque d'origine en un clic.
- Ce que votre PC peut faire (page Ma machine) : note de la machine, jeux fluides en Ultra, Haute et Moyenne, images par seconde attendues et meilleure offre. Chaque résultat dit sa source : mesure sur votre PC, mesures de la communauté ou estimation prudente.
- Ubisoft, Rockstar, Battle.net, Epic et EA : ce qui est possible et pourquoi, clairement affiché.

## 1.7.2 — La version en bas à gauche, la mise à jour en un clic
- La version installée s'affiche en bas à gauche. ORION surveille la page officielle du projet et l'encart s'allume quand une nouvelle version sort.
- Un clic sur l'encart télécharge la nouvelle version, vérifie son empreinte, l'installe et redémarre ORION. La progression s'affiche sur place.
- Plus de fenêtre de mise à jour à chaque démarrage : un rappel discret suffit. L'encart peut être masqué dans Réglages > Mises à jour.
- Mise à jour tout ou rien : la nouvelle version est préparée à côté de l'ancienne, puis échangée d'un coup. Si c'est impossible, l'ancienne reste intacte et ORION redémarre dessus.

## 1.7 — Mises à jour automatiques, mode discret et bibliothèque complète
- Mise à jour automatique : ORION vérifie les nouvelles versions, contrôle l'empreinte du fichier et s'installe en un clic.
- Mode discret en jeu : pendant une partie, même lancée depuis Steam ou Epic, ORION met en pause ses tâches de fond. Le temps de jeu est aussi compté hors d'ORION.
- Jeux possédés mais non installés (Steam, Epic, GOG) : visibles en grisé, avec un bouton pour les installer.
- Bouton « Signaler un problème » : un rapport sans données personnelles, prêt à envoyer. Un plantage n'est plus silencieux.
- Sauvegardes de parties copiées dans OneDrive, Google Drive ou Dropbox si vous le souhaitez.
- Recettes communautaires vérifiées avant usage : aucune ne peut écrire hors du dossier du jeu.
- Interface disponible en anglais.
- Données rangées dans une base locale : plus rapide, et plus de fichier abîmé si le PC s'éteint pendant une écriture.
- Connexions mieux réparties entre les services, indicateur « hors ligne ».

## 1.6 — Fiches de jeu enrichies et première version publique
- Captures d'écran dans la fiche de chaque jeu, avec visionneuse.
- Actualités et mises à jour des jeux traduites intégralement en français, texte d'origine à un clic.
- Encart « marché gris » : revendeurs de clés et leurs risques, toujours séparés des offres sûres.
- Un jeu désinstallé disparaît tout seul, sans relancer d'analyse.
- Jaquettes des jeux tout juste sortis enfin récupérées.
- Première version publique, avec son site et ses téléchargements.

## 1.5 — La Boutique et une bibliothèque plus propre
- Boutique : tous les jeux, le prix le plus bas sur des sites sûrs uniquement, actualisée toutes les 12 minutes.
- Recherche tolérante : fautes de frappe, phonétique et sigles (gta, bg3…).
- Menu rapide ⋮ sur chaque jaquette.
- Doublons fusionnés (un même jeu vu par Steam et par Windows).
- Nouvelle source : Ankama (Dofus, Wakfu).
- Envies plus lisibles, jeux « à venir » reconnus.
- ORION ménage les serveurs de Steam : pause automatique en cas de refus.

## 1.4 — Soutien au projet
- Fenêtre de soutien avec QR code PayPal.
- Lien de don verrouillé dans l'application : personne ne peut le détourner.

## 1.3 — Installateur et assistant IA
- Installateur autonome : raccourcis, entrée dans « Applications installées », désinstallation propre.
- Un seul ORION à la fois : un second lancement rappelle la fenêtre.
- Assistant IA facultatif (Claude, ChatGPT, Gemini, Mistral, Ollama) : il apprend un jeu inconnu à ORION et explique les baisses de performances.
- Bannière d'accueil, navigation à la manette et affichage salon.

## 1.2 — Jeux gratuits, prix et performances
- Jeux gratuits du moment : Epic, Steam, GOG, Prime Gaming et autres, avec leurs conditions.
- Prix, avis et plus bas historique ; liste d'envies avec alertes.
- Mesure des images par seconde réelles (PresentMon) et ajustements proposés.
- Sauvegardes de parties archivées et restaurables.

## 1.1 — Recettes partagées
- Recettes de réglages partagées par la communauté, téléchargées automatiquement.

## 1.0 — Première version
- Détection des jeux Steam, Epic, GOG, Ubisoft, EA, Battle.net, Xbox, des dossiers de jeux et des programmes installés.
- Jaquettes, bannières et logos récupérés automatiquement.
- Analyse du PC : processeur, carte graphique, mémoire, écrans et tous leurs modes.
- Trois profils de lancement (Esport, Détente, Photoréaliste) qui règlent le jeu et l'écran, avec sauvegarde et restauration.
- Temps de jeu par jeu, tri et filtres.
