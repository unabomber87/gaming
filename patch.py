"""
Script conceptuel : Amélioration de la documentation pour login/page d'accueil/admin
- Ajout workflow détaillé dans use-cases.md et ADR
- Ajout schéma textuel / diagramme simplifié
- Ajout Non-functional requirements dans requirements.md
- Complétion ADR spécifique login/admin
"""

from pathlib import Path

ROOT = Path("./")

# Fichiers docs à mettre à jour
USECASE_FILE = ROOT / "docs" / "prd" / "use-cases.md"
REQUIREMENTS_FILE = ROOT / "docs" / "prd" / "requirements.md"
ADR_FILE = ROOT / "docs" / "adr" / "0008-login-home-admin-flow.md"

# 1️⃣ Workflow détaillé et schéma textuel
workflow_text = """
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
"""

# 2️⃣ Non-functional requirements
non_functional_text = """
# Non-functional Requirements: Page Login & Page d'accueil

- Performance: temps de chargement < 2s pour page d'accueil
- Sécurité: OAuth2 sécurisé (state, redirect URI, token exchange)
- Login/password admin stocké en hash sécurisé (bcrypt)
- Frontend responsive (desktop / mobile)
- Scalabilité: facile ajout nouvelles plateformes / widgets
- Gestion des erreurs et messages clairs
"""

# 3️⃣ Compléter l'ADR login/admin
adr_update_text = """
# ADR 0008 - Décisions complémentaires

Décisions:
- OAuth2 pour login joueur sur Steam, Epic, PSN, Xbox
- Login/password interne pour admins
- Redirection automatique selon rôle (joueur → page accueil, admin → dashboard)
- Prévoir l'ajout futur de nouvelles plateformes facilement
- Structuration backend: AuthController, HomeController, AdminController
- Structuration frontend: pages/login, pages/home, pages/admin
"""

# 4️⃣ Écriture / ajout dans les fichiers docs
for path, content in [
    (USECASE_FILE, "\n\n" + workflow_text),
    (REQUIREMENTS_FILE, "\n\n" + non_functional_text),
    (ADR_FILE, "\n\n" + adr_update_text)
]:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)
    print(f"Documentation améliorée : {path}")

# 5️⃣ Ajouter le schéma textuel dans README frontend
README_FRONT = ROOT / "frontend" / "pages" / "login" / "README.md"
with open(README_FRONT, "a", encoding="utf-8") as f:
    f.write("\n\n# Schéma de redirection Login\n")
    f.write(workflow_text)
print(f"Schéma workflow ajouté au README frontend : {README_FRONT}")

print("Amélioration des docs et ADR terminée avec workflow, non-functional requirements et diagramme ASCII.")