


# ADR 0008 - Login → Page d'accueil / Dashboard Admin

Décisions:
- OAuth2 pour login joueur sur plateformes gaming
- Login/password interne pour admins
- Redirection automatique selon rôle
- Backend Laravel avec controllers séparés: AuthController, HomeController, AdminController
- Frontend organisé en pages distinctes pour login, home, admin
- Scalabilité pour ajouter facilement nouvelles plateformes ou fonctionnalités
