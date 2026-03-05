# login - frontend
Placeholder pour structure et composants.


# Schéma de redirection Login

# Workflow Complet: Login → Page d'accueil / Dashboard Admin

Flux Utilisateur:
1. L'utilisateur arrive sur la page login
2. Choisit la méthode de connexion:
   - Steam / Epic / PSN / Xbox (OAuth2)
   - Admin login/password interne
3. Authentification:
   - Joueur: récupération infos publiques via API
   - Admin: vérification interne login/password
4. Redirection:
   - Joueur → Page d'accueil (profil, stats, recommandations)
   - Admin → Dashboard admin
5. Gestion de session sécurisée (JWT ou session backend)
6. Gestion des erreurs (mauvais login, token expiré)

Schéma textuel (ASCII simplifié):

      +----------------+
      | Page Login     |
      +----------------+
             |
   +---------+---------+
   |                   |
   v                   v
 Joueur               Admin
   |                   |
   v                   v
Page Accueil       Dashboard Admin
   |
   v
Résumé infos & recommandations
# login - Placeholder
Structure et rôle du dossier.

## Schéma workflow

# Workflow Complet: Login → Page d'accueil / Dashboard Admin

Flux Utilisateur:
1. L'utilisateur arrive sur la page login
2. Choisit la méthode de connexion:
   - Steam / Epic / PSN / Xbox (OAuth2)
   - Admin login/password interne
3. Authentification:
   - Joueur: récupération infos publiques via API
   - Admin: vérification interne login/password
4. Redirection:
   - Joueur → Page d'accueil (profil, stats, recommandations)
   - Admin → Dashboard admin
5. Gestion de session sécurisée (JWT ou session backend)
6. Gestion des erreurs (mauvais login, token expiré)

Schéma textuel ASCII simplifié:

      +----------------+
      | Page Login     |
      +----------------+
             |
   +---------+---------+
   |                   |
   v                   v
 Joueur               Admin
   |                   |
   v                   v
Page Accueil       Dashboard Admin
   |
   v
Résumé infos & recommandations
