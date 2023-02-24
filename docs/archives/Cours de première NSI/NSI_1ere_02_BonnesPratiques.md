---
title: "Thème 1 - Chapitre 2 : Bonnes pratiques en programmation"
author: [Sébastien SAUVAGE]
date: "06/09/2022"
keywords: [NSI, première, pratique, programmation, python]
discipline: NSI (1ère)
---

[^hist-info.org]: François GUILLIER. *Histoire de l'informatique* [en ligne]. 2016 [consulté le 18 juillet 2019]. [histoire-informatique.org](https://histoire-informatique.org/grandes_dates/)  
[^hist-info.online]: Serge ROSSI. *Histoire de l'informatique* [en ligne]. 20 novembre 2004 [consulté le 18 juillet 2019]. [histoire.info.online.fr](http://histoire.info.online.fr/)  
[^logopython]: Logo python (c) : [https://www.python.org/static/img/python-logo.png](https://www.python.org/static/img/python-logo.png)  
[^algolfortran]: Familles Algol et Fortran : [https://commons.wikimedia.org/wiki/File:Algol%26Fortran_family-by-Borkowski.svg](https://commons.wikimedia.org/wiki/File:Algol%26Fortran_family-by-Borkowski.svg)  
[^thonny]: [Thonny](https://thonny.org/)  
[^edupython]: [Edupython](http://edupython.tuxfamily.org/)  
[^python]: [python](https://www.python.org/)  
[^notepadpp]: [notepad++](https://notepad-plus-plus.org/fr/)  

\huge \textbf{Thème 6}\normalsize  

\ 

\Large \textbf{Chapitre 1 : Quelques bonnes pratiques en programmation}\normalsize  

# Eléments du programme  

![NSI_1ere_02_BonnesPratiques](./NSI_1ere_02_BonnesPratiques_Tab_Programme.png) \   

# Un peu (voir plus si affinité !) d'histoire [^hist-info.org] [^hist-info.online]  
**_1947_** : Apparition de `l'assembleur` (utilisation de mnémoniques). Inventé par Maurice V.Wilkes de l'Université de Cambridge, ce langage est le premier langage de ce type a être mis au point afin de faciliter l'usage des ordinateurs. Chaque instruction machine est codée sous forme de symboles dans un style proche du langage naturel. Par exemple: " début ", " stop ", " aller en " ... Avant la programmation s'effectuait directement en binaire.  
**_1951_** : Premier langage compilé: le `A0` par Grace Hopper. Cela permet de générer du code binaire à partir d'un code source.  
**_1956_** : Création du premier langage de programmation universel, le `FORTRAN` (FORmula TRANslator) par John Backus d'IBM. Mis au point sur un IBM 701, c'est le premier langage informatique de haut niveau, c'est à dire qu'il nécessite un programme intermédiaire (le compilateur) qui le traduit en instructions compréhensibles par l'ordinateur. L'avantage est que le programme en FORTRAN est indépendant de la machine, il suffit d'avoir le compilateur adapté. Il est encore utilisé dans les domaines scientifiques et techniques.  
**_1958_** : John Mc Carthy, mathématicien au MIT (Massachusetts Institute of Technology) qui y a fondé en 1957 le département d'Intelligence Artificielle, crée le langage de programmation `LISP` (LISt Processing) qui va avoir une grande influence sur le développement de la programmation objet. Ce langage sera initialement développé sur IBM 7090.  
**_1960_** : Création de l'`ALGOL` par Edsger Dijkstra. Très théorique, ce langage sera très peu utilisé mais sera très étudié comme modèle. Sa création est l'issue d'une conférence quelques années avant entre américains et européens durant laquelle a été lancée l'idée d'un langage standard universel.  
**_1960_** : Publication du cahier des charges du langage de programmation `COBOL` (COmmon Business Oriented Language) par Grace Hopper. Il devient, après le FORTRAN, le second grand langage de programmation universel, faisant ainsi rapidement disparaître l'ALGOL. Sa consécration par le Département de la Défense Américain qui l'a déclaré indispensable, l'accent qu'il met sur les structures de données et sa syntaxe proche de l'anglais en ont fait un langage largement utilisé, particulièrement dans les applications commerciales.  
**_1964_** : Thomas Kurtz et John Kemeny créent le langage `BASIC` (Beginner's All-purpose Symbolic Instruction Code) au Dartmouth College pour leurs étudiants. Ses versions initiales n'étaient ni structurées ni compilées, alors que les plus récentes sont toujours structurées et souvent compilées.  
**_1966_** : Le langage de programmation `LOGO` est crée par une équipe chez BBN (Bolt Beranek & Newman) dirigée par Wally Fuerzeig dont faisait partie Seymour Papert. Ce langage très graphique est basé sur le principe d'une tortue que l'on pilote à l'écran en lui donnant des ordres (tourner, avancer, etc...).  
**_1968_** : Création du `FORTH` par Charles Moore. C'est un langage informatique basé sur l'utilisation de piles de données. De par son status entre langage de bas-niveau (très proche du matériel) et de haut niveau, il est extrêmement compact et rapide. Il a longtemps été utilisé comme 'Open Firmware' (logiciel chargé de charger le système d'exploitation) par les machines d'Apple et de Sun.  
**_1968_** : Création du PASCAL par Nikhlaus Wirth. La rigueur nécessaire pour utiliser ce langage de haut niveau fait qu'il est très apprécié dans l'enseignement. Il a été très largement popularisé par sa version développée par Philippe Kahn: `Turbo Pascal` (1983) de BORLAND.  
**_1970_** : Ken Thompson, pensant qu'UNIX ne serait pas complet sans un langage de programmation de haut niveau commence à porter le Fortran sur le PDP 7 mais change rapidement d'avis et crée en fait un nouveau langage, le `B` (en référence au BCPL dont il s'inspire).  
**_1972_** : Successeur du langage B, le `C`, créé par Dennis Ritchie a pour objectif premier d'aider au développement d'Unix. Il fait évoluer le langage et le dote d'un vrai compilateur générant du code machine PDP/11 (le B était un langage interprété). Le langage C est à la fois proche du matériel, permettant ainsi de réécrire le noyau UNIX en C (Cf. été 1973) et suffisamment généraliste, le rendant ainsi facilement portable. Les développements et les succès du langage C et d'UNIX sont intimement liés. Brian Kernighan écrit en 1978 un livre au sujet de la programmation en langage C devenu LA référence au point que ce livre est surtout connu sous le nom : "Le Kernighan & Ritchie".  
**_1972_** : Création du premier langage orienté objet, SmallTalk par Alan Kay au Xerox PARC.  
**_1972_** : Conçu par le Français Alain Colmeraurer, le `PROLOG` (PROgrammation en LOGique) est un langage dit "descriptif de l'Intelligence Artificielle".  
**_1983_** : Bjarn Stroustrup développe une extension orientée objet au langage C : le `C++`.  
**_20 février 1991_** : Apparition du langage `PYTHON` (le nom provient de la série TV Monty Python's Flying Circus dont l'auteur, Guido Van Rossum, était fan). C'est un langage de programmation interprété, placé sous licence libre. Il fonctionne sur la plupart des plateformes informatiques (windows, unix, macOS, android, iOS). Sa syntaxe simple permet de faciliter le travail des programmeurs.  
![Logo Python](./NSI_1ere_02_BonnesPratiques_python-logo.png) [^logopython]  
**_1995_** : Le langage `JAVA` (signifie "café" en argot américain - en argot français on dit "Kawa" ), développé par la firme Sun Microsystems, fait son apparition. Ce langage objet est principalement utilisé sous forme d'applet en symbiose avec un client Web. Il a pour cela une particularité: le programme est d'abord compilé en "p-code" (byte-code) totalement indépendant de l'architecture. Puis ce p-code est interprété (c'est à dire transformé au fur et à mesure en code spécifique à l'ordinateur) lors de l'exécution du programme.  
**_1995_** : Brendan Eich crée le `JAVA SCRIPT`. Initialement appelé LiveScript, ce langage a été créé en s'inspirant de nombreux langages (dont Java) mais en simplifiant la syntaxe. Ce langage va connaître différentes implémentations par Microsoft (JScript) ou Adobe (LiveScript) mais c'est au milieu des années 2000 que sont utilisation va devenir indissociable des pages Web, en particulier pour les actions asynchrones (AJAX).  
**_2000_** : Le `C#` est un langage développé par Microsoft, inspiré par le langage Java.  
![Famille Algol et Fortran](./NSI_1ere_02_BonnesPratiques_AlgolFortran_family-by-Borkowski.png) [^algolfortran]  

# Préambule  
Sur les premiers ordinateurs, les premiers programmes étaient écrits en langage machine, le seul langage qu'un ordinateur est capable de comprendre. C'était des suites d'instructions écrites en binaire, dont avec une multitude de 0 et de 1. Très peu pratique, le langage assembleur est alors apparu : il s'agit alors de coder les instructions par des mots (mnémoniques) comme par exemple `ADD` pour ajouter. Malgré tout, ce langage est très proche du langage machine puisqu'il suffit de traduire les instructions en code binaire pour que l'ordinateur comprenne. Au fil du temps, des langages plus évolués sont apparus selon les besoins d'utilisation de l'ordinateur. Ainsi, les langages qui apparaissent ensuite sont de plus en plus simples à utiliser puisqu'une instruction dans ce nouveau langage regroupe parfois de nombreuses instructions en langage machine. Ces langages sont plus ou moins `évolués` et on les classe en deux grandes catégories : les langages interprétés et les langages compilés.  
Il existe de nombreux langages de programmation et chacun répond à des besoins souvent différents : traitement de grandes quantités de données, graphisme, pages web, ...  
Par exemples, pour programmer dans une page web, les langages php ou javascript seront souvent choisis. Ensuite, le C ou le C++ sont des langages assez proches du système mais plus délicat à maîtriser. Le java ou le python sont des langages plus évolués, plus accessibles.  
Dans le cadre de l'enseignement NSI, tout comme la plupart des enseignements du lycée, le langage Python sera souvent le langage utilisé. Malgré tout, dans le cadre de la spécialité NSI, nous étudierons également quelques aspects d'autres langages afin d'en dégager les points communs et les différences pour notre usage.  

# Découverte de Python
Il existe différentes manières d'écrire un programme en langage python. Tous permettent d'écrire le même fichier au format `PY` mais ces logiciels offrent des ajouts et un confort non négligeables parfois selon l'usage que l'on en a : affichage des contenus des variables, modules intégrés supplémentaires, coloration syntaxique, ... Un simple éditeur de textes suffit ! Bien que ce choix est assez personnel, dans le cadre de l'enseignement NSI, nous utiliserons essentiellement le logiciel `Thonny`[^thonny] mais libre à vous d'en tester d'autres à la maison : Edupython (sous windows)[^edupython], Python et idle[^python], notepad++ (sous windows)[^notepadpp] ... Certains sites proposent également d'écrire les programmes en ligne, ce qui évite d'installer le moindre logiciel.  

Edupython, Idle et Notepad++ sont disponible en version portable (utilisation sur clé USB par exemple, sans installation sur l'ordinateur).  

# Une première fonction    
L'objectif de cette partie est d'établir un petit programme qui permette de calculer la distance parcourue par un sportif selon son temps et sa vitesse moyenne.  
Ouvrir le logiciel Thonny :  
![thonny](./NSI_1ere_02_BonnesPratiques_thonny.png)  
La première chose est d'afficher le contenu des variables : menu *View* puis cocher *Variables*.  
Le temps que l'on y est, modifions quelques réglages : menu *Tools*, *Options...*  
Cocher *Highlight matching names*, *Highlight local variables*, et *Show line number*. Enfin, choisir *80* dans *Recommended maximum line lenght*.  La coloration syntaxique permettra de visualiser les variables, et un trait imaginaire vertical apparaîtra pour indiquer la limite recommandée pour écrire une ligne de code.  

## Utilisation de l'invite de commande (Shell)  
Pour calculer la distance parcourue, il suffit d'utiliser la formule : $D = V \times t$ où $D$ est la distance, exprimée en mètres, $V$ est la vitesse moyenne, exprimée en $m.s^{-1}$ et $t$ est la durée du parcours, exprimée en secondes.  
Calculons par exemple la distance parcourue par un cycliste allant en moyenne à $8 m.s^{-1}$ pendant $2 h$, c'est à dire $7 200 s$.  
Dans la zone `Shell`, saisir :
```python
>>> vitesse = 8
>>> duree = 7200
```  
On observe dans la colonne de droite *Variables* le contenu des deux qui viennent d'être saisies.  
Les espaces autour du signe '=' ne sont pas nécessaires mais permettent une meilleure lisibilité de la ligne de code. Pour les mêmes raisons, on appelle *vitesse* la vitesse au lieu de *v* par exemple.  
Pour calculer la distance, il suffit de saisir :  
```python  
>>> distance = vitesse * duree  
>>> distance
```  

**A faire**  

Quelle est la distance parcourue par le coureur cycliste ?  

\   

## Ecrire sous forme d'une fonction  
A chacune de ses sorties, le coureur cycliste doit donc saisir les trois lignes dans le Shell pour obtenir la distance parcourue. Evidemment, ça demande à chaque fois trois lignes de saisie pour le même calcul et de connaître la formule ! Afin d'automatiser cela, nous allons créer ce que l'on appelle une fonction. Celle-ci permettra d'automatiser la formule et pourra même être sauvegardée afin d'éviter de la saisir à chaque utilisation.  

### Saisie de la fonction  
Dans le cadre *untitled*, saisir le code suivant :
```python  
#! /usr/bin/python3
# coding: utf-8

def calcul_distance(vitesse, duree):  
  distance = vitesse * duree  
  return distance
```  
La première ligne permet l'utilisation du programme en mode console sous Linux par exemple.  
La seconde ligne permet d'indiquer le format d'encodage des caractères.  
On notera que pour indiquer ce qui fait partie de la fonction est décalé d'au moins 4 espaces, c'est ce qu'on appelle `une indentation`. Sans elle, les lignes ne sont plus considérée comme faisant partie de la fonction, ce qui peut conduire à des erreurs.  
Une fonction se termine de préférence toujours par `return`.  

### Sauvegarder le script  
Quand on effectue un travail en informatique, la première chose à effectuer est de sauvegarder ! Aller dans le menu *File* puis *Save as...*, aller dans le dossier `/NSI/premiere` de votre espace de travail et choisir ensuite comme nom de fichier `NOM_Prenom_bonnes_pratiques.py`. Eviter les accents et remplacer les espace par le caractère '\_' obtenu à l'aide de la touche '8'.  

Avant d'utiliser notre fonction, il faut la faire reconnaître par l'interpréteur. Dans le menu *Run* choisir *Run current script* ou simplement, appuyer sur *F5*.  
La fonction est disponible (elle apparaît à droite dans la liste des variables).

### Utiliser notre fonction  
Dans la partie *Shell*, saisir :
```python  
calcul_distance(8, 7200)  
```  
On obtient ainsi la distance parcourue attendue.  

### Exercice  
Si l'on souhaite effectuer d'autres calculs de distance, il suffit de saisir `calcul_distance(..., ...)` en remplaçant les pointillés par la vitesse et le temps dans cet ordre. Il n'est pas utile avant d'appuyer de nouveau sur *F5*, la fonction étant toujours reconnue.  
Pour les deux questions ci-dessous, écrire l'instruction à saisir dans la console puis indiquer la valeur renvoyée par la fonction.  

1. *Calculer de cette manière la distance parcourue par ce même cycliste pour une sortie à la même vitesse mais d'une durée de 4h.*  

\   

2. *Un coureur à pied s'aligne sur une course de 10 km. Grace à son entraînement, il estime sa vitesse moyenne de course à 2,8 $m.s^{-1}$. Peut-il espérer faire cette course en moins d'une heure ? (répondre à la question en s'aidant de la fonction créée précédemment)*  

\   


## Documenter d'une fonction  
L'intérêt de programmer des fonctions réside aussi dans le fait qu'elles puissent être utilisées dans un autre cadre, par un autre utilisateur car il est rare en programmation qu'un logiciel soit le fruit d'une seule personne.  Dans notre cas, on peut imaginer que notre fonction puisse être utilisée par un autre élève d'une autre classe par exemple. Comment savoir alors que dans notre fonction `calcul_distance`, il faille saisir en premier la vitesse ? Pour répondre à cette question, il faut écrire **la documentation** de la fonction. Pour y avoir accès, il suffit dans le Shell de saisir `help(calcul_distance)`. Essayez ! Evidemment, pour le moment, cela n'apporte pas grand chose comme info !  

### Décrire la fonction  
La fonction s'appelle `calcul_distance` mais elle n'est pas assez explicite pour comprendre le cadre de son usage. Cela pourrait être un calcul de distance avec le théorème de Pythagore par exemple ...  
Compléter votre fonction en ajoutant les lignes manquantes :  
```python  
def calcul_distance(vitesse, duree):
    '''
    Cette fonction calcule la distance parcourue en fonction de la vitesse
    moyenne et de la durée de parcours données en paramètres.
    '''
    distance = vitesse * duree
    return distance
```
La documentation s'écrit entre succession de trois apostrophes \' \' \'. Elle est écrite sous la première ligne qui définit la fonction. Elle ne sera pas lue lors de l’exécution de la fonction.  
Dans un premier temps, la description est écrite en français, mais il faut garder en tête qu'elle est destinée au monde entier et donc devrait être écrite en anglais ! A l'avenir, n'hésitez pas à écrire dans la langue de Shakespeare dans vos documentations pour prendre de meilleures habitudes.  

Saisir de nouveau `help(calcul_distance)` pour voir la nouvelle documentation de votre fonction. Penser à appuyer sur F5 avant pour que les modiciations soient prisent en compte.  

### Préciser les paramètres  
Tout cela n'indique toujours pas l'ordre des paramètres et leurs contenus, même si leur nom est assez explicite !  
Pour cela, il faut ajouter quels sont les paramètres de la fonction et préciser leur usage.  
Compléter de nouveau votre fonction :  
```python  
def calcul_distance(vitesse, duree):
    '''
    Cette fonction calcule la distance parcourue en fonction de la vitesse
    moyenne et de la durée de parcours données en paramètres.

    :param:
    vitesse : (float) Vitesse moyenne de l'objet.
    duree : (float) Durée de parcours.
    '''
    distance = vitesse * duree
    return distance
```  
Il n'y a pas de convention particulière pour la description des paramètres. Par exemple, on peut écrire *:param:* avant de les décrire.  
*float* correspond au type du contenu de la variable. Dans le cas présent, comme il s'agit d'un nombre réel (nombre flottant en informatique), on indique cela. Pour un entier, on indiquerait *int*, pour un chaîne de caractères (string), on écrirait *str*, pour une liste d'éléments *list*, etc ...  

Sauvegarder et exécuter le script. Vérifier les modifications prises en compte dans votre documentation en saisissant de nouveau `help(calcul_distance)` dans le Shell.  

### Préciser ce que la fonction retourne  
Enfin, pour pouvoir exploiter la fonction dans un autre cadre, il est nécessaire d'indiquer également le type de donnée retournée par la fonction. Compléter votre documentation comme suit :  
```python  
def calcul_distance(vitesse, duree):
    '''
    Cette fonction calcule la distance parcourue en fonction de la vitesse
    moyenne et de la durée de parcours données en paramètres.

    :param:
    vitesse : (float) Vitesse moyenne de l'objet.
    duree : (float) Durée de parcours.

    :renvoie:
    (float)
    '''
    distance = vitesse * duree
    return distance
```
On peut préciser également ce que renvoie la fonction, mais dans notre cas, c'est déjà indiqué dans la description de la fonction.  
Vérifier les modifications via le Shell.  

### Autre manière de préciser le type des paramètres et objet renvoyé
Plutôt que de spécifier comme ci-dessus les types des paramètres et de l'objet retourné, il est possible sur la première ligne qui défini la fonction de préciser ces spécifications. Pour cela, il suffit de les préciser comme cela :  
```python  
def calcul_distance(vitesse : float, duree : float) ->float :
    '''
    Cette fonction calcule la distance parcourue en fonction de la vitesse
    moyenne et de la durée de parcours données en paramètres.
    '''
    distance = vitesse * duree
    return distance
```

### Vérifier les préconditions  
**A faire**  
Dans la console, saisir :  
```python
>>> calcul_distance('bonjour', 'bravo')
```
Que ce passe-t-il ? Pourquoi ?  

\   

\   

Afin d'éviter ce type de messages d'erreurs liés aux types des paramètres saisis par l'utilisateur, il est possible de vérifier les types des paramètres saisis. Pour cela, on utilise l'instruction `assert` de la manière suivante :  
```python  
def calcul_distance(vitesse : float, duree : float) ->float :
    '''
    Cette fonction calcule la distance parcourue en fonction de la vitesse
    moyenne et de la durée de parcours données en paramètres.
    '''
    assert isinstance(vitesse, int) or isinstance(vitesse, float), "Vous devez saisir un nombre"
    distance = vitesse * duree
    return distance
```

**A faire**  

1) Saisir de nouveau dans la console `calcul_distance('bonjour', 'bravo')`. Quel est cet fois le message d'erreur ?  

\  

2) Ajouter une deuxième ligne avec l'instruction `assert` qui permet de vérifier la précondition du paramètre `duree`.  

### D'autres éléments  
Dans la documentation, on peut ajouter d'autres éléments :  

* Les conditions d'utilisation :
```python  
    ...
    :CU:
    Aucune
    ...
```  
* Les effets de bord, c'est-à-dire les modifications autre que les modifications locales (au sein de la fonction) :
```python
    ...
    :Effet de bord:
    Aucune
    ...
```  
Comme effet de bord, on peut souvent trouver l'affichage dans le Shell ou encore la modification d'une variable définie en dehors de la fonction (variable globale). Il faut **éviter les effets de bord**, sources de nombreux problèmes.  

## Utiliser un jeu de tests  
Enfin, lorsque l'on écrit une fonction, il est toujours préférable d'illustrer la documentation par un ou plusieurs exemples. Ainsi, au moment de l’exécution, cela permet une autovérification et ainsi parfois soulever des erreurs.  

### Ajouter des exemples tests
#### Syntaxe  
Pour ajouter des tests dans une fonction, il suffit d'ajouter les instructions précédées de `>>>` et en-dessous, la réponse attendue (comme l'affichage dans le Shell) :  
```python  
def calcul_distance(vitesse, duree):
    '''
    Cette fonction calcule la distance parcourue en fonction de la vitesse
    moyenne et de la durée de parcours données en paramètres.

    :param:
    vitesse : (float) Vitesse moyenne de l'objet.
    duree : (float) Durée de parcours.

    :renvoie:
    (float)

    :exemples:
    >>> calcul_distance(8, 7200)
    57600
    >>> calcul_distance(1, 200)
    200
    >>> calcul_distance(2, 3600) == 7200
    True
    '''
    distance = vitesse * duree
    return distance
```
Le dernier test est plus intéressant et se traduit par "Est-ce que calcul_distance(2, 3600) est égal à 7200", la réponse attendue étant "Vrai".  

**A vous !**  
Modifier les deux premiers tests selon le troisième exemple en utilisant `==`.  

#### Vérifier les tests  
\ 

Pour vérifier que la fonction renvoie bien les résultats attendus dans les tests, deux possibilités :

* l'une dans le Shell en saisissant : `import doctest` puis `doctest.testmod()`. Si les tests sont satisfaits, cela renvoie *TestResults(failed=0, attempted=0)* et cela signifie que tout va bien ! **Faites-le !**
* la seconde, en fin de script en ajoutant après la dernière ligne :
```python
def calcul_distance(vitesse, duree):
  ...
  return distance
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)
```  
Enregistrer les modifications et observer le résultat : si la dernière ligne est *Test passed* c'est que les tests sont validés, sinon, il faut lire les lignes précédentes pour détecter les tests insatisfaits.  

#### Remarques  
* Si des tests ne sont pas satisfaits, cela signifie uniquement que la fonction ne renvoie pas la réponse attendue dans le test. La source peut venir de la fonction, mais cela peut aussi parfois venir du test.
* A la place de *verbose = True*, on peut mettre *verbose = False* pour que le doctest soit moins bavard en cas de succès des vérifications.
* Les tests doivent parcourir tous les cas de figures possibles afin de vérifier la robustesse du code.

#### Exercice  

1. Modifier _verbose = True_ en _verbose_ = False_ pour observer les modifications.
2. Modifier l'une des valeurs attendues par les trois tests pour observer l'affichage en cas d'erreurs.

# Résumé : comment écrire une fonction  
Lorsque l'on écrit une fonction, il est préférable de la rédiger dans cet ordre :  

* Commencer par la création de la fonction (l'instruction *pass* permet d'indiquer à la fonction de ne rien faire) :
```python
def nom_de_la_fonction(param1, param2, ...):
  pass
  return
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose = False)
```  
* **Ecrire la documentation complète avant même la première ligne de code** : ce que fait la fonction, précision concernant les paramètres, les valeurs retournées, les conditions d'utilisation, les effets de bord, les tests.
* Remplacer *pass* par les lignes de code.
* Corriger le code pour que la fonction corresponde aux attentes et que les tests passent tous.  

# Pour s'entraîner ...  
## Périmètre, surface et volume d'objets usuels  
_Dans le même script, vous allez créer autant de fonctions que de formules. Les fonctions seront correctement documentées en suivant l'ordre des questions._  

1. Choisir une formule de calcul de périmètre, d'aire, de volume ...
2. Ecrire la documentation complète de la fonction (doc et tests).
3. Ecrire le code de la fonction pour qu'elle retourne ce qui est attendu.  

Reproduire ce travail pour plusieurs formules.  

**Remarque :**  
Si besoin, le nombre $\pi$ s'obtient en important le module math (écrire `import math` avant les définitions de fonctions) puis, pour utiliser le nombre $\pi$, il suffit d'écrire `math.pi`  
Par exemple :
```python
import math

def ma_fonction():
    return 2 * math.pi
```
Cela renvoie la valeur de $2 \times \pi$.  

## Lancé d'un dé

Ecrire une fonction qui simule le lancé d'un dé.  

\   

Pour obtenir un nombre entier au hasard, comme pour le module math, importer le module `random` puis utiliser la fonction `random.randint` ou `random.randrange` (Saisir `help(random.randint)` et `help(random.randrange)` par exemple pour accéder à la documentation de la fonction pour en connaître la syntaxe et l'usage).  

# Comment cela se passe-t-il dans d'autres langages de programmation ?  
Calcul de la distance à partir de la vitesse et de la durée de parcours:  

La variable *vitesse* et la variable *duree* contiennent les valeurs respectives de la vitesse et de la durée de parcours.  

Voici la même fonction écrite dans différents langages de programmation, la documentation ayant été volontairement réduite :  

## En langage naturel (ce n'est pas un langage de programmation)  

```python
fonction(vitesse, duree)  
    d <- vitesse * duree
    renvoyer d
```

## En python  
```python
def calcul_distance(vitesse, duree):
    '''
    Cette fonction calcule la distance parcourue en fonction de la vitesse
    moyenne et de la durée de parcours données en paramètres.
    '''
    d = vitesse * duree
    return d
```

## En javascript  
```javascript
function calcul_distance(vitesse, duree){
  /*
  Cette fonction calcule la distance parcourue en fonction de la vitesse
  moyenne et de la durée de parcours données en paramètres.
  */
  var d = vitesse * duree ;
  return d ;
}
```

## En C ou C++
```c
float calcul_distance(float vitesse, float duree){
  /*
  Cette fonction calcule la distance parcourue en fonction de la vitesse
  moyenne et de la durée de parcours données en paramètres.
  */
  float d = vitesse * duree ;
  return d ;
}
```  

## Exercice  
Dans un tableau à trois colonnes (python, javascript, C), écrire les différences et les points communs à la structure des fonctions ci-dessus dans les différents langages de programmation proposés.  

**Source**  

C’est quoi un langage de programmation ?. *Culture informatique* [en ligne]. Page créée le 31 août 2017 [consultée le 19 août 2019]. [https://www.culture-informatique.net/cest-quoi-langage-de-programmation/](https://www.culture-informatique.net/cest-quoi-langage-de-programmation/)