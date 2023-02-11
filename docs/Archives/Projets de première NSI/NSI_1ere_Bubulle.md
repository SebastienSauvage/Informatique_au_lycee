---
title: "Projet : Bubulle"
author: [Sébastien SAUVAGE]
date: "11/01/2023"
keywords: [NSI, première, projet, pyxel, bubulle]
discipline: NSI
---
\huge \textbf{Projet}\normalsize  

\ 

\Large \textbf{Animation interactive Bubulle}\normalsize  

# Introduction et version 0
L'objectif de ce projet est de créer une animation graphique comportant des disques, appelés bulles.  

Les bulles se déplacent à des vitesses variables. Lorsqu'elles se rencontrent, la plus grosse absorbe la plus petite et sa vitesse est modifiée.  

Enfin, lorsque l'utilisateur clique sur l'une des bulles, celle-ci "explose" en plusieurs plus petites bulles.  

Pour débuter ce projet, le fichier `NSI_1ere_Pyxel_Bubulles_Squelette.py` est mis à disposition.  

Ce fichier comporte le squelette du programme.  

Chaque bulle sera représentée par un tableau contenant son rayon, les coordonnées de son centre, les valeurs de déplacement selon des deux axes et enfin, la couleur de la bulle.  

Cinq constantes sont utilisées :  

- `BULLE_VITESSE_MAX` est le déplacement maximal sur un des axes que peut posséder une bulle.
- `NOMBRES_BULLES_DEBUT` est le nombre de bulle en animation au lancement du programme.
- `NB_BULLES_EXPLOSION` est le nombre de "petites" bulles qui apparaissent à la place de la bulle qui explose.
- `FENETRE_WIDTH` et `FENETRE_HEIGHT` sont respectivement, la largeur et la hauteur de la fenêtre de l'animation.

### A FAIRE
Ecrire les documentations des fonctions `cree_bulle`, `get_rayon`, `set_rayon`, `get_couleur`, `get_abscisse`, `set_abscisse`, `get_ordonnee`, `set_ordonnee`, `get_depl_abscisse`, `set_depl_abscisse`, `get_depl_ordonnee` et `set_depl_ordonnee`.  

Exemple d'utilisation :  

```python
>>> b = cree_bulle()
>>> get_rayon(b)
9.50621678401362
>>> b = set_rayon(b, 2)
>>> get_rayon(b)
2
>>> get_abscisse(b)
238.4212911712092
>>> b = set_abscisse(b, 154)
>>> get_abscisse(b)
154
>>> b
[2, [154, 118.28885858784678], [-0.856717356219812, 3.5268185623351127], 12]
```

### A FAIRE
Ecrire les documentations des fonctions `update`, `draw`.  

Sauvegarder le fichier sous la forme `NOM1_Prenom1_NOM2_Prenom2_Bubulle0.py`  

Pour la suite du projet, penser à écrire chaque documentation des fonctions demandées **avant** d'en rédiger le code.  

# Version 1 : création d'une bulle
## Créer une bulle
Compléter la fonction `cree_bulle`.  

- `rayon` est une variable de type `float` contenant le rayon de la bulle. Le rayon est choisi aléatoirement entre 3 et 10.
- `position` de type `list` comporte les coordonnées du centre de la bulle. Les deux valeurs de type `float` sont prises aléatoirement de manière à ce que la bulle ne dépasse pas de la fenêtre.
- `deplacement` de type `list` comporte les déplacements selon des deux axes. Les deux valeurs de type `float` sont choisies aléatoirement entre la vitesse maximale et son opposée.
- `couleur` de type `int` est un nombre entier compris entre 1 et 15, et correspond au code couleur de la bulle.  

Sauvegarder le fichier sous la forme `NOM1_Prenom1_NOM2_Prenom2_Bubulle1_1.py`

## Set et get d'une bulle
Compléter les fonctions `get_...` et `set_...` permettant de renvoyer respectivement l'élément correspondant, et une bulle dont l'élément a été modifié.  

Sauvegarder le fichier sous la forme `NOM1_Prenom1_NOM2_Prenom2_Bubulle1_2.py`, etc. au fur et à mesure des fonctions codées.  

# Version 2 : affichage des bulles
Maintenant on peut créer des bulles.  Il s'agit d'en afficher quelques une ...  

### A FAIRE
A la fin du code, créer une variable `liste_bulles` de type `list` contenant des "bulles" (utiliser la fonction `cree_bulle`). Leur nombre est stocké dans la constante `NUM_INITIAL_BUBBLES`.  

Sauvegarder le fichier sous la forme `NOM1_Prenom1_NOM2_Prenom2_Bubulle2_1.py`  

### A FAIRE
Compléter la méthode `draw` afin de tracer un disque de couleur pour chacune des bulles de la variable créée juste avant.  

Pour tracer un disque de centre (x, y), de rayon R et de couleur c, on utilise l'instruction `pyxel.circ(x, y, R, c)`

Sauvegarder le fichier sous la forme `NOM1_Prenom1_NOM2_Prenom2_Bubulle2_2.py`  

### A FAIRE
A la dernière ligne de votre programme, ajouter la ligne :  

```python
pyxel.run(update, draw)
```

Sauvegarder le fichier sous la forme `NOM1_Prenom1_NOM2_Prenom2_Bubulle2_3.py`  

Si tout est bien effectué, l'affichage des bulles (statiques) fonctionne.  

# Version 3 : déplacement des bulles
## Déplacement de la bulle
### A FAIRE
Afin de modéliser le déplacement de la bulle, écrire le code de la fonction nommée `deplace` permettant à la bulle de se déplacer. Le déplacement consiste à ajouter aux coordonnées du centre de la bulle les valeurs du couple de déplacement et de définir cette somme comme nouvelles coordonnées du centre de la bulle.  

Cette fonction renvoie le paramètre avec les coordonnées de son centre modifiées.  

Sauvegarder le fichier sous la forme `NOM1_Prenom1_NOM2_Prenom2_Bubulle3_1.py`

### A FAIRE
Compléter la fonction `update` afin de déplacer les bulles. Cette fonction utilisera la fonction écrite précédemment.  

Sauvegarder le fichier sous la forme `NOM1_Prenom1_NOM2_Prenom2_Bubulle3_2.py`

### A FAIRE
Compléter la fonction `deplace` afin que les bulles ne sortent pas de la fenêtre.  

Dans le cas contraire, le déplacement selon l'un des axes doit changer de signe pour modéliser un "rebond" de la bulle sur le bord de la fenêtre.  

Sauvegarder le fichier sous la forme `NOM1_Prenom1_NOM2_Prenom2_Bubulle3_3.py`

# Version 4 : collisions de bulles
Pour que deux bulles entrent en collision, il faut et suffit que la distance entre leurs centres soit inférieure à la somme de leurs rayons.  

### A FAIRE
Ajouter une fonction `collision2bulles` qui renvoie `True` ou `False` selon si les deux bulles passées en paramètre entrent en collision.  

Sauvegarder le fichier sous la forme `NOM1_Prenom1_NOM2_Prenom2_Bubulle4_1.py`

### A FAIRE
Ecrire une méthode `collisions` afin de traiter l'ensemble des collisions possibles entre toutes les bulles.  

Cette fonction renvoie la liste des bulles, passée en paramètre, mise à jour.  

Lorsque deux bulles entrent en collision, elles disparaissent et laissent place à une bulle :

- de rayon la racine carrée de la somme des carrés deux anciens rayons ($r_{nouv} = \sqrt{r1^2 + r2^2}$)
- dont le centre est un point entre les deux anciens centres de bulles ($x_{nouv} = \sqrt{(x1 \times r1 + x2 \times r2) / (r1 + r2)}$, de même pour $y$)
- dont la couleur est aléatoire.  

Sauvegarder le fichier sous la forme `NOM1_Prenom1_NOM2_Prenom2_Bubulle4_2.py`

# Version 5 : cliquer sur une bulle
### A FAIRE
Ecrire une fonction `explosion` qui vérifie si on a cliqué sur une bulle et qui l'"explose" dans ce cas. Le nombre de bulles créées est contenu dans la constante `NB_BULLES_EXPLOSION`.  

Cette fonction renvoie la liste des bulles modifiées en conséquence.  

Sauvegarder le fichier sous la forme `NOM1_Prenom1_NOM2_Prenom2_Bubulle5.py`

# Version 6 et ultérieures : améliorations de l'animation
Laisser libre court à votre imagination pour améliorer cette animation : score affiché contenant le nombre maximum de bulles obtenues, affichage d'image au lieu de disque, etc.  