\# 🤝 Guide de Contribution



\## 📌 Branches

| Branche | Rôle |

|---|---|

| `main` | Production stable |

| `develop` | Intégration des features |

| `feature/\*` | Nouvelles fonctionnalités |

| `hotfix/\*` | Corrections urgentes |



\## ✍️ Nommage des commits

Toujours utiliser ce format :

\- `feat:` → nouvelle fonctionnalité

\- `fix:` → correction de bug

\- `chore:` → configuration, setup

\- `docs:` → documentation

\- `refactor:` → refactoring de code



\## 🔀 Règles des Pull Requests

\- Toujours créer une PR pour merger dans develop ou main

\- Titre clair et descriptif

\- Ajouter P1 comme reviewer obligatoire

\- Ne jamais pusher directement sur main



\## 🌿 Créer une branche

```bash

git checkout develop

git checkout -b feature/nom-de-la-feature

```



\## 📤 Pousser son travail

```bash

git add .

git commit -m "feat: description claire"

git push origin feature/nom-de-la-feature

```

Ensuite ouvrir une Pull Request sur GitHub.

