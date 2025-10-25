# Déploiement sur GitHub Pages

Ce dossier contient une version statique du site AnimeZone optimisée pour GitHub Pages.

## Comment déployer sur GitHub Pages

Suivez ces étapes pour déployer votre site sur GitHub Pages:

1. **Créez un nouveau dépôt GitHub** (si ce n'est pas déjà fait)
   - Connectez-vous à votre compte GitHub
   - Créez un nouveau dépôt nommé `animezone` (ou un autre nom de votre choix)

2. **Préparez les fichiers statiques**
   - Copiez tous les fichiers du dossier `static/` dans un dossier temporaire
   - Renommez `github-pages-index.html` en `index.html`
   - Créez des copies des fichiers spécifiques nécessaires:
     - Copiez `index.html` et renommez la copie en `search.html`
     - Créez un dossier `anime` et copiez-y `index.html` (cela servira pour les pages d'anime)

3. **Téléchargez les fichiers sur GitHub**
   - Clonez votre dépôt localement: `git clone https://github.com/VOTRE_NOM_UTILISATEUR/animezone.git`
   - Copiez tous les fichiers préparés dans ce dossier
   - Effectuez un commit et un push:
     ```
     git add .
     git commit -m "Initial commit for GitHub Pages"
     git push origin main
     ```

4. **Activez GitHub Pages**
   - Allez sur la page de votre dépôt sur GitHub
   - Cliquez sur "Settings" (Paramètres)
   - Descendez jusqu'à la section "GitHub Pages"
   - Sélectionnez la branche "main" comme source et cliquez sur "Save"
   - GitHub vous fournira l'URL où votre site est accessible (généralement `https://VOTRE_NOM_UTILISATEUR.github.io/animezone/`)

5. **Vérifiez le déploiement**
   - Attendez quelques minutes que GitHub déploie votre site
   - Visitez l'URL fournie pour vérifier que tout fonctionne correctement

## Limitations de la version GitHub Pages

Cette version est une version simplifiée du site complet, avec les limitations suivantes:

1. **Pas de backend**: Toutes les fonctionnalités qui nécessitent un serveur Python Flask sont désactivées
2. **Données limitées**: Seules les données récupérées via l'API Anime-Sama sont disponibles
3. **Pas de compte utilisateur**: Les fonctionnalités comme les favoris ou le suivi de progression ne sont pas disponibles
4. **Cache local**: Les données sont mises en cache dans le navigateur pour limiter les requêtes API

## Résolution des problèmes connus

### Erreurs CORS (403 Forbidden)

Si vous rencontrez des erreurs "403 Forbidden" ou des problèmes CORS:

1. Le script `cors-proxy.js` essaie automatiquement différents proxys CORS publics
2. Si tous échouent, essayez de visiter manuellement l'un des services de proxy suivants pour les autoriser:
   - https://cors-anywhere.herokuapp.com/
   - https://corsproxy.io/

### Films qui ne s'affichent pas correctement

Le script `anime-fix.js` a été spécialement conçu pour résoudre ce problème. Si vous rencontrez encore des difficultés:

1. Vérifiez que `anime-fix.js` est bien chargé dans la page
2. Ouvrez la console du navigateur pour voir s'il y a des erreurs
3. Essayez de rafraîchir la page après son chargement complet

## Mise à jour du site

Pour mettre à jour votre site sur GitHub Pages:

1. Modifiez les fichiers nécessaires
2. Effectuez un nouveau commit et push vers GitHub
3. GitHub Pages déploiera automatiquement les changements

## Support

Pour toute question ou problème, veuillez ouvrir une issue sur le dépôt GitHub.

---

*Note: Cette documentation est spécifique à la version GitHub Pages. Pour la documentation complète du site, veuillez consulter le README principal.*