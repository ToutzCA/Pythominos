# Quick Reference - Pythominos NumWorks

## Installation en 3 étapes

### Sur calculatrice NumWorks
1. Allez sur [my.numworks.com](https://my.numworks.com/)
2. Copiez `pythominos_numworks.py`
3. Transférez sur votre calculatrice

### Sur simulateur
1. Allez sur [simulateur NumWorks](https://www.numworks.com/simulator/)
2. Copiez `pythominos_numworks.py`
3. Exécutez

## Commandes de jeu

| Touche | Action |
|--------|--------|
| ↑ ↓ ← → | Déplacer curseur |
| OK | Placer/Retirer pièce |
| EXE | Rotation 90° |
| SHIFT | Miroir horizontal |
| BACK | Retirer pièce |

## Fichiers du projet

```
Pythominos/
├── Pythominos.py              # Version PC originale (Pyxel)
├── pythominos_numworks.py     # ⭐ Version NumWorks
├── sauvegarde.py              # Système de sauvegarde (PC uniquement)
├── README.md                  # Vue d'ensemble
├── README_NUMWORKS.md         # Doc NumWorks complète
├── INSTALLATION_NUMWORKS.md   # Guide d'installation
├── NUMWORKS_FEATURES.md       # Détails techniques
├── SUMMARY.md                 # Résumé développeur
└── QUICK_REFERENCE.md         # Ce fichier
```

## Code essentiel

### Créer un jeu
```python
game = Game()
game.run()  # Boucle principale
```

### Classes principales
```python
Piece(numero, pattern)   # Une pièce de jeu
  .rotate()              # Rotation 90°
  .mirror()              # Symétrie

Board(width, height)     # Le plateau
  .can_place(piece, r, c)  # Test placement
  .place_piece(piece, r, c) # Placer
  .is_full()               # Victoire?

Game()                   # Contrôleur
  .update()              # Logique
  .draw()                # Affichage
  .run()                 # Boucle
```

### Dimensions
```python
SCREEN_WIDTH = 320      # NumWorks
SCREEN_HEIGHT = 222
CELL_SIZE = 20
BOARD_WIDTH = 12
BOARD_HEIGHT = 5
```

## API NumWorks utilisée

### Graphiques (kandinsky)
```python
fill_rect(x, y, w, h, (r,g,b))
draw_string(text, x, y, color, bg)
```

### Clavier (ion)
```python
keydown(KEY_LEFT)    # True si enfoncée
KEY_UP, KEY_DOWN, KEY_RIGHT
KEY_OK, KEY_BACK, KEY_EXE, KEY_SHIFT
```

## Dépannage rapide

**Script ne démarre pas**
→ Vérifiez la syntaxe Python, copiez tout le fichier

**"Memory Error"**
→ Supprimez d'autres scripts Python

**Pas de pièce visible**
→ C'est normal, utilisez OK pour placer

**Impossible de placer**
→ Position occupée ou hors limites

## Liens utiles

- 📖 [Doc complète](README_NUMWORKS.md)
- 🔧 [Installation](INSTALLATION_NUMWORKS.md)
- 💻 [Détails techniques](NUMWORKS_FEATURES.md)
- 📊 [Résumé](SUMMARY.md)
- 🌐 [My NumWorks](https://my.numworks.com/)
- 🎮 [Simulateur](https://www.numworks.com/simulator/)

## Tests rapides

### Test syntaxe
```bash
python3 -m py_compile pythominos_numworks.py
```

### Test simulation
```bash
python3 pythominos_numworks.py
```

### Test logique
```python
from pythominos_numworks import Piece, Board, Game
board = Board(12, 5)
piece = Piece(1, [[1],[1],[1],[1],[1]])
assert board.can_place(piece, 0, 0)
assert board.place_piece(piece, 0, 0)
print("✅ Tests passés")
```

## Spécifications

| Spec | Valeur |
|------|--------|
| Taille fichier | ~15 KB |
| RAM utilisée | ~25 KB |
| Écran | 320×222 px |
| Plateau | 12×5 cases |
| Pièces | 12 uniques |
| Cellule | 20×20 px |
| FPS cible | 10-20 |

## Limitations

❌ Pas d'audio  
❌ Pas de sauvegarde  
❌ Une seule taille de plateau  
❌ Pas de menu pause  
❌ Pas d'animations  

✅ Tout le gameplay essentiel fonctionne!

## Contribution

1. Fork le repo
2. Branch: `git checkout -b amelioration`
3. Modifiez `pythominos_numworks.py`
4. Testez sur simulateur
5. Commit & Push
6. Pull Request

## Support

- 🐛 Bugs → GitHub Issues
- 💡 Idées → GitHub Discussions
- 📧 Questions → Voir README

---

**Version**: 1.0  
**Statut**: ✅ Production Ready  
**Licence**: Voir LICENSE  
**Auteurs**: Voir CREDITS
