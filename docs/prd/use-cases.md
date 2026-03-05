
# Use Case: Page d'accueil Dashboard Gaming

Objectif:
- Offrir un aperçu rapide des informations importantes pour l'utilisateur
- Accès aux recommandations de jeux, stats de joueur, backlog et notifications

Fonctionnalités:
1. Résumé du profil utilisateur (pseudo, avatar, plateforme connectée)
2. Statistiques principales (jeux joués, heures, achievements)
3. Recommandations personnalisées de jeux
4. Accès rapide aux docs PRD et ADR
5. Notifications et mises à jour du backlog
6. Boutons d'accès aux plateformes connectées (Steam, Epic, PSN, Xbox)



# Use Case: Page Login Multi-plateformes et Admin

Objectif:
- Permettre aux joueurs de se connecter via Steam, Epic Games, PSN, Xbox
- Permettre aux administrateurs de se connecter via login/password interne

Fonctionnalités:
1. Login via Steam / Epic / PSN / Xbox
2. Login via formulaire admin interne
3. Redirection selon type d'utilisateur:
   - Joueur → Page d'accueil
   - Admin → Dashboard admin
4. Gestion sécurisée des sessions
5. Gestion des erreurs et messages clairs



# Use Case: Login Multi-plateformes et Dashboard Admin

Objectif:
- Permettre aux joueurs de se connecter via Steam, Epic, PSN, Xbox
- Permettre aux administrateurs de se connecter via login/password interne
- Rediriger les joueurs vers la page d'accueil
- Rediriger les admins vers le dashboard admin

Flux complet:
1. L’utilisateur arrive sur la page login
2. Choisit la méthode:
   - Plateformes gaming (OAuth2) → récupération infos publiques
   - Admin (login/password) → vérification interne
3. Redirection selon rôle:
   - Joueur → Page d'accueil
   - Admin → Dashboard admin
4. Gestion sécurisée des sessions et tokens
5. Gestion des erreurs et messages clairs



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
