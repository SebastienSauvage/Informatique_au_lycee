---
title: "Thème 1 - Chapitre 1 : Ecriture d'un nombre dans différentes bases"
author: [Sébastien SAUVAGE]
date: "03/09/2022"
keywords: [NSI, terminale, binaire]
discipline: NSI
---

\huge \textbf{Projet}\normalsize  

\ 

\Large \textbf{Jeu de Morpion}\normalsize  

\   

# Présentation générale
Les règles du jeu vous sont rappelées à la page suivante : [https://www.regles-de-jeux.com/regle-du-morpion/](https://www.regles-de-jeux.com/regle-du-morpion/)  

\   

**Contraintes**  

A l'aide du module `Pygame`, vous coderez en langage `Python`, le jeu du morpion avec les contraintes utilisateurs suivantes :  

- ce jeu se joue à 2 joueurs humains ;
- les joueurs cliquent avec le bouton gauche de la souris pour ajouter les symboles (X ou O) dans les cases ;
- Une fois la partie gagnée par un des deux joueurs, les 3 symboles alignés deviennent rouges ;
- Une fois la partie gagnée, il est impossible d'ajouter de nouveaux symboles (X et O) ;
- Un appui sur la touche "Entrée" doit permettre de reprendre le jeu à zéro.

Evidemment, votre code devra être le plus lisible possible. Vous penserez en particulier à écrire des fonctions, bien documentées, qui effectuent le minimum de choses (des tâches simples), à utiliser des noms de variables explicites, etc.  

\   

L'évaluation tiendra compte par ordre d'importance des éléments suivants :  

- le programme proposé, même incomplet, fonctionne sans erreur ;
- les fonctions sont correctement documentées (description de la fonction, des paramètres et de l'élément éventuellement retourné, préconditions et postconditions indiquées, effets de bord éventuels, exemples nombreux mais judicieusement choisis) ;
- le programme correspond aux contraintes demandées, précisées ci-dessus.

Vous utiliserez le fichier fourni qui est à compléter au fur et à mesure des paragraphes ci-dessous.  

# Le moteur de jeu
Pour commencer, le jeu se jouera **sans interface graphique**.  

\   

La grille sera modélisée par un tableau de tableaux à trois éléments.  

Les éléments de ce tableau de tableaux seront des entiers compris entre 0 et 4 :  

- 0 pour une case vide,
- 1 ou 2 pour un rond ou une croix,
- 3 ou 4 pour un rond ou une croix issu d'un alignement victorieux.

Ainsi, une grille en cours de jeu sera constituée de 0, 1 et 2. Lorsqu'un joueur a gagné, la grille comportera en plus, soit trois 3, soit trois 4 modélisant les trois éléments alignés.  

\   

Le programme comportera deux variables globales :  

- `joueur` qui vaut 1 ou 2 selon le joueur qui doit jouer. La variable vaut 1 au début du jeu.
- `partie_en_cours` qui est un Booléen, indiquant si le jeu peut se poursuivre ou non. Par défaut, cette variable vaut `True`. Elle passe à `False` quand trois symboles sont alignés ou lorsque la grille est pleine.

## Initialisation du jeu
Compléter la fonction `init_grille`, déjà documentée, qui renvoie un tableau de tableaux à 3 éléments tous nuls.  

## Affichage d'une grille de jeu
Compléter la fonction `afficher_grille`, déjà documentée, qui affiche dans la console la grille selon l'exemple fourni.  Compléter la documentation de cette fonction par d'autres exemples intéressants.  

## Vérification d'une grille
La vérification d'une grille consiste à :  

- vérifier s'il y a un alignement de trois éléments identiques sur une ligne, une colonne ou une diagonale ;
- modifier la grille du jeu en indiquant trois 3 ou trois 4 en cas d'alignement des symboles d'un des deux joueurs.

Pour cela, compléter les fonctions :  

- `verifier_ligne` qui vérifie la ligne dont le numéro est passé en paramètre.  
Ainsi, `verifier_ligne(grille, 1)` vérifie la deuxième ligne de la grille ;
- `verifier_toutes_lignes` qui vérifie l'ensemble des lignes de la grille passée en paramètre.  
`verifier_toutes_lignes` utilisera la fonction `verifier_ligne` ;
- `verifier_colonne` et `verifier_toutes_colonnes` sont à écrire selon le même modèle que les fonctions de vérification des lignes ;
- `verifier_diagonale1` et `verifier_diagonale2` sont des fonctions pour vérifier chacune des diagonales, peu importe l'ordre.  
`verifier_toutes_diagonales` permettra de vérifier les deux diagonales ;
- `verifier_grille` permet de vérifier l'ensemble d'une grille passée en paramètre.

Evidemment, les fonctions vérifiant plusieurs lignes, colonnes ou diagonales utiliseront la ou les fonctions précédentes.  

## La fonction principale
Ecrire une fonction `morpion` qui permet que le jeu puisse se dérouler correctement :  

- saisie de la position de la croix ou du cercle à ajouter,
- vérification de la validité du coup proposé,
- ajout du coup,
- vérification de la grille,
- affichage de la grille,
- arrêt du jeu ou passage à l'autre joueur.

Les joueurs saisiront leurs choix dans la console. Pour cela, vous utiliserez l'instruction `input`.  

Vous n'hésiterez pas à ajouter d'autres fonctions afin d'alléger le contenu de la fonction `morpion`. En particulier, vous serez amenés à ajouter des fonctions pour chaque élément indiqué ci-dessus (saisie, vérification de la validité du coup, ajout d'un coup dans la grille, etc.).  

# Partie graphique
## Affichage
Modifier la fonction d'affichage pour que l'affichage s'effectue dans une fenêtre graphique et non plus dans la console.  

La fonction utilisera la bibliothèque `Pygame`.  

Pour rappel, en cas d'alignement, la couleur des éléments alignés est différentes, et est modélisée par des 3 ou des 4 dans la grille.  

## Saisie des coups
Modifier l'une ou les fonctions écrites pour la saisie s'effectue sur la partie graphique à l'aide du bouton gauche de la souris.

\   

\underline{{\textit{\textbf{Sources}}}}  

- ROCHE D. (2020, 17 septembre). \textit{Projet : jeu du morpion avec Pygame}. Informatique au lycée. [https://pixees.fr/informatiquelycee/n_site/nsi_term_projet_3.html](https://pixees.fr/informatiquelycee/n\_site/nsi\_term\_projet\_3.html)