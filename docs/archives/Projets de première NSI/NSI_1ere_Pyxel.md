---
title: "Projet : Découverte de la bibliothèque Pyxel"
author: [Sébastien SAUVAGE]
date: "11/01/2023"
keywords: [NSI, première, projet, pyxel]
discipline: NSI
---
\huge \textbf{Projet}\normalsize  

\ 

\Large \textbf{Découverte de la bibliothèque Pyxel}\normalsize  

# DÉPLACER UN CARRÉ AVEC LES TOUCHES DE DIRECTIONS
Ouvrir le fichier `NSI_1ere_Pyxel_tutoriel1.py`.  

\  

Voici quelques explications à propos de ce fichier :  

\  

Après avoir importé le module `Pyxel` dans votre script Python, on crée des variables globales, ainsi que les fonctions nécessaires.  

Ce programme doit contenir les fonctions `draw` et `update`. La fonction `draw` crée et positionne les objets, alors que la fonction `update` met à jour les variables. Dès le début du programme, on spécifie d’abord la taille de la fenêtre avec la méthode `init` :  

```python
# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Nuit du c0de")
```

On lance l’application `Pyxel` avec la méthode `run` qui crée deux processus basés sur les fonctions `draw` et `update` :  

```Python
pyxel.run(update, draw)
```

Cette instruction doit être la dernière du programme. Pour déplacer un objet, on modifie ses coordonnées dans la fonction `vaisseau_deplacement`. Ici on les modifie à l’aide du clavier, en vérifiant si une touche est pressée (dans cet exemple, la touche droite et le touche gauche) :  

```Python
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 1
```

Il ne reste plus qu’à afficher le carré avec ses nouvelles coordonnées grâce à cette instruction dans la fonction `draw` :  

```Python
    # vaisseau (carre 8x8)
    pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)
```

### A vous de jouer
Modifier le script pour le déplacer le carré vers la gauche ainsi que selon l’axe des y.  

### A vous de jouer
Les attributs `pyxel.mouse_x` et `pyxel.mouse_y` permettent de connaitre la position actuelle de la souris. **Modifier** le script pour contrôler le carré avec la souris.  

# AJOUTER DES TIRS
Ouvrir le fichier `NSI_1ere_Pyxel_tutoriel2.py`.  

Voici quelques explications à propos de ce fichier :  

Un tir est caractérisé par ses coordonnées. Créer un tir signifie ajouter un couple de coordonnées dans la liste des tirs.  

```Python
    # btnr pour eviter les tirs multiples
    if pyxel.btnr(pyxel.KEY_SPACE):
        tirs_liste.append([x+4, y-4])
    return tirs_liste
```

Les coordonnées du tir sont déterminées à partir de celles du vaisseau, sachant que ces coordonnées correspondent au coin en haut à gauche.  

![Position_Tir](./NSI_1ere_Pyxel_tir_coor.png) \   

On déplace ensuite d’un pixel le tir jusqu’à ce qu’il sorte de l’écran. Il suffit alors de le retirer de la liste des tirs pour le supprimer.  

```Python
    for tir in tirs_liste:
        tir[1] -= 1
        if  tir[1]<-8:
            tirs_liste.remove(tir)
    return tirs_liste
```

# AJOUTER DES ENNEMIS
Ouvrir le fichier `NSI_1ere_Pyxel_tutoriel3.py`.  

\  

Voici quelques explications à propos de ce fichier :  

\  

Les images sont affichées à l’écran à raison de 30 images par secondes. L’attribut `frame_count` du module `pyxel` comptabilise le nombre d’images affichées depuis le début du jeu. Ainsi, pour créer un ennemi toute les secondes, on vérifie que le nombres d’images est un multiple de 30. La création des ennemis repose sur le même principe que celui des tirs, mais on utilise la fonction `randint` du module `random` pour les créer de façon aléatoire selon l’axe des x.  

```Python
    # un ennemi par seconde
    if (pyxel.frame_count % 30 == 0):
        ennemis_liste.append([random.randint(0, 120), 0])
    return ennemis_liste
```

# AJOUTER LES COLLISIONS
Ouvrir le fichier `NSI_1ere_Pyxel_tutoriel4.py`.  

\  

Voici quelques explications à propos de ce fichier :  

\  

Pour le cas de la collision d’un tir avec un ennemi, la détection est simple : la coordonnée en y doit être inférieure à `ye – 8`, et la coordonnée en x doit être comprise entre `xe` et `xe + 8`.  

![Colisions](./NSI_1ere_Pyxel_collision_tir.png) \   

Pour détecter une collision entre un ennemi et un vaisseau, il faut considérer deux cas de figure (en ne considérant pour l’instant que l’axe des x) :  

![Collisions](./NSI_1ere_Pyxel_collisions.png) \   

A partir de ces figures, on en déduit deux conditions : il faut le bord gauche du vaisseau soit inférieur à `xe + 8`, et le bord droit supérieur à `xe`.  

On applique le même raisonnement sur l’axe des y.  

Grâce aux collisions il est possible de mettre une condition d’échec avec un écran de fin de jeu. La méthode `text` permet d’afficher un texte aux coordonnées spécifiées (on peut également préciser le nombre de vie pendant la partie).  

```Python
    # si le vaisseau possede des vies le jeu continue
    if vies > 0:    
    ...
    # sinon: GAME OVER
    else:

        pyxel.text(50,64, 'GAME OVER', 7)
```

\newpage

# AJOUTER LES EXPLOSIONS LORS DES COLLISIONS
Ouvrir le fichier `NSI_1ere_Pyxel_tutoriel5.py`.  

\  

Voici quelques explications à propos de ce fichier :  

\  

Pour les explosions, on procède comme pour les tirs.  

Cependant, en plus des coordonnées, on ajoute un troisième paramètre. C’est ce paramètre qui permettra de créer des cercles dont le rayon et la couleur évolue.  

# AJOUTER DES IMAGES
Ouvrir le fichier `NSI_1ere_Pyxel_tutoriel6.py`.  

\  

Voici quelques explications à propos de ce fichier :  

\  

**Une tuile** (**tile** en anglais) est un élément graphique d'un jeu vidéo, constitué de petites images (en général) carrées disposées sur une grille.  

Une tuile peut représenter un sprite ou un élément de décor, avec lequel on peut interagir ou non. L'ensemble complet des tuiles disponibles pour une utilisation dans une zone de jeu est appelé un jeu de tuiles (ou tileset en anglais).  

L’éditeur Pyxel peut créer des images et des sons utilisables dans des applications Pyxel. (voir la documentation Pyxel)  

Lors de l'initialisation du jeu, il est nécessaire de charger en mémoire le fichier ressource (ici, il s'appelle `images.pyxres`).  

```Python
# chargement des images
pyxel.load("images.pyxres")
```

On peut ensuite placer l’image à l’écran, à la place du carré initial :  

```Python
        # vaisseau (carre 8x8)
        pyxel.blt(vaisseau_x, vaisseau_y, 0, 0, 0, 8, 8)
```

Si les dimensions de l’image sont indiquées comme négatives, la copie de l’image sera inversée horizontalement et/ou verticalement.  

Il est également possible de spécifier une couleur transparente, qui ne sera donc pas dessinée à l’écran. On a choisi ici la couleur noire (code : `0`), initialisé dans la constante `TRANSPARENT_COLOR`.

\   

\underline{{\textit{\textbf{Sources}}}}  

- Peio47 (2022, 16 novembre). \textit{Créer une application Pyxel}. La Nuit du C0de. [https://nuitducode.github.io/DOCUMENTATION/PYTHON/Tutoriel%20d%C3%A9taill%C3%A9%20-%20Terminale/Cr%C3%A9er%20une%20application%20Pyxel/](https://nuitducode.github.io/DOCUMENTATION/PYTHON/Tutoriel%20d%C3%A9taill%C3%A9%20-%20Terminale/Cr%C3%A9er%20une%20application%20Pyxel/)