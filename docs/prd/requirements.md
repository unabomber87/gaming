
# Functional Requirements: Page d'accueil

- Afficher les informations de profil utilisateur
- Afficher les stats globales et achievements
- Accéder aux recommandations IA
- Accéder rapidement aux documents et backlog
- Boutons clairs pour chaque plateforme connectée
- Gestion de la sécurité et des sessions



# Functional Requirements: Page Login

- Authentification OAuth2 pour Steam, Epic, PSN, Xbox
- Authentification login/password interne pour admin
- Redirection vers page d'accueil ou dashboard admin selon rôle
- Session sécurisée (JWT ou backend)
- Interface frontend responsive et claire (boutons plateformes)
- Gestion des erreurs (token expiré, mauvais login)
- Préparer l'ajout de nouvelles plateformes futures



# Functional Requirements: Login, Page d'accueil et Dashboard Admin

- Authentification OAuth2 pour Steam, Epic, PSN, Xbox
- Authentification login/password pour admin
- Redirection selon rôle
- Page d'accueil joueur:
   - Résumé profil, stats, achievements
   - Recommandations IA
   - Accès rapide aux docs et backlog
- Dashboard admin:
   - Gestion utilisateurs
   - Statistiques globales
   - Accès aux outils d'administration
- Frontend responsive et boutons clairs
- Gestion sécurisée des sessions (JWT / backend)
- Gestion des erreurs (mauvais login, token expiré)
- Préparer l'ajout de nouvelles plateformes à l'avenir



# Non-functional Requirements: Page Login & Page d'accueil

- Performance: temps de chargement < 2s pour page d'accueil
- Sécurité: OAuth2 sécurisé (state, redirect URI, token exchange)
- Login/password admin stocké en hash sécurisé (bcrypt)
- Frontend responsive (desktop / mobile)
- Scalabilité: facile ajout nouvelles plateformes / widgets
- Gestion des erreurs et messages clairs



# Non-functional Requirements: Page Login & Page d'accueil

- Performance: temps de chargement page accueil < 2s
- Sécurité: OAuth2 sécurisé (state, redirect URI, token exchange)
- Login/password admin stocké en hash sécurisé (bcrypt)
- Frontend responsive (desktop / mobile)
- Scalabilité: facile ajout nouvelles plateformes / widgets
- Gestion des erreurs et messages clairs
