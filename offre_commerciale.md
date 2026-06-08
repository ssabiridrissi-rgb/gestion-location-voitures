# Offre Commerciale — AutoLoc

**Référence :** OC-AutoLoc-2026  
**Date :** Juin 2026  
**Préparé par :** Équipe AutoLoc — Mohamed Bouhassoune  
**Client :** AgenceAuto Maroc

---

## 1. Présentation du client

**Client :** AgenceAuto Maroc  
**Secteur :** Transport et location de véhicules  
**Taille :** PME — 5 à 20 employés, flotte de 15 à 50 véhicules  
**Localisation :** Casablanca, Maroc  
**Besoin identifié suite à :** Audit opérationnel révélant une gestion manuelle inefficace du catalogue et des réservations, entraînant des pertes de clients et une mauvaise visibilité sur la flotte disponible.

---

## 2. Problème identifié

L'agence fait face à plusieurs difficultés opérationnelles majeures :

- **Gestion manuelle du catalogue** : les voitures sont listées sur des fichiers Excel non partagés, sources d'erreurs et de doublons
- **Absence d'outil de recommandation** : les agents perdent du temps à conseiller manuellement chaque client selon ses besoins
- **Aucune visibilité en temps réel** : pas de compteur de disponibilité ni de suivi des réservations
- **Expérience client médiocre** : temps d'attente élevé, absence d'interface en ligne pour les clients

Ces problèmes entraînent une perte estimée de 20 à 30% de clients potentiels faute de réactivité.

---

## 3. Solution proposée

**AutoLoc** est une application web légère, accessible via navigateur, sans installation client. Elle centralise la gestion de la flotte et intègre un **assistant IA (Alex)** qui guide automatiquement chaque client vers la voiture idéale en moins de 2 minutes.

**Valeur ajoutée clé :** l'assistant IA remplace une partie du travail de conseil des agents, libérant du temps pour des tâches à plus forte valeur ajoutée.

---

## 4. Fonctionnalités clés

| Fonctionnalité | Description | Bénéfice |
|---|---|---|
| Catalogue voitures | Affichage filtré par type, prix, transmission | Visibilité immédiate de la flotte |
| CRUD Admin | Ajouter, modifier, supprimer des voitures | Gestion en temps réel |
| Réservations | Suivi des réservations par modèle | Évite les doubles réservations |
| Assistant IA Alex | Recommandation personnalisée en 5 questions | Réduction du temps de conseil |
| Tableau de bord | Compteurs voitures/réservations en live | Pilotage opérationnel |

---

## 5. Technologies utilisées

| Technologie | Justification |
|---|---|
| Python / Flask | Léger, rapide à déployer, maintenu par une large communauté |
| Groq API (llama-3.3-70b) | IA gratuite, ultra-rapide, réponse en < 1 seconde |
| HTML / CSS / JavaScript | Interface responsive sans dépendance lourde |
| SonarCloud | Garantie de qualité et maintenabilité du code |

---

## 6. Planning simplifié

| Phase | Durée | Livrable |
|---|---|---|
| Phase 1 — Cadrage & Setup Git | 2 jours | Repo, branches, environnement |
| Phase 2 — Développement MVP CRUD | 4 jours | Catalogue + admin fonctionnels |
| Phase 3 — Intégration IA | 2 jours | Chatbot Alex opérationnel |
| Phase 4 — Qualité & Refactoring | 2 jours | SonarCloud, Strategy Pattern |
| Phase 5 — Documentation & Livraison | 2 jours | README, offre, présentation |
| **Total** | **~12 jours** | **Version v1.0 livrée** |

---

## 7. Estimation budgétaire *(simulation pédagogique)*

| Poste | Détail | Coût estimé |
|---|---|---|
| Développement backend Flask | 2 développeurs × 10j × 250 MAD/j | 5 000 MAD |
| Intégration IA Groq | 1 développeur × 4j × 300 MAD/j | 1 200 MAD |
| Refactoring & Qualité | 1 développeur × 4j × 280 MAD/j | 1 120 MAD |
| Documentation & Business | 1 personne × 6j × 200 MAD/j | 1 200 MAD |
| API Groq (usage) | Quota gratuit suffisant en production légère | 0 MAD |
| Hébergement VPS (1 an) | Serveur basique Railway ou Render | 1 200 MAD |
| **Total estimé** | | **9 720 MAD** |

> *Budget prévisionnel à titre indicatif. Une version pilote peut être déployée gratuitement sur Railway ou Render.*

---

## 8. Conclusion

AutoLoc répond directement aux besoins d'une agence de location moderne : rapidité, visibilité et expérience client améliorée. L'intégration de l'IA Groq apporte une valeur différenciante immédiate sans coût supplémentaire.

L'architecture modulaire basée sur le **Design Pattern Strategy** garantit que le fournisseur IA peut être remplacé ou étendu sans refonte du projet, assurant une pérennité technique sur le long terme.

**Nous proposons une mise en production d'un pilote opérationnel sous 2 semaines, avec démonstration live et formation des utilisateurs incluse.**

---

*Document préparé dans le cadre du module Maintenance Logicielle*  
*Université Mundiapolis — École d'Ingénierie — 2025/2026*  
*Équipe AutoLoc : Saad Sabir Idrissi, Taha Mohammed Adib, Mohamed Chraibi, Marwane Ouahid, Mohamed Bouhassoune*
