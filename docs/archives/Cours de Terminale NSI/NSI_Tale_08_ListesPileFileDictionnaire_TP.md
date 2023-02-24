---
title: "Thème 1 - Chapitre 3 : Liste, pile, file et dictionnaire"
author: [Sébastien SAUVAGE]
date: "16/11/2022"
keywords: [NSI, terminale, liste, pile, file, dictionnaire]
discipline: NSI
---
[^tag_w3s]:[https://www.w3.org/community/webed/wiki/HTML/Training/Tag_syntax](https://www.w3.org/community/webed/wiki/HTML/Training/Tag\_syntax)
[^prédicat]:**Prédicat** : dans ce contexte, il s'agit d'une fonction retournant `True` ou `False` en relation à une propriété du paramètre de cette dernière.
[^parser]:**parser** : Programme informatique qui met en évidence la structure d'un texte, d'un programme informatique.
[^docpythonfiles]:_5.1.2 Utilisation des listes comme des files_ : \par [https://docs.python.org/fr/3/tutorial/datastructures.html\#using-lists-as-queues](https://docs.python.org/fr/3/tutorial/datastructures.html\#using-lists-as-queues)
[^methodeindex]:_Méthode index_ : [https://docs.python.org/fr/3/library/stdtypes.html?highlight=index\#str.index](https://docs.python.org/fr/3/library/stdtypes.html?highlight=index\#str.index)
[^methodesplit]:_Méthode split_ : [https://docs.python.org/3.6/library/stdtypes.html\#str.split](https://docs.python.org/3.6/library/stdtypes.html\#str.split)

\huge \textbf{Thème 1}\normalsize  

\ 

\Large \textbf{Chapitre 3bis : Liste, pile, file et dictionnaire}\normalsize  

\  

\  

# Motivation
## Fichier au format HTML bien formés
Le HTML est un format de fichier utilisé par les navigateurs web. Les fichiers au format HTML (et plus généralement au format XML) sont des fichiers texte dans lesquels on trouve des balises :

- ouvrantes de la forme `<nom attributs>`,
- fermantes de la forme `</nom>`,
- auto-fermantes de la forme `<nom attributs/>`.

où `nom` désigne le nom de la balise et `attributs` une liste de couples `clé=valeur`.  

Dans la pratique, `nom` est par exemple `div`, `p`, `html`, `body`, `head`, ...  

Pour la syntaxe des tags HTML, voir la page du W3C dédiée[^tag_w3s]. Les balises auto-fermantes sont : `area`, `br`, `hr` , `img` , `input` , `link` , `meta` et `param`.  

Dans cette activité, on considère qu'un document HTML est bien formé si :  

- à chaque balise ouvrante correspond une balise fermante,
- on ne peut fermer une balise que si toutes les balises situées entre les deux balises ouvrantes et fermantes  sont fermées.

Par exemple, les documents `ex1.html` et `ex4.html` sont bien formés, alors que les documents `ex2.html` et `ex3.html` sont mal formés.  

On veut écrire un prédicat[^prédicat] renvoyant `True` si un texte est un document HTML bien formé et `False` dans le cas contraire.  

Dans ce cadre, on peut donc ne pas tenir compte des balises auto-fermantes (et on ne demande pas de vérifier ici si les balises sont des balises `HTML` existantes, ni si on respecte les attributs des balises).  

La première étape est d'écrire un parser[^parser] de fichier `HTML`, permettant de parcourir séquentiellement les balises.  

# Écriture d'un parser HTML
L'écriture d'un tel parser est une tâche difficile, car un caractère `<` peut être rencontré dans différentes situations :

- Situation 1 : définition du type du document : `<!DOCTYPE ...>`
- Situation 2 : signe inférieur dans le texte : `i < len(l)`
- Situation 3 : commentaires HTML `<!-\ -` et `-\ ->`
- Situation 4 : signe inférieur dans des attributs : `<script data-user=">myfunc();">`

Pour simplifier les choses nous commencerons par traiter uniquement des fichiers `HTML` avec la situation 1, puis nous autoriserons dans une deuxième version les documents `HTML` contenant les situations 2 à 4.  

## Structure de file
Les tags rencontrés seront ajoutés dans une file. Une file est une structure de données séquentielle agissant comme une file d'attente : on peut ajouter et retirer des éléments de la structure, mais les premiers éléments ajoutés seront toujours les premiers à sortir.  

La structure de file dispose des primitives suivantes :  

- `q=Queue()` : crée une nouvelle file vide ;
- `q.enqueue(el)` : ajoute l'élément `el` à la file `q` ;
- `q.dequeue()` : enlève le premier élément ajouté à la structure et le renvoie ;
- `q.is\_empty()` : renvoie `True` si, et seulement si, la file est vide.  

On dit que la file est une structure `FIFO` (`First In First Out`).  

Le fichier `myqueue.py` contient le squelette d'un module implémentant une structure de file (on ne peut utiliser le nom `queue.py` car Python dispose déjà d'un module homonyme).  
\newpage

### A faire
1. Prendre connaissance du paragraphe 5.1.2 de la documentation Python[^docpythonfiles].  
Comme ce paragraphe l'indique : _toutefois, les listes ne sont pas très efficaces pour réaliser ce type de traitement. Alors que les ajouts et suppressions en fin de liste sont rapides, les opérations d'insertions ou de retraits en début de liste sont lentes (car tous les autres éléments doivent être décalés d'une position)._  
Aussi, il sera judicieux d'utiliser comme attribut de notre classe `Queue` une structure de la classe `collections.deque`.
2. Recopier le fichier `myqueue.py` dans votre espace de travail et compléter-le.  

## Première version
Dans un module `html\_parser1.py`, écrire une première version du parser : la fonction `parse(document)` prend en paramètre un document sous forme d'une chaîne de caractères et renvoie une file contenant les tags.  

Pour vous aider, le fichier `html\_parser1.py` contient le squelette d'un parser.  

Dans cette première version, on considère que seule la situation 1 peut être rencontrée et on ignore les situations 2, 3 et 4. Et on rappelle que les balises auto-fermantes peuvent être ignorées.  

Par souci de simplification on pourra considérer que les attributs d'une balise ne peuvent être séparés que par des espaces.  

On utilisera à profit la méthode `index`[^methodeindex] des chaînes de caractères :  

```Python
>>> help(str.index)
Help on method_descriptor:

index(...)
    S.index(sub[, start[, end]]) -> int
    
    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Raises ValueError when the substring is not found.
```

La méthode `split`[^methodesplit] peut également s'avérer utile.  

### A faire
Recopier le fichier `html\_parser1.py` dans votre espace de travail et compléter-le en tenant des conseils ci-dessus.  

# Vérificateur HTML : un algorithme
Dès que l'on peut récupérer les tags séquentiellement, nous pouvons nous attaquer à l'écriture du vérificateur `HTML` (checker). Il peut être utile de faire l'analogie entre les documents `HTML` et les expressions correctement parenthésées.  

Une expression bien parenthésée est une expression contenant un certains nombre de  type de parenthèses telle que :  

- à chaque parenthèse ouvrante correspond une parenthèse fermante,
- à tout moment, on ne peut fermer une parenthèse que si l'expression située entre les deux parenthèses se correspondant est bien parenthésée.  

Par exemple, les expressions suivantes sont bien parenthésées :  

- `((()))`
- `()()()`
- `([\{\}]())`

Les expressions suivantes ne sont pas bien parenthésées :  

- `(()))`
- `(()`
- `([)]`

\newpage

Pour vérifier si une expression est correctement parenthésée, une méthode est d'utiliser une pile :  

- lorsque l'on rencontre une parenthèse ouvrante on l'empile,
- lorsque l'on rencontre une parenthèse fermante, par exemple `]}` :  
  - si la pile est vide, alors l'expression est mal parenthèsée (trop de fermantes),
  - sinon, on  dépile l'ouvrante située au sommet de la pile et on vérifie que les deux parenthèses correspondent (`(` et `)`, `[` et `]`).  

Lorsque toute la chaîne a été parcourue, la pile doit être vide (pas d'ouvrante non fermée).  

Un document `HTML` peut être vue comme une expression parenthésée :

- les tags ouvrants `<tag>` sont les parenthèses ouvrantes ;
- les tags fermants `</tag>` sont les parenthèses fermantes.  

Sur la pile, on placera des tags ouvrants.  

# Opération primitives sur les piles
Les `piles` sont des structures de données linéaires admettant les `opérations primitives` suivantes :  

- création d'une pile vide ;
- empilement d'un élément sur une pile ;
- dépilement du sommet d'une pile ;
- test de vacuité d'une pile.  

Le principe d'une pile est le suivant : on ne peut accéder un élément (e) de la pile qu'en ayant enlevé d'abord tous les éléments empilés après (e).  

L'élément renvoyé par la méthode `pop` est le dernier élément empilé. On dit que la pile est une structure **LIFO** (_Last In First Out_).

# Implémentation du module mystack
Le fichier `mystack.py` contient le squelette de l'implémentation d'une pile.  

### A faire
1. Copier dans votre espace de travail le fichier `mystack.py` et implémentez votre propre structure de pile.
2. Enfin, copier dans votre espace de travail le fichier `html\_checker.py` et implémenter l'algorithme de vérification.  

# Amélioration du parser
## Utiliser des expressions régulières
L'objectif est ici d'écrire une nouvelle version du parser permettant de prendre en compte l'ensemble des situations particulières listées plus haut.  

Pour cela, nous pouvons utiliser une expression régulière. Une expression régulière est une chaîne de caractère spécifiant un format permettant de :  

- dire si une chaîne correspond au format ;
- capturer certaines parties de ce format.

Un cours sur les expressions régulières est hors du programme, mais nous allons en fournir une pour récupérer les tags d'un document `HTML`.  

Le code du fichier `html\_parser2.py` contient une expression régulière présentée sur plusieurs lignes pour plus de lisibilité. Elle permet de récupérer les tags en tenant compte des guillemets.  

### A faire
1. Copier le fichier `html\_parser2.py` dans votre espace de travail.
2. Bien regarder l'exemple d'utilisation de l'expression régulière pour la comprendre (lignes 30 à 45).  
Ne pas hésiter à tester plusieurs exemples dans la console Python.
3. En utilisant cette expression régulière, écrire une deuxième version du parser en complétant la fonction `parser`.  

## Pour aller plus loin
Utiliser une expression régulière a toujours ses limites pour parser un fichier html. Des bibliothèques existent pour itérer sur les tags d'un tel document.  

Parmi elles, on peut utiliser la classe `HTMLParser`. Le fichier `html\_parser3.py` contient le code d'une classe héritant de `HTMLParser` et qui construit la liste des tags.  

### A faire
1. Copier le fichier `html\_parser3.py` dans votre espace de travail.
2. Compléter la fonction `parser` utilisant la classe décrite dans ce même fichier.  

\   

\   

\underline{{\textit{\textbf{Sources}}}}  

- Université de Lille (2020, 21 novembre). _Piles et files_. Enseignement DIU EIL.  
[https://gitlab-fil.univ-lille.fr/diu-eil-lil/portail/-/blob/master/bloc4-5/pile_file/pile.md](https://gitlab-fil.univ-lille.fr/diu-eil-lil/portail/-/blob/master/bloc4-5/pile\_file/pile.md)
