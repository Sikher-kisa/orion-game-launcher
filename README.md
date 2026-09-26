# ORION Game Launcher

**Launcher de jeux PC gratuit pour Windows.** ORION trouve tous les jeux installés sur la machine, où qu'ils soient, et les lance avec des réglages graphiques calculés pour votre carte, votre écran et ce que vous voulez faire de la partie.

🌐 **Site officiel : [orion-game-launcher.pages.dev](https://orion-game-launcher.pages.dev/)**

⬇️ **[Télécharger la dernière version (Installateur-ORION.exe)](https://github.com/Sikher-kisa/orion-game-launcher/releases/latest/download/Installateur-ORION.exe)** · Windows 10 et 11, 64 bits

> **Version d'essai.** ORION est en phase de test ouverte : tout fonctionne, mais tout peut encore bouger. Des mises à jour arrivent régulièrement, et vos retours décident des prochaines.

## Ce qui est déjà en place

- **Détection des jeux** : Steam, Epic, GOG, Ubisoft Connect, EA app, Battle.net, Microsoft Store, Ankama, dossiers personnels. Doublons fusionnés, jeux désinstallés retirés automatiquement.
- **Fiches de jeu** : jaquettes officielles, captures d'écran, temps de jeu, actualités traduites en français.
- **Réglages calculés** : profils Esport, Détente et Photoréaliste adaptés à votre carte graphique et à votre écran, avec aperçu, confirmation, sauvegarde et restauration en un clic.
- **Mesure des performances** : images par seconde réelles, 1 % et 0,1 % bas, ajustements proposés.
- **Boutique** : prix le plus bas sur les boutiques officielles et agréées, actualisé toutes les douze minutes ; encart « marché gris » séparé avec ses risques.
- **Jeux gratuits et envies** : cadeaux, week-ends gratuits, alertes de baisse de prix.
- **Sauvegardes** (copie possible dans OneDrive, Google Drive ou Dropbox), **stockage, manette, IA facultative.**
- **Mode discret en jeu, jeux possédés non installés, interface en anglais.**
- **Mise à jour en un clic** : la version installée s'affiche en bas à gauche ; quand une nouvelle version sort, un clic l'installe (empreinte vérifiée, remplacement tout ou rien) et ORION redémarre.

## Installation

1. Téléchargez `Installateur-ORION.exe` depuis la page [Releases](https://github.com/Sikher-kisa/orion-game-launcher/releases).
2. Si Windows affiche « Windows a protégé votre ordinateur », cliquez sur **Informations complémentaires** puis **Exécuter quand même** : l'installateur n'est pas encore signé numériquement.
3. Choisissez le dossier, validez. Aucun droit administrateur n'est demandé.

L'empreinte SHA-256 de chaque version est indiquée dans ses notes de publication.

Ensuite, ORION se met à jour tout seul : l'encart en bas à gauche signale chaque nouvelle version, un clic la télécharge, vérifie son empreinte, l'installe puis redémarre ORION. Vos données sont conservées.

## Journal des versions

Toutes les étapes depuis la première version : [CHANGELOG.md](CHANGELOG.md).

## Signaler un problème

Ouvrez un ticket dans l'onglet [Issues](https://github.com/Sikher-kisa/orion-game-launcher/issues) en précisant la version d'ORION, le jeu concerné et ce qui s'est passé.

## Financement

ORION est gratuit, sans publicité, sans compte et sans télémétrie. Le projet vit uniquement de **dons libres** ([PayPal](https://paypal.me/FoxSikh)) et de **liens partenaires** vers certaines boutiques, qui ne changent ni le prix payé ni l'ordre des offres. Aucune contrepartie n'est demandée à l'utilisateur.

## Comment c'est fait

ORION est un projet **vibe codé** : développé en dialoguant avec Claude (Anthropic), qui propose l'architecture, écrit et teste le code, pendant que l'auteur fixe le cap et essaie chaque version. Python 3.13, PySide6 / Qt 6, architecture à plugins.

Recettes de réglages partagées : [orion-recettes](https://github.com/Sikher-kisa/orion-recettes).
