# 🐤 Jeu de Canaries – Jeu de Dames avec IA

## 📌 Présentation  
**Jeu de Canaries** est une version simplifiée d’un **jeu de dames** se jouant sur une **grille 5x5**. Le jeu propose :  
- Un **mode Joueur contre Joueur**  
- Un **mode Joueur contre IA naïve**  

Chaque joueur déplace ses pions (`O` ou `X`) pour capturer ceux de l'adversaire ou le bloquer totalement.

---

## 🎯 Objectifs  
- Affichage dynamique d’une **grille interactive**  
- Sélection et **déplacement de pions** avec règles de validation  
- Deux types de déplacement :
  - **Simple** : vers une case vide adjacente  
  - **Saut** : par-dessus un pion adverse  
- Un mode **IA aléatoire** (choix naïf mais valide)  
- Détection de la **fin de partie** : plus de pions ou joueur bloqué

---

## 🛠️ Technologies Utilisées  
- **Python 3**  
- Bibliothèques standard : `random`, `math`, `sys`, `os`  
- Jeu entièrement en **ligne de commande (CLI)**  

---

## 🚀 Installation et Exécution

### 1. Cloner le projet
```bash
git clone https://github.com/votre-utilisateur/jeu-de-canaries.git
cd jeu-de-canaries
```
## 🚀 Lancer le jeu

Pour démarrer le jeu, exécutez simplement le fichier `jeu.py` :

```bash
python jeu.py
```
## 📜 Règles du Jeu

### 🎮 Modes disponibles
- **Mode 0** : Joueur contre Joueur  
- **Mode 1** : Joueur contre IA naïve  

### 🎯 But du jeu
- Capturer **tous les pions adverses**  
- **Ou** bloquer complètement l’adversaire pour l’empêcher de jouer  

### 🔄 Déroulement d’un tour
1. Le joueur actif sélectionne un pion à l’aide d’une **coordonnée** (ex : `2B`, `4E`, etc.)  
2. Il choisit le **type de déplacement** :
   - `0` : **Déplacement simple** (vers une case vide adjacente)  
   - `1` : **Saut** (par-dessus un pion adverse)  
3. Le jeu passe au joueur suivant (**ou à l’IA** si le mode choisi est le mode 1)
