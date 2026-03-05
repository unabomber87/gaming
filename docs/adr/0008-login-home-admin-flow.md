


# ADR 0008 - Login → Page d'accueil / Dashboard Admin

Décisions:
- OAuth2 pour login joueur sur plateformes gaming
- Login/password interne pour admins
- Redirection automatique selon rôle
- Backend Laravel avec controllers séparés: AuthController, HomeController, AdminController
- Frontend organisé en pages distinctes pour login, home, admin
- Scalabilité pour ajouter facilement nouvelles plateformes ou fonctionnalités



# ADR 0008 - Décisions complémentaires

Décisions:
- OAuth2 pour login joueur sur Steam, Epic, PSN, Xbox
- Login/password interne pour admins
- Redirection automatique selon rôle (joueur → page accueil, admin → dashboard)
- Prévoir l'ajout futur de nouvelles plateformes facilement
- Structuration backend: AuthController, HomeController, AdminController
- Structuration frontend: pages/login, pages/home, pages/admin
