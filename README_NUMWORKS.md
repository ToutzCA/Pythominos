# Pythominos pour NumWorks

Version adaptée du jeu Pythominos pour la calculatrice NumWorks.

## Présentation

Pythominos est un jeu de puzzle inspiré du Katamino, adapté pour fonctionner sur la calculatrice NumWorks. Le but est de remplir complètement un plateau avec des pièces de formes différentes.

## Caractéristiques de cette version

### Adaptations pour NumWorks

- ✅ **Graphiques simplifiés** : Utilise le module `kandinsky` pour l'affichage
- ✅ **Interface optimisée** : Adapté pour l'écran 320x222 pixels
- ✅ **Contrôles au clavier** : Utilise les touches de la calculatrice NumWorks
- ✅ **Pas d'audio** : Les sons et la musique sont supprimés (limitation NumWorks)
- ✅ **Pas de sauvegarde fichier** : Jeu en mémoire uniquement
- ✅ **Optimisé pour la mémoire** : Code simplifié pour respecter les limites

### Dimensions du jeu

- Taille du plateau : 12 colonnes × 5 lignes
- Taille des cellules : 20×20 pixels
- 12 pièces différentes disponibles
- Chaque pièce a une couleur unique

## Installation

### Méthode 1 : Via l'interface web NumWorks

1. Allez sur [my.numworks.com](https://my.numworks.com/)
2. Connectez votre calculatrice NumWorks via USB
3. Cliquez sur "Ajouter un script Python"
4. Copiez le contenu de `pythominos_numworks.py`
5. Nommez le script "pythominos"
6. Transférez-le sur votre calculatrice

### Méthode 2 : Via le simulateur

1. Utilisez le simulateur NumWorks en ligne : [www.numworks.com/simulator](https://www.numworks.com/simulator/)
2. Ajoutez le script Python `pythominos_numworks.py`
3. Exécutez le script

## Commandes

### Touches de jeu

- **Flèches directionnelles** : Déplacer le curseur sur le plateau
- **OK** : Placer ou retirer la pièce sélectionnée
- **EXE** : Faire pivoter la pièce (rotation 90°)
- **SHIFT** : Miroir horizontal de la pièce
- **BACK** : Retirer la pièce du plateau

### Objectif

Remplir complètement le plateau avec les pièces disponibles. Quand toutes les cases sont remplies, vous gagnez !

## Différences avec la version originale

La version NumWorks est une adaptation simplifiée du jeu original `Pythominos.py` :

### Fonctionnalités retirées

- ❌ Musique et effets sonores
- ❌ Menu principal animé avec cascade de pièces
- ❌ Mode Grand Chelem
- ❌ Sauvegarde sur fichier
- ❌ Écrans de crédits et paramètres avancés
- ❌ Animations complexes
- ❌ Support souris (interface tactile)

### Fonctionnalités conservées

- ✅ Mécanique de jeu principale (placement de pièces)
- ✅ Rotation et symétrie des pièces
- ✅ Détection de collision
- ✅ Détection de victoire
- ✅ 12 pièces différentes
- ✅ Couleurs distinctes pour chaque pièce

## Limitations techniques NumWorks

La calculatrice NumWorks a les contraintes suivantes :

1. **Mémoire limitée** : ~32 KB pour les scripts Python
2. **Pas de système de fichiers** : Impossible de sauvegarder des parties
3. **Pas d'audio** : Aucun support pour les sons
4. **Écran fixe** : 320×222 pixels (couleur)
5. **Clavier physique** : Interface limitée aux touches de la calculatrice
6. **Python MicroPython** : Sous-ensemble de Python 3 avec limitations

## Architecture du code

Le code est organisé en classes principales :

```
pythominos_numworks.py
│
├── Piece         # Représente une pièce de jeu
├── Board         # Représente le plateau de jeu
└── Game          # Contrôleur principal du jeu
    ├── update()  # Gestion de la logique
    ├── draw()    # Affichage graphique
    └── run()     # Boucle principale
```

## Développement et tests

### Test sur PC (mode simulation)

Le code inclut un mode simulation qui permet de tester la structure sans NumWorks :

```python
python pythominos_numworks.py
```

En mode simulation, les modules NumWorks sont simulés et le code affiche des messages de debug au lieu de dessiner à l'écran.

### Variables importantes

```python
SCREEN_WIDTH = 320      # Largeur écran NumWorks
SCREEN_HEIGHT = 222     # Hauteur écran NumWorks
CELL_SIZE = 20          # Taille d'une cellule
BOARD_WIDTH = 12        # Largeur du plateau
BOARD_HEIGHT = 5        # Hauteur du plateau
```

## Améliorations futures possibles

- [ ] Ajouter plusieurs niveaux de difficulté (plateaux de différentes tailles)
- [ ] Implémenter un compteur de mouvements
- [ ] Ajouter un chronomètre
- [ ] Créer un mode tutoriel
- [ ] Optimiser davantage pour la mémoire
- [ ] Ajouter des défis prédéfinis

## Crédits

### Version originale Pythominos

**Code :**
- Camille TOUTZEVITCH
- Achille LAFOURCADE
- Leandre MONCORGE
- Gabriel ESCHENBRENNER

**Musique et effets sonores :**
- Adrien TOUTZEVITCH

### Adaptation NumWorks

Adaptation réalisée pour permettre au jeu de fonctionner sur la calculatrice NumWorks avec ses contraintes spécifiques.

## Licence

Projet scolaire - Voir le dépôt original pour plus d'informations.

## Ressources

- [Documentation NumWorks Python](https://www.numworks.com/resources/engineering/software/python/)
- [Module Kandinsky](https://www.numworks.com/resources/engineering/software/python/kandinsky/)
- [Module Ion](https://www.numworks.com/resources/engineering/software/python/ion/)
- [Simulateur NumWorks](https://www.numworks.com/simulator/)
