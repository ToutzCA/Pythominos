# Guide d'Installation - Pythominos pour NumWorks

Ce guide vous explique comment installer et utiliser Pythominos sur votre calculatrice NumWorks.

## Prérequis

- Une calculatrice NumWorks (n0100 ou plus récent)
- Un câble USB pour connecter la calculatrice à votre ordinateur
- Un navigateur web moderne (Chrome, Firefox, Safari, Edge)
- OU accès au simulateur NumWorks en ligne

## Méthode 1 : Installation sur une vraie calculatrice NumWorks

### Étape 1 : Préparer le fichier

1. Téléchargez le fichier `pythominos_numworks.py` depuis ce dépôt
2. Ouvrez le fichier dans un éditeur de texte
3. Copiez tout le contenu du fichier (Ctrl+A puis Ctrl+C)

### Étape 2 : Accéder à l'interface NumWorks

1. Ouvrez votre navigateur web
2. Allez sur [my.numworks.com](https://my.numworks.com/)
3. Connectez votre calculatrice NumWorks à votre ordinateur via USB
4. La calculatrice devrait être détectée automatiquement

> **Note :** Si la calculatrice n'est pas détectée, assurez-vous :
> - Que le câble USB fonctionne correctement
> - Que votre navigateur a l'autorisation d'accéder aux périphériques USB
> - Que la calculatrice est allumée

### Étape 3 : Ajouter le script Python

1. Sur my.numworks.com, cliquez sur l'onglet **"Python"**
2. Cliquez sur le bouton **"Ajouter un script"** (icône +)
3. Donnez un nom au script : `pythominos` (ou autre nom de votre choix)
4. Collez le code copié à l'étape 1 dans l'éditeur
5. Cliquez sur **"Enregistrer"**

### Étape 4 : Transférer sur la calculatrice

1. Cliquez sur le bouton **"Installer"** ou **"Envoyer à la calculatrice"**
2. Attendez que le transfert se termine (quelques secondes)
3. Un message de confirmation devrait apparaître

### Étape 5 : Lancer le jeu sur la calculatrice

1. Débranchez votre calculatrice
2. Sur la calculatrice, appuyez sur le bouton **Home**
3. Naviguez jusqu'à l'application **Python**
4. Sélectionnez le script `pythominos`
5. Appuyez sur **OK** pour lancer le jeu
6. Le jeu démarre !

## Méthode 2 : Test sur le simulateur NumWorks

Si vous n'avez pas de calculatrice NumWorks, vous pouvez tester le jeu sur le simulateur en ligne.

### Étape 1 : Accéder au simulateur

1. Ouvrez votre navigateur web
2. Allez sur [www.numworks.com/simulator](https://www.numworks.com/simulator/)
3. Le simulateur se charge automatiquement

### Étape 2 : Ajouter le script

1. Cliquez sur l'icône Python dans le simulateur
2. Cliquez sur **"Ajouter un script"**
3. Copiez-collez le contenu de `pythominos_numworks.py`
4. Nommez le script `pythominos`
5. Enregistrez

### Étape 3 : Exécuter le jeu

1. Dans le simulateur, sélectionnez le script `pythominos`
2. Cliquez sur **"Exécuter"** (bouton play) ou appuyez sur EXE
3. Le jeu démarre dans le simulateur
4. Utilisez la souris pour cliquer sur les touches du simulateur

## Comment jouer

### Objectif

Remplir complètement le plateau de jeu (12×5 cases) avec les pièces disponibles.

### Commandes

| Touche | Action |
|--------|--------|
| **Flèches** (↑ ↓ ← →) | Déplacer le curseur sur le plateau |
| **OK** | Placer la pièce à la position du curseur / Retirer une pièce placée |
| **EXE** | Faire pivoter la pièce courante (rotation 90°) |
| **SHIFT** | Miroir horizontal de la pièce courante |
| **BACK** | Retirer la pièce du plateau |

### Déroulement du jeu

1. **Sélection de la pièce** : Au démarrage, la première pièce est sélectionnée automatiquement
2. **Déplacement du curseur** : Utilisez les flèches pour positionner le curseur
3. **Ajustement de la pièce** : 
   - Appuyez sur **EXE** pour faire pivoter la pièce
   - Appuyez sur **SHIFT** pour inverser la pièce horizontalement
4. **Placement** : Appuyez sur **OK** pour placer la pièce
   - Un aperçu de la pièce s'affiche sous le curseur
   - La pièce ne peut être placée que sur des cases vides
5. **Correction** : Si vous voulez retirer une pièce, appuyez sur **OK** ou **BACK** quand elle est sélectionnée
6. **Victoire** : Quand le plateau est complètement rempli, un message de victoire s'affiche !

### Astuces

- 💡 Essayez différentes orientations de pièces avant de les placer
- 💡 Commencez par les coins et les bords
- 💡 Les pièces peuvent être tournées et inversées plusieurs fois
- 💡 Si vous êtes bloqué, retirez quelques pièces et réessayez

## Dépannage

### Le script ne se lance pas sur la calculatrice

**Problème :** Le script plante ou ne démarre pas

**Solutions :**
- Vérifiez que vous avez copié **tout** le contenu du fichier `pythominos_numworks.py`
- Assurez-vous que le firmware de votre NumWorks est à jour (version 16.0.0 ou plus)
- Vérifiez qu'il n'y a pas d'autres scripts Python utilisant beaucoup de mémoire
- Essayez de supprimer d'autres scripts Python pour libérer de la mémoire

### Erreur "Memory Error"

**Problème :** Message d'erreur mémoire insuffisante

**Solutions :**
- Supprimez d'autres scripts Python de la calculatrice
- Supprimez des applications non essentielles
- Réinitialisez la calculatrice (attention : cela efface tout !)

### Le jeu est trop lent

**Problème :** Le jeu réagit lentement aux touches

**Solutions :**
- C'est normal sur NumWorks, le processeur est limité
- Attendez un peu entre chaque action
- Le jeu est optimisé autant que possible pour NumWorks

### La calculatrice n'est pas détectée par my.numworks.com

**Problème :** Le site ne reconnaît pas la calculatrice

**Solutions :**
1. Essayez un autre câble USB
2. Essayez un autre port USB sur votre ordinateur
3. Redémarrez la calculatrice (bouton reset au dos)
4. Utilisez un autre navigateur (Chrome recommandé)
5. Vérifiez les permissions USB de votre navigateur
6. Sur Mac : vérifiez les autorisations système

### Impossible de placer une pièce

**Problème :** Le message "Cannot place here" s'affiche

**Solutions :**
- La position choisie est déjà occupée par une autre pièce
- La pièce dépasse du plateau
- Essayez une autre position ou rotation
- Vérifiez que toutes les cases de la pièce sont dans les limites du plateau

## Spécifications techniques

### Mémoire utilisée

- **Taille du script** : ~15 KB
- **Mémoire RAM** : ~20-25 KB pendant l'exécution
- **Compatible** avec NumWorks Epsilon 16.0.0+

### Performance

- **Framerate** : Variable selon NumWorks (~10-30 FPS)
- **Input lag** : Minimal (~50ms)
- **Temps de chargement** : <1 seconde

### Modules Python NumWorks utilisés

```python
from kandinsky import fill_rect, draw_string  # Graphiques
from ion import keydown, KEY_*                 # Contrôles clavier
```

## Mises à jour

Pour mettre à jour vers une nouvelle version :

1. Supprimez l'ancien script `pythominos` de la calculatrice
2. Téléchargez la nouvelle version depuis GitHub
3. Suivez à nouveau les étapes d'installation

## Support et contributions

- **Issues** : Signalez les bugs sur GitHub
- **Améliorations** : Proposez des features via Pull Requests
- **Questions** : Consultez le README principal

## Ressources utiles

### Documentation NumWorks

- [Documentation officielle NumWorks Python](https://www.numworks.com/resources/engineering/software/python/)
- [Module Kandinsky (graphiques)](https://www.numworks.com/resources/engineering/software/python/kandinsky/)
- [Module Ion (clavier)](https://www.numworks.com/resources/engineering/software/python/ion/)

### Communauté

- [Forum NumWorks](https://community.numworks.com/)
- [NumWorks Workshop](https://workshop.numworks.com/) - Scripts partagés

### Outils de développement

- [Simulateur NumWorks](https://www.numworks.com/simulator/)
- [My NumWorks](https://my.numworks.com/) - Interface de gestion

## Licence

Voir le fichier LICENSE du projet principal.

---

**Bon jeu ! 🎮**

Si vous rencontrez des problèmes, n'hésitez pas à ouvrir une issue sur GitHub.
