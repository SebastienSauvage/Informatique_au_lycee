---
title: "Projet : Bubulle"
author: [Sébastien SAUVAGE]
date: "17/11/2022"
keywords: [NSI, terminale, projet, pyxel, bubulle]
discipline: NSI
---
\huge \textbf{Projet}\normalsize  

\ 

\Large \textbf{Animation interactive Bubulle}\normalsize  

# Introduction et version 0
L'objectif de ce projet est de créer une animation graphique comportant des disques, appelés bulles.  

Les bulles se déplacent à des vitesses variables. Lorsqu'elles se rencontrent, la plus grosse absorbe la plus petite et sa vitesse est modifiée.  

Enfin, lorsque l'utilisateur clique sur l'une des bulles, celle-ci "explose" en plusieurs plus petites bulles.  

Pour débuter ce projet, le fichier `NSI_Tale_Pyxel_Bubulles_Squelette.py` est mis à disposition.  

Ce fichier comporte le squelette du programme.  

Chaque bulle sera une instance de la classe `Bulle`. Et l'animation sera une instance de la classe `Bubullle`.  

Cinq constantes sont utilisées :  

- BULLE_VITESSE_MAX est le déplacement maximal sur un des axes que peut posséder une bulle.
- NOMBRES_BULLES_DEBUT est le nombre de bulle en animation au lancement du programme.
- NB_BULLES_EXPLOSION est le nombre de "petites" bulles qui apparaissent à la place de la bulle qui explose.
- FENETRE_WIDTH et FENETRE_HEIGHT sont respectivement, la largeur et la hauteur de la fenêtre de l'animation.

### A FAIRE
Ecrire les documentations des classes `Bulle` et `Bubulle` ainsi que du constructeur `__init__` et des quatre méthodes `quitter`, `affichage_consignes`, `update` et `draw`.  

Sauvegarder le fichier sous la forme `NOM1_Prenom1_NOM2_Prenom2_Bubulle0.py`

Pour la suite du projet, penser à écrire chaque documentation des méthodes demandées avant d'en rédiger le code.  

# Version 1 : création de l'objet `Bulle`
## Constructeur
Dans la classe `Bulle`, Remplacer l'instruction `pass` par la création de quatre attributs.  

- Le premier attribut est un objet de type `float` contenant le rayon de la bulle. Le rayon est choisi aléatoirement entre 3 et 10.
- Le deuxième attribut de type `list` comporte les coordonnées du centre de la bulle. Les deux valeurs de type `int` sont prises aléatoirement de manière à ce que la bulle ne dépasse pas de la fenêtre.
- Le troisième attribut de type `list` comporte les déplacements selon des deux axes. Les deux valeurs de type `int` sont choisies aléatoirement entre la vitesse maximale et son opposée.
- Le dernier attribut de type `int` est un nombre entier compris entre 1 et 15, et correspond au code couleur de la bulle.  

Sauvegarder le fichier sous la forme `NOM1_Prenom1_NOM2_Prenom2_Bubulle1.py`

# Version 2 : affichage des bulles
Maintenant on dispose d'une classe d'objets `Bulle`.  Il s'agit d'en afficher quelques une ...  

### A FAIRE
Ajouter un attribut de type `list` à la classe `Bubulle` contenant des objets de type `Bulle`.  

### A FAIRE
Compléter la méthode `draw` afin de tracer un disque de couleur pour chacune des bulles de l'attribut ajouté juste avant.  

Pour tracer un disque de centre (x, y), de rayon R et de couleur c, on utilise l'instruction `pyxel.circ(x, y, R, c)`

Sauvegarder le fichier sous la forme `NOM1_Prenom1_NOM2_Prenom2_Bubulle2.py`


# Version 3 : déplacement des bulles
## Déplacement de la bulle
### A FAIRE
Afin de modéliser le déplacement de la bulle, écrire une méthode de la classe `Bulle` nommée `deplacement` permettant à la bulle de se déplacer. Le déplacement consiste à ajouter les valeurs du troisième attributs aux valeurs du deuxième attribut et de modifier ce dernier avec les résultats obtenus.  

### A FAIRE
Compléter la méthode `update` de la classe `Bubulle` afin de déplacer les bulles. Cette méthode utilisera la méthode écrite à la question précédente.  

### A FAIRE
Compléter la méthode `deplacement` de la classe `Bulle` afin que la bulle ne sorte pas de la fenêtre.  

Dans le cas contraire, le déplacement selon l'un des axes doit changer de signe pour modéliser un "rebond" de la bulle sur le bord de la fenêtre.  

Sauvegarder le fichier sous la forme `NOM1_Prenom1_NOM2_Prenom2_Bubulle3.py`

# Version 4 : collisions de bulles
Pour que deux bulles entrent en collision, il faut et suffit que la distance entre leurs centres soit inférieure à la somme de leurs rayons.  

### A FAIRE
Ajouter une méthode `distance` à la classe `Bulle` permettant de renvoyer la distance entre deux bulles, l'une des deux étant passée en paramètre.  

### A FAIRE
Ecrire une méthode `collisions` dans la classe `Bubulle` afin de vérifier si deux bulles ne rentrent pas en collisions.  

Lorsque deux bulles entrent en collision, elles disparaissent et laisse place à une bulle :

- de rayon la racine carrée de la somme des carrés deux anciens rayons ($r_{nouv} = \sqrt{r1^2 + r2^2}$)
- dont le centre est un point entre les deux anciens centres de bulles ($x_{nouv} = \sqrt{(x1 \times r1 + x2 \times r2) / (r1 + r2)}$, de même pour $y$)
- dont la couleur est aléatoire.  

Sauvegarder le fichier sous la forme `NOM1_Prenom1_NOM2_Prenom2_Bubulle4.py`

# Version 5 : cliquer sur une bulle
### A FAIRE
Ecrire une méthode `explosion` qui vérifie si on a cliqué sur une bulle et qui l'"explose" dans ce cas. Le nombre de bulles créées est contenu dans la constante `NB_BULLES_EXPLOSION`.  

Modifier la méthode `update` afin d'appeler la méthode écrite précédemment.  

Sauvegarder le fichier sous la forme `NOM1_Prenom1_NOM2_Prenom2_Bubulle5.py`

# Version 6 et ultérieures : améliorations de l'animation
Laisser libre court à votre imagination pour améliorer cette animation : score affiché contenant le nombre maximum de bulles obtenues, affichage d'image au lieu de disque, etc.  