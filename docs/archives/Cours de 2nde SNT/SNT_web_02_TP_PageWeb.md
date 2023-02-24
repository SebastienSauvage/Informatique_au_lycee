---
title: "Thème web - Chapitre 2 : Créer une page web"
author: [Sébastien SAUVAGE]
date: "06/09/2022"
keywords: [SNT, WEB, Page web, html, css]
discipline: SNT
...

\Huge \textbf{Thème 2 : Le web}\normalsize  

\ 

\huge \textbf{Chapitre 2 : Créer une page web}\normalsize

\ 

L’objectif de ce TP est de découvrir comment une page Web est structurée, de découvrir les langages qui permettent de l'écrire et ainsi être capable de créer ses propres pages Web.  

# Préambule
### A faire

Avant de créer un site Web, ou même votre première page Web, il faut avant tout préparer votre espace de travail. Il existe déjà un dossier `documents_profs` :

- Au même endroit, créer un dossier sous la forme `NOM_Prenom` (sans accent) et un sous-dossier `SNT` ;
- dans le dossier `SNT`, créer un dossier `site_Web` ;
- dans ce dossier, créer deux sous-dossiers `IMG` et `CSS`.

Maintenant que votre espace de travail est organisé, il faut maintenant créer une première page Web. Afin de vous faciliter la tâche, une partie du travail est déjà effectué.  

### A faire
Se rendre dans le dossier `documents_profs/SNT/HTML_CSS` et copier les trois fichiers, `Bulbizarre.html`, `Bulbizarre.css` et `Bulbizarre.png`, dans votre dossier `site_Web`.

Maintenant que votre espace est organisé et que les fichiers sont récupérés, l’ensemble du travail s’effectue dans le dossier `site_Web`.  

# Découvrir le langage HTML
## Afficher une page Web
### A faire
Dans un premier temps, double-cliquer sur le fichier intitulé `Bulbizarre.html`. Normalement un navigateur (_Chrome_, _Firefox_, _Edge_, etc.) s’ouvre et vous voyez une page Web peu attirante ...  

## Editer une page Web
Afin d’améliorer cette page est la rendre plus attirante, une modification du fichier `Bulbizarre.html` s’impose. Or un fichier `HTML` est un simple fichier texte.  

### A faire

1) Ouvrir le fichier `Bulbizarre.html` avec le _bloc note_ de la manière suivante :  

- Effectuer un clic droit sur le fichier `Bulbizarre.html`,
- choisir "_Ouvrir avec ..._",
- choisir "_Bloc note_".

2) Recopier la première ligne.  

......................................................................................................................................

3) Ecrire les deux caractères qui l'entourent ? On appelle cela **une balise**.  

......................................................................................................................................

4) Citer d'autres balises écrites dans le documents.  

......................................................................................................................................

\   

......................................................................................................................................

### A savoir
Le langage `HTML` est **un langage balisé**.

Une page `HTML` commence toujours par la balise `<!DOCTYPE html>`.

L’ensemble du reste du code doit se trouver entre les balises `<html>` et `</html>`.

Le reste de la page est scindée en deux : une partie entre les balises `<head>` et `</head>` non visible sur la page Web affichée (**la tête**), et une partie entre les balises `<body>` et `</body>` qui constitue la partie visible (**le corps**). Certaines pages peuvent contenir à la fin les balises `<foot>` et `</foot>` mais ce n'est pas le cas de la nôtre.

### A faire
Retrouver l'ensemble de ces balises dans le document HTML ouvert avec le _Bloc note_.

### A faire

1) Recopier le texte dans le navigateur indiqué sur l’onglet de la page.  

......................................................................................................................................

2)  
- Dans le fichier HTML ouvert avec le _Bloc note_, quelle ligne permet de définir ce texte ? Remplacer ce texte par le texte "_Bulbizarre_".
- Sauvegarder le fichier HTML (dans le _bloc note_, menu _fichier_ puis _sauvegarder_).
- Rafraîchir la page Web du navigateur en appuyant sur la touche F5. Observer le changement de texte au niveau de l’onglet de la page Web.

## Afficher une image
### A faire
Normalement, la page devrait afficher une image mais ce n'est pas le cas pour le moment.  

1) Recopier la ligne de code contenant la balise `<img \>`qui permet cet affichage.  

......................................................................................................................................

2) Ecrire le nom du fichier contenant une image. Ecrire le nom du dossier dans lequel il devrait se trouver.  

......................................................................................................................................

\   

......................................................................................................................................


3) Dans l'explorateur de fichiers, déplacer le fichier `Bulbizarre.png` dans le bon dossier que vous aviez créé en début de TP.  
Dans le navigateur, rafraîchir (touche F5 ) la page et normalement l’image devient visible.  

## Lien hypertexte
1) Ecrire une définition de l'expression **Lien hypertexte**. Préciser votre source.

......................................................................................................................................

\   

......................................................................................................................................

2) Recopier la ligne de code du fichier HTML contenant les balises `<a>` et `</a>` qui permet de définir un lien hypertexte.  

......................................................................................................................................

\   

Recopier l'adresse du lien hypertexte.  

......................................................................................................................................

\   

Expliquer à quoi sert le texte qui suit le mot clé `title`.

......................................................................................................................................

\   

......................................................................................................................................  

3) En bas de la page Web (dans le code du fichier ouvert avec le _Bloc note_, juste avant la balise `<body>`), ajouter un deuxième lien hypertexte vers l'adresse `https://www.pokepedia.fr/Liste_des_Pokémon_de_la_première_génération`  

3) Dans le _Bloc note_, sauvegarder le fichier HTML et dans le navigateur, réfraîchir la page. Vérifier que le lien ajouté fonctionne bien en cliquant dessus.  

## Ajouter une mise en forme
### A savoir
La mise en forme d’une page Web peut se coder directement dans le fichier `HTML`, mais généralement, cette partie est décentralisée dans un fichier `CSS` (_Feuille de style en cascade_) qui est lui-même un fichier texte et écrit dans un certain langage.  

### A faire
1) Recopier la ligne du fichier `HTML` qui fait référence à un fichier `CSS`.  

......................................................................................................................................

2) Ecrire dans quel emplacement devrait se trouver le fichier CSS.  

......................................................................................................................................

3) Déplacer le fichier `Bulbizarre.css` dans le bon dossier.  

4) Dans le navigateur, rafraîchir la page et normalement, la page prend un peu de couleur et de mise en forme : des marges sont apparues, une partie du texte est en gras, une autre est centrée, un dernière est « justifiée »[^1]

[^1]: Le texte commence le plus à gauche possible et se termine le plus à droite possible. La taille des espaces est ajusté.  

Nous sommes loin du résultat attendu, mais cela avance ...  

### A savoir
Pour indiquer qu’une partie du texte subit une certaine mise en forme, il faut :  

- dans le fichier `HTML`, ajouter `id = ’NomDeReference’` ou `class =’NomDeReference’` dans la balise à l’ouverture de l’objet que l'on souhaite mettre en forme (`<p>` pour les paragraphes par exemple) ;
- dans le fichier `CSS`, ajouter `#NomDeReference{...}` (pour une référence `ID`) ou `.NomDeReference{...}` (pour une référence `CLASS`).  

### A faire

1) Dans le fichier `HTML`, ajouter `class = ’paragraphe’` dans la balise `<p>` pour les paragraphes _Le Bulbizarre utilise couramment ..._ et _L’ensemble des images et ..._.
2) Sauvegarder le fichier `HTML`.
3) Rafraîchir la page dans le navigateur pour observer que les deux paragraphes sont maintenant "justifiés".

### A faire

1) Recopier la ligne du fichier `CSS` qui permet de modifier la couleur du texte.

......................................................................................................................................

Le fait que la définition de la couleur se trouve dans l’attribut `body` signifie que c’est l’ensemble des éléments contenus dans la balise `<body>` qui seront écrits en noir (Code couleur `#000000`).  

2) Modifier la couleur pour une écriture en rouge (code couleur `#FF0000`).  
Sauvegarder le fichier `CSS` et vérifier que le texte est bien en rouge en rafraîchissant la page Web dans le navigateur.  

3) Remettre le texte en noir.  

4) Mettre en couleur verte uniquement le texte _Physionomie et attitudes_.  
_Indication_ : pour déterminer le code hexadécimal de la couleur, vous pourrez vous aider par exemple de la page [https://www.w3schools.com/colors/colors_hexadecimal.asp](https://www.w3schools.com/colors/colors_hexadecimal.asp)  

### A savoir
Dans un code `HTML`,  

- `id = ’...’` permet de définir **une référence unique** d’un élément ;
- `class = ’...’` permet de définir une référence qui peut être reprise par plusieurs éléments.

Ainsi, lorsque l’on veut mettre en forme de la même manière plusieurs éléments, on utilisera `class` et lorsque l’on veut définir de manière unique une partie de la mise en forme d’un élément, on utilisera `id`.  

### A faire
Maintenant que vous avec découvert comment ajouter et modifier une mise en forme d’une partie d’une page Web, il ne vous reste plus qu’à ajouter des éléments ou modifier les fichiers `HTML` et `CSS` pour obtenir la page souhaitée[^2]  

[^2]: voir fichier documents_profs/SNT/HTML_CSS/page_modele.png  

Inspirez-vous des lignes déjà existantes dans le fichier `CSS` et le fichier `HTML` !  

# Création libre
### A faire
Parmi les sujets proposés ci-dessous, coder une page Web illustrant ce sujet en respectant les contraintes suivantes :    

- la page devra contenir au moins une image, ainsi qu’un lien hypertexte ;
- vous distinguerez dans deux fichiers différents le contenu (`HTML`) et la mise en forme (`CSS`) ;
- vous tâcherez de réinvestir ce que vous avez étudiez dans le paragraphe précédent en variant les couleurs de texte et de fond, la taille des caractères, la mise en forme des paragraphes, etc.
- votre page Web sera sauvegardée dans le dossier `NOM_Prenom/SNT/ma_page_web`

### Liste des sujets disponibles
Eva LOVELACE  
La pascaline  
Alan Turing  
Premier microprocesseur IBM  
Machine Enigma  
Tim Berners Lee  
Réseau Arpanet  
Le télégraphe  
Le téléphone  
La fibre optique  
Premier satellite de communication  
La radio  
La télévision  
Le moteur de recherche Google  
Le moteur de recherche Qwant  
Amazon  
Facebook  
Tweeter  
Mastodon  
Microsoft  
Linus Torvalds  
Wikipédia  
Richard Stallman  
Le jeu Pong  
IBM PC  
Linux, GNU-Linux  
Windows  
Mac OS  
Android  
La Commission Nationale Informatique et Libertés (CNIL)  
Les navigateurs Web historiques  