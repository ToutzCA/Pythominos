# Fonctionnalités de la version NumWorks

## Vue d'ensemble technique

La version NumWorks de Pythominos est une adaptation complète du jeu original, optimisée pour les contraintes matérielles de la calculatrice NumWorks.

## Contraintes NumWorks respectées

### Matériel
- ✅ **Écran** : 320×222 pixels, couleur
- ✅ **Mémoire RAM** : ~32 KB pour les scripts Python
- ✅ **Processeur** : ARM Cortex-M7 à 216 MHz
- ✅ **Stockage** : Limité pour les scripts Python

### Logiciel
- ✅ **Python** : MicroPython (sous-ensemble de Python 3)
- ✅ **Pas de fichiers** : Pas de système de fichiers accessible
- ✅ **Pas d'audio** : Aucune API audio disponible
- ✅ **Modules disponibles** : kandinsky, ion, math, random

## Architecture simplifiée

### Structure du code

```
pythominos_numworks.py (une seule fichier ~15 KB)
│
├── Constants (couleurs, dimensions)
├── Piece patterns (12 pièces prédéfinies)
│
├── Class Piece
│   ├── __init__(numero, pattern)
│   ├── rotate() - Rotation 90°
│   └── mirror() - Symétrie horizontale
│
├── Class Board
│   ├── __init__(width, height)
│   ├── can_place() - Test de collision
│   ├── place_piece() - Placement
│   ├── remove_piece() - Retrait
│   └── is_full() - Test de victoire
│
├── Class Game
│   ├── __init__()
│   ├── update() - Logique du jeu
│   ├── draw() - Affichage
│   └── run() - Boucle principale
│
└── main() - Point d'entrée
```

### Optimisations mémoire

1. **Pas de ressources externes** : Tout est dans un seul fichier
2. **Structures de données simples** : Listes et tuples basiques
3. **Pas de caching** : Recalcul à la volée
4. **Couleurs en dur** : Pas de palettes dynamiques

## Comparaison des versions

| Fonctionnalité | Version Pyxel | Version NumWorks | Raison |
|----------------|---------------|------------------|---------|
| **Écran** | 384×320 (scalable) | 320×222 (fixe) | Contrainte matérielle |
| **Taille cellule** | 32×32 pixels | 20×20 pixels | Optimisation espace |
| **Audio** | ✅ Musique + Sons | ❌ Aucun | NumWorks n'a pas d'API audio |
| **Animations** | ✅ Cascade de pièces | ❌ Aucune | Économie mémoire/CPU |
| **Menu principal** | ✅ Complet | ❌ Direct au jeu | Simplification |
| **Grand Chelem** | ✅ 12 niveaux | ❌ Non implémenté | Simplification |
| **Mode Libre** | ✅ Tailles variables | ❌ 12×5 fixe | Simplification |
| **Sauvegarde** | ✅ Fichier JSON | ❌ Non disponible | Pas de filesystem |
| **Sélection pièces** | ✅ Interface graphique | ✅ Simplifié | Adaptation écran |
| **Contrôles souris** | ✅ Drag & drop | ❌ Clavier uniquement | Pas de souris |
| **Crédits** | ✅ Écran dédié | ℹ️ Dans README | Économie espace |
| **Paramètres** | ✅ Menu in-game | ❌ Non nécessaire | Pas de son à désactiver |

## Gameplay adapté

### Différences de gameplay

**Version Pyxel (originale) :**
- Sélection interactive des pièces avec souris
- Drag & drop pour placer les pièces
- Menu rapide avec sauvegarde
- Effets visuels et sonores

**Version NumWorks :**
- Navigation au curseur uniquement
- Placement avec touche OK
- Pas de sauvegarde
- Feedback visuel minimal

### Flux de jeu simplifié

```
1. Démarrage du jeu
   ↓
2. Plateau 12×5 avec 4 pièces disponibles
   ↓
3. Sélection pièce + Déplacement curseur
   ↓
4. Rotation/Miroir (optionnel)
   ↓
5. Placement avec OK
   ↓
6. Répéter 3-5 jusqu'à victoire
   ↓
7. Écran de victoire
   ↓
8. OK pour recommencer
```

## API NumWorks utilisée

### Module Kandinsky (graphiques)

```python
# Remplir un rectangle avec une couleur
fill_rect(x, y, width, height, color)
# color = tuple RGB (R, G, B) où 0 ≤ R,G,B ≤ 255

# Dessiner du texte
draw_string(text, x, y, text_color, bg_color)
# Couleurs = tuples RGB
```

**Limitations :**
- Pas de sprites ou textures
- Pas de transformations (rotation d'images)
- Pas de transparence (sauf background de texte)
- Police de caractères fixe

### Module Ion (clavier)

```python
# Tester si une touche est enfoncée
keydown(KEY_*)

# Touches disponibles :
KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN  # Flèches
KEY_OK                                   # Bouton OK (rond)
KEY_BACK                                 # Bouton retour
KEY_EXE                                  # Bouton EXE
KEY_SHIFT                                # Touche Shift
```

**Limitations :**
- Pas de gestion d'événements (pas de callback)
- Pas de repeat automatique (à implémenter)
- Détection binaire (enfoncé/relâché)

## Détails d'implémentation

### Représentation du plateau

```python
# Plateau = liste 2D
board.grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Ligne 0
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Ligne 1
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Ligne 2
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Ligne 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Ligne 4
]
# 0 = vide, 1-12 = numéro de pièce
```

### Représentation des pièces

```python
# Pièce = liste de coordonnées relatives
piece.coords = [
    [0, 0],  # Cellule 1
    [1, 0],  # Cellule 2
    [2, 0],  # Cellule 3
    [3, 0],  # Cellule 4
    [4, 0],  # Cellule 5
]
# Exemple : pièce "I" (ligne verticale)
```

### Détection de collision

```python
def can_place(piece, row, col):
    for dr, dc in piece.coords:
        r, c = row + dr, col + dc
        # Hors limites ?
        if r < 0 or r >= height or c < 0 or c >= width:
            return False
        # Case occupée ?
        if board[r][c] != 0:
            return False
    return True
```

### Rotation de pièce

```python
# Rotation 90° sens horaire
# Transformation : (x, y) → (y, -x)
def rotate():
    # Normaliser à l'origine
    norm = [[x - min_x, y - min_y] for x, y in coords]
    # Appliquer rotation
    rot = [[y, -x] for x, y in norm]
    # Re-normaliser
    coords = [[x - min_x2, y - min_y2] for x, y in rot]
```

## Performances

### Mesures estimées

- **Temps de démarrage** : < 1 seconde
- **Framerate** : ~10-20 FPS (selon complexité affichage)
- **Input lag** : ~50-100ms
- **Mémoire utilisée** : ~20-25 KB RAM

### Optimisations appliquées

1. **Redessinage minimal** : Uniquement ce qui change
2. **Pas de double buffering** : Kandinsky gère automatiquement
3. **Calculs simples** : Éviter les opérations complexes
4. **Pas de récursion** : Boucles itératives uniquement

## Tests effectués

### Tests de syntaxe
```bash
python3 -m py_compile pythominos_numworks.py
✅ Aucune erreur de syntaxe
```

### Tests en mode simulation
```bash
python3 pythominos_numworks.py
✅ Démarre sans erreur
✅ Affiche les messages de simulation
✅ Pas de crash
```

### Tests requis sur NumWorks
- [ ] Test sur calculatrice réelle
- [ ] Test de tous les contrôles
- [ ] Test de performance
- [ ] Test de mémoire
- [ ] Test de victoire
- [ ] Test de cas limites

## Évolutions possibles

### Court terme (simples)
- [ ] Ajouter un compteur de mouvements
- [ ] Ajouter un chronomètre
- [ ] Améliorer les messages d'erreur
- [ ] Ajouter plus de pièces de départ

### Moyen terme (modérées)
- [ ] Implémenter plusieurs tailles de plateau
- [ ] Ajouter un mode "défi" avec solutions prédéfinies
- [ ] Implémenter un système de hints
- [ ] Optimiser davantage les performances

### Long terme (complexes)
- [ ] Mode 2 joueurs (tour par tour)
- [ ] Générateur de puzzles aléatoires
- [ ] Système de scoring
- [ ] Sauvegarde via encodage base64 à copier-coller

## Limitations connues

### Techniques
- ⚠️ Pas de sauvegarde permanente
- ⚠️ Impossible de quitter proprement (bouton Home)
- ⚠️ Pas de menu pause
- ⚠️ Pas de son/feedback audio
- ⚠️ Police de caractères fixe (pas de gras, italique)

### Gameplay
- ⚠️ Une seule taille de plateau
- ⚠️ Pas de mode tutoriel
- ⚠️ Pas de hints ou aide
- ⚠️ Pas de undo/redo

### Interface
- ⚠️ Pas de curseur visuel sophistiqué
- ⚠️ Pas d'animations
- ⚠️ Messages texte simples
- ⚠️ Pas de menu de paramètres

## Ressources

### Documentation NumWorks
- [Python API Reference](https://www.numworks.com/resources/engineering/software/python/)
- [Kandinsky Module](https://www.numworks.com/resources/engineering/software/python/kandinsky/)
- [Ion Module](https://www.numworks.com/resources/engineering/software/python/ion/)

### Exemples de code
- [NumWorks Workshop](https://workshop.numworks.com/)
- [Communauté NumWorks](https://community.numworks.com/)

### Outils
- [Simulateur en ligne](https://www.numworks.com/simulator/)
- [My NumWorks (gestion)](https://my.numworks.com/)

## Contribution

Pour améliorer cette version :

1. **Fork** le dépôt
2. Créez une branche : `git checkout -b amelioration-numworks`
3. Modifiez `pythominos_numworks.py`
4. Testez sur simulateur **ET** calculatrice réelle
5. Commitez : `git commit -m "Description"`
6. Push : `git push origin amelioration-numworks`
7. Créez une **Pull Request**

### Checklist pour PR
- [ ] Code testé sur simulateur
- [ ] Code testé sur vraie NumWorks
- [ ] Documentation mise à jour
- [ ] Pas de régression des fonctionnalités existantes
- [ ] Optimisation mémoire vérifiée
- [ ] Pas de syntaxe Python avancée (compatibilité MicroPython)

---

**Version NumWorks créée avec ❤️ pour la communauté NumWorks**
