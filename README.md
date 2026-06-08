# 🚗 AutoLoc — Gestion de Location de Voitures avec IA

> Application web de gestion de location de voitures avec assistant IA intégré (Groq API)

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey?logo=flask)
![Groq](https://img.shields.io/badge/Groq-llama--3.3--70b-orange)
![SonarCloud](https://img.shields.io/badge/SonarCloud-Passed-brightgreen?logo=sonarcloud)
![Version](https://img.shields.io/badge/version-v1.0-green)
![License](https://img.shields.io/badge/license-Academic-blue)

---

## 🎯 Description

**AutoLoc** est une application web développée avec Flask permettant à une agence de location de voitures de gérer son catalogue, ses réservations et d'offrir à ses clients un **assistant IA intelligent** capable de recommander la voiture idéale selon leurs besoins.

---

## ✨ Fonctionnalités

### 🔧 CRUD — Gestion du catalogue
- ✅ Ajouter une voiture (marque, modèle, type, places, prix/jour, transmission, carburant)
- ✅ Modifier les informations d'une voiture existante
- ✅ Supprimer une voiture du catalogue
- ✅ Visualiser le catalogue complet avec filtres

### 🤖 Assistant IA — Alex (Groq API)
- ✅ Chatbot intégré accessible via bouton "Assistant IA"
- ✅ Pose 5 questions séquentielles : budget, passagers, type de trajet, transmission, carburant
- ✅ Recommande la voiture la plus adaptée parmi le catalogue
- ✅ Powered by **Groq llama-3.3-70b-versatile** (gratuit)

### 📊 Tableau de bord
- ✅ Compteur voitures disponibles et réservations en temps réel
- ✅ Interface Admin séparée de l'interface client

---

## 🏗️ Architecture

```
gestion-location-voitures/
├── app.py                  # Serveur Flask — routes CRUD + chatbot IA
├── requirements.txt        # Dépendances Python
├── .env.example            # Template configuration clé API
├── .gitignore              # Fichiers exclus du repo
├── README.md               # Documentation
├── templates/
│   ├── index.html          # Page catalogue client
│   └── admin.html          # Page administration
└── static/
    ├── css/
    │   └── style.css       # Styles de l'application
    └── js/
        └── chatbot.js      # Logique du chatbot IA frontend
```

### Design Pattern — Strategy

Le pattern **Strategy** est appliqué sur le module IA :

```
ChatbotStrategy (classe abstraite)
    └── get_response(message, history) → str

GroqChatbotStrategy (implémentation concrète)
    └── Appelle l'API Groq llama-3.3-70b

ChatbotContext (contexte)
    └── execute(message, history) → délègue à la stratégie active
```

**Avantage :** changer de fournisseur IA (Groq → OpenAI → Mistral) sans toucher au code des routes Flask.

---

## 🚀 Installation

### 1. Cloner le projet
```bash
git clone https://github.com/ssabiridrissi-rgb/gestion-location-voitures.git
cd gestion-location-voitures
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Configurer la clé API Groq
Créer un compte gratuit sur [console.groq.com](https://console.groq.com) → générer une clé API, puis :

```bash
# Linux / macOS
export GROQ_API_KEY="votre_clé_ici"

# Windows (PowerShell)
$env:GROQ_API_KEY="votre_clé_ici"

# Ou créer un fichier .env
echo "GROQ_API_KEY=votre_clé_ici" > .env
```

### 4. Lancer l'application
```bash
python app.py
```

Ouvrir [http://localhost:5000](http://localhost:5000)

---

## 🛠️ Technologies

| Technologie | Version | Rôle |
|---|---|---|
| Python | 3.10+ | Langage principal |
| Flask | 3.0 | Framework web |
| Groq API | llama-3.3-70b | Assistant IA |
| HTML / CSS / JS | — | Interface utilisateur |
| SonarCloud | — | Analyse qualité du code |

---

## 🔍 Qualité du code — SonarCloud

Analyse effectuée sur **469 lignes de code** :

| Métrique | Résultat |
|---|---|
| Quality Gate | ✅ Passed |
| Issues corrigées | 2 (HTTP methods Flask + contraste CSS) |
| Duplications | 0.0% |
| Couverture | — |

Issues corrigées :
- `app.py L22` — Ajout de `methods=['GET']` explicite sur la route Flask
- `style.css L82` — Correction du ratio de contraste texte/fond (WCAG AA 4.7:1)

---

## 🌿 Workflow Git

```
main
└── develop
    ├── feature/crud-voitures      → CRUD catalogue (Taha)
    ├── feature/ai-suggestion      → Chatbot Groq IA (Chraibi)
    ├── feature/design-pattern     → Strategy Pattern (Marwane)
    ├── feature/quality            → SonarCloud config (Marwane)
    └── hotfix/fix-readme-typo     → Correction README (Saad)

Tag : v1.0
```

---

## 👥 Équipe

| Rôle | Nom | Responsabilités |
|---|---|---|
| Workflow & Release Manager | Saad Sabir Idrissi | Git, branches, PRs, hotfix, tag v1.0 |
| Feature Lead — MVP | Taha Mohammed Adib | CRUD voitures, interface admin |
| AI Lead | Mohamed Chraibi | Chatbot Alex, intégration Groq API |
| Quality & Refactoring Lead | Marwane Ouahid | Design Pattern Strategy, SonarCloud |
| Business & Documentation Lead | Mohamed Bouhassoune | README, offre commerciale, présentation |

---

## 📄 Licence

Projet académique — Module Maintenance Logicielle  
Université Mundiapolis — École d'Ingénierie — 2025/2026
