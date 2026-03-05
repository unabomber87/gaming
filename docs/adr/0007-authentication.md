


# ADR 0007 - Authentication Multi-plateformes et Admin

Décisions:
- OAuth2 pour login joueur sur Steam, Epic, PSN, Xbox
- Login/password interne pour accès admin
- Redirection selon type d'utilisateur
- Backend Laravel avec endpoints séparés pour chaque plateforme
- Frontend boutons clairs avec logos pour chaque plateforme
- Scalabilité pour ajouter facilement de nouvelles plateformes
