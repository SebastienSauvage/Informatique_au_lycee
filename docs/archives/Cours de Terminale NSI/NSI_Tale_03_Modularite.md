---
title: "Thème 4 - Chapitre 2 : Modularité"
author: [Sébastien SAUVAGE]
date: "28/09/2022"
keywords: [NSI, terminale, programmation, modularité]
discipline: NSI
---
[^GéoDataMine]: [https://geodatamine.fr](https://geodatamine.fr)
[^Openstreetmap_France]: [https://www.openstreetmap.fr/](https://www.openstreetmap.fr/)

\huge \textbf{Thème 4}\normalsize  

\ 

\Large \textbf{Chapitre 2 : Modularité}\normalsize  

# Introduction
**Exercice**  

Dans cet exercice, l'ensemble des fichiers `PY` seront placés dans le même dossier.  

On considère une suite géométrique de raison $q$ ($q >1$) et de premier terme $U_0$, positif, donnés.  

On note $S_n$ la somme $U_0 + U_1 + \ldots + U_n$.  

1. \   
    a. On sait (pour ceux qui ont suivi la spécialité Mathématiques en première) que pour tout entier naturel $n$, $U_n = U_0 \times q^n$.  
    
        En vous appuyant sur cette définition, écrire, en langage Python, dans un fichier nommé `terme3.py` une fonction `terme`.  

        Cette fonction aura trois paramètres : $q$, la raison (type `float`), $u$, la valeur du premier terme (type `float`) et $n$,le rang de la suite dont on cherche la valeur (type `integer`).  
        
        Cette fonction retournera la valeur de $U_n$ (type `float`).  

        Par exemple, `terme(2, 1, 5)` signifie que l'on cherche le terme $u_5$, lorsque $q = 2$ et $u_0 = 1$. Cette instruction renvoie 32.  

        Ainsi :  

        ```python
        >>> terme(2, 1, 5)
        32
        ```

        Vous penserez à bien documenter votre fonction ...
    b. On sait également (toujours pour les mêmes raisons), que $S_n = U_0 \times \dfrac{1 - q^{n + 1}}{1 - q}$.  
        
        En vous appuyant sur cette définition, écrire, en langage Python, dans un fichier nommé `somme3.py`, une fonction `somme`.  

        Cette fonction a trois paramètres : `q`, la raison (type `float`), `u`, la valeur du premier terme (type `float`) et `n`, le rang de la somme dont on cherche la valeur (type `integer`).  

        Cette fonction renvoie la valeur de $S_n$ calculée selon la formule ci-dessus.  

        Par exemple, `somme(2, 1, 5)` renvoie 63.
    c. On considère un nombre $A$ réel. Ecrire, en langage Python, dans un fichier nommé `calcul_de_seuil.py` une fonction `seuil`.  

        Cette fonction aura trois paramètres, tous de type `float` : `A`, la valeur du seuil à atteindre , `q`, la raison de la suite géométrique et `u`, la valeur du premier terme de la suite.  

        La fonction retournera alors la première valeur $n$ du rang de la suite pour lequel la somme $S_n$ est strictement supérieure à $A$.  
        
        Par exemple, `seuil(60, 2, 1)` renvoie 5.  

        Comme la fonction nécessitera les calculs des sommes $S_n$, il sera nécessaire de commencer le programme par `import somme3 as mod1` et ensuite d'utiliser la fonction `mod1.somme`.
2. \   
    a. En considérant uniquement que $U_{n + 1} = q \times U_n$, écrire deux fonctions, nommées `terme`, répondant aux mêmes contraintes que la fonction `terme` de la question 1.a., l'une utilisant une boucle, l'autre étant une fonction récursives.  

        Sauvegarder les deux fonctions dans deux fichiers différents nommés `terme1.py` et `terme2.py`.
    b. En considérant uniquement que $S_n = U_0 + U_1 + \ldots + U_n$, écrire deux fonctions `somme`, l'une utilisant une boucle, l'autre étant une fonction récursives répondant au même contraintes que la fonction `somme` de la question 1.b..  

        Sauvegarder les deux fonctions dans deux fichiers différents nommés `somme1.py` et `somme2.py`  

        Ces deux fonctions feront appel à l'une des fonctions `somme`, précédemment écrite.
3. \   
        - Que se passe-t-il en changeant la première ligne `import somme3 as mod1` par `import somme1 as mod1` ou `import somme2 as mod1` ?  
        - Procéder de même au sein des fichiers contenant les fonctions `somme` nécessitant l'importation de la fonction `terme`.  
        - Conclusion : quelles sont les éléments nécessaires à connaître pour coder une fonction ?

# Modularité
Un programme écrit en Python ou en Java commence souvent par des lignes de type `import ...`, en C++ par `include ...`.  

Il s'agit de fonctions déjà écrite (par soi-même ou une autre personne) dont nous souhaitons disposer pour un projet donné.  

**Définition**  

Un module est un fichier regroupant un ensemble de fonctions écrites auparavant dans un langage donné dans le but d'être réutilisées par d'autres programmes.  

# Modules
En Python, un module peut être un simple fichier. Ce fichier contient principalement des définitions de fonctions et de constantes destinées à être utilisées à l'aide d'une documentation. Il n'y a pas besoin de savoir comme les fonctions sont codées, mais il est nécessaire de connaître la façon de les utiliser et ce qu'elles produisent. Pour créer un module, il suffit donc d'écrire ces définitions dans un fichier dont le nom a pour extension `PY`.  

\   

## Exercice
Recopier et compléter le module ci-dessous, appelé `aires`, contenant quatre fonctions : `disque`, `rectangle`, `carre` et `triangle` permettant de calculer les aires des figures géométriques fréquemment rencontrées au collège.  

```python
'''
Ce module contient différentes fonctions permettant de calculer les aires des figures usuelles
vues collège.
'''
... #  <--- A compléter

def disque(...): #  <--- A compléter
    ... #  <--- A compléter

def rectangle(longueur: float, largeur: float) -> float:
    '''
    Fonction qui renvoie l'aire d'un rectangle dont la longueur et la largeur
    sont passées en paramètres.
    :param:
    longueur, largeur : longueur de deux côtés consécutifs du rectangle
    :effets de bord:
    aucun
    :exemple:
    >>> rectangle(5, 6) == 30
    True
    '''
    assert (longueur >= 0) and (largeur >= 0), "longueur et largeur doivent être des nombres positifs"
    return ... #  <--- A compléter
    
... #  <--- A compléter
```

## Exemple d'utilisation
Ainsi, maintenant, pour utiliser les fonctions du module `aires`, il suffit de saisir `import aires`.  

Dans le terminal, on peut utiliser le module de la manière suivante :  

```python
>>> import aires
>>> aires.rectangle(5, 9)
45
```

## Astuces
Le contenu d'un module s'obtient à l'aide de l'instruction `dir`.  

La documentation d'une fonction s'obtient à l'aide de l'instruction `help`.

## Exemple
Dans le terminal, on peut donc obtenir les documentations :  

```
>>> import test
>>> dir (test)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__',
 '__spec__', 'carre', 'disque', 'rectangle', 'triangle']
>>> help(test.rectangle)
Help on function rectangle in module test:

rectangle(longueur: float, largeur: float) -> float
    Fonction qui renvoie l'aire d'un rectangle dont la longueur et la largeur
    sont passées en paramètres.
    :param:
    longueur, largeur : longueur de deux côtés consécutifs du rectangle
    :effets de bord:
    aucun
    :exemple:
    >>> rectangle(5, 6) == 30
    True

```

# Bibliothèques
## Définitions
**Un package** est un ensemble de modules.  

**Une bibliothèque** est un ensemble de un ou plusieurs packages.  

## Exemples

- La bibliothèque `Matplotlib` contient différents modules : `pylab`, `pyplot`, ...  
Pour appeler l'un des module, il suffit d'écrire : `import matplotlib.pylab` par exemple.
- `Numpy` et `Scipy` sont des bibliothèques pour le calcul scientifique ;
- `PIL` est une bilbiothèque pour la manipulation et le traitement d'images ;
- `Pygame` est une bibliothèque pour la création de jeux en 2D ;
- `Django` est une bibliothèque pour le développement WEB.

# API
## Définition
### Définition
**Une API (_Application Programming Interface_)** est une interface de programmation d'application.  

Elle est destinée à être utilisée par des programmes. Le principe de ce type d'interface est le même que celui des UI (_User Interface_) ou des GUI (_Graphical User Interface_) destinées, elles, à un utilisateur humain.

### Remarque
Le principe de base est que le fonctionnement interne, la logique sous-jacente, n'a pas besoin d'être connue du programme utilisateur. Par contre, cela nécessite une documentation fournie décrivant son utilisation.  

### Définition
**Une interface** est ce qu'il suffit de connaître d'une fonction, d'une classe, etc pour pouvoir l'utiliser.  

### Propriété
En général, l'interface d'une fonction est constituée de :  

- Son nom ;
- ses paramètres : leur sens et leur type ;
- le type de ce qui est renvoyé en sortie, effets de bord compris.

### Exemple
Pour la fonction `rectangle` du module `aires`, son interface est donnée par :  

- NOM : `rectangle` ;
- Paramètres : `longueur` et `largeur` de type `float` tous les deux correspondant aux dimensions du rectangle ;
- Renvoie, sans effet de bord : l'aire du rectangle, objet de type `Float`.

### Astuce
L'interface d'une fonction est la première chose à déterminer (donc écrire sa documentation) avant l'écriture du code, afin d'être bien certain des attentes de celui qui l'utilisera dans le but de répondre à ses souhaits.  

## La variable `__name__`
Dans chaque module, une variable `__main__` est créée automatiquement à l'exécution d'un programme. Cette variable contient le nom du programme courant quand on importe un programme. Mais le nom du programme principal est toujours `__main__`. Donc la fonction `main` est exécutée seulement si le fichier module constitue le programme principal.  

Afin de n'exécuter un code que lorsque le module est le programme principal, il suffit d'ajouter en fin de module les lignes :  

```python
if __name__ == '__main__':
    ... # <--- Partie des instructions à n'exécuter que si le module est le programme principal.
```

## Les API Web
Il existe différents types d'API. Parmi elles, **les API Web** sont les plus nombreuses. Les réseaux sociaux par exemple, proposent des API permettant d'accéder à des données. Pour ce type d'API, les demandes ne sont pas codées dans le même langage que le code de l'API. Une méthode est d'**émettre une requête vers un serveur distant qui renvoie alors les données demandées**. De nombreux services Web proposent ainsi des API basées sur le protocole HTTP et utilisent le réseau. Il suffit donc d'utiliser n'importe quel langage capable d'envoyer une requête HTTP pour accéder au service Web.  

Les API disponibles sur le Web peuvent être libres et gratuites ou payantes. Celles qui sont libres peuvent nécessiter une clé d'authentification.  

Par exemple, on trouve sur la page [http://openweathermap.org/api](http://openweathermap.org/api) diverses API concernant le climat et la météo. La plupart sont payantes mais _Current weather data_ est gratuite. Elle nécessite cependant de s'enregistrer pour obtenir une clé d'authentification.  

\   

Quelques sites intéressants à visiter :  

- [https://fr.openfoodfacts.org/data](https://fr.openfoodfacts.org/data) qui se revendique "_base de données collaborative, libre et ouverte des produits alimentaires du monde entier_".
- [https://www.openstreetmap.fr](https://www.openstreetmap.fr) où se trouve le site OpenStreetMap France.
- [https://api.gouv.fr/rechercher-api](https://api.gouv.fr/rechercher-api) référence plusieurs API disponibles et gratuites, en particulier l'API `Géo` :  

    - à l'adresse [https://api.gouv.fr/api/api-geo](https://api.gouv.fr/api/api-geo) on trouve une description ;
    - à l'adresse [https://geo.api.gouv.fr/decoupage-administratif](https://geo.api.gouv.fr/decoupage-administratif) la documentation technique.  

Pour effectuer des requêtes en langage Python, le plus simple est d'utiliser une bibliothèque comme `requests`, installable par exemple via la commande `pip install requests`.  

Après importation de la bibliothèque, afin de récupérer des données, il faut émettre une requête de type `get` :  

```python
>>> import requests
>>> rep = requests.get('https://www.education.gouv.fr/test')
```

Afin de connaître le code réponse à la requête, un affichage de la variable `rep` suffit, mais on peut aussi utiliser `rep.status_code` qui renvoie uniquement la valeur du code réponse à la requête :  

```python
>>> rep
<Response [404]>
>>> rep.status_code
404
```

Ici, le code 404 signifie que la page n'existe pas !  

\newpage

Les types de code réponses les plus fréquents à une requête GET sont :  

- 200 : tout est ok, le résultat est renvoyé ;
- 301 : le serveur est redirigé vers une autre adresse ;
- 400 : la requête ne semble pas correcte pour le serveur ;
- 401 : il y a un problème d'authentification ;
- 403 : l'accès à la ressource n'est pas autorisée ;
- 404 : la ressource n'a pas été trouvée.

Voici une requête valide pour obtenir le nom, le code et la population des communes du département 59 (voir la documentation précédemment citée) :  

```python
>>> import requests
>>> url = """https://geo.api.gouv.fr/departements/59/communes?fields=nom,code,population&format=json"""
>>> rep = requests.get(url)
>>> rep
<Response [200]>
>>> rep.status_code
200
```

Les données renvoyées sont au format `JSON`. Pour les afficher, la méthode `json` produit une liste de dictionnaires dont nous n'affichons que les quatre premiers éléments :  

```python
>>> rep.json()
[{'nom': 'Abancourt', 'code': '59001', 'population': 469}, 
{'nom': 'Abscon', 'code': '59002', 'population': 4309}, 
{'nom': 'Aibes', 'code': '59003', 'population': 372}, 
{'nom': 'Aix-en-Pévèle', 'code': '59004', 'population': 1320},
...
```

## Exercice
Effectuer une recherche des communes du Nord par code postal puis une seconde recherche de ces mêmes villes par coordonnées géographiques.  

\   


\   

Une autre API avec GéoDataMine [^GéoDataMine] permet d'extraire des données de OpenStreetMap France [^Openstreetmap_France] :  

```python
>>> import requests
>>> url = """https://geodatamine.fr/boundaries"""
>>> rep = requests.get(url)
>>> data = rep.json()
>>> for d in data:
        k = d['name']
        if k =='Douai':
            print(d)
        
{'id': -1643921, 'name': 'Douai', 'ref': '593', 'type': 'admin_7'}
{'id': -56243, 'name': 'Douai', 'ref': '59178', 'type': 'admin_8'}
{'id': -4260196, 'name': 'Douai', 'ref': '5915', 'type': 'political'}
```

On peut utiliser alors l'identifiant obtenu -56243, par exemple, pour trouver par exemple les bibliothèques à Douai :  

```python
>>> url = '''https://geodatamine.fr/data/library/-56243?format=geojson'''
>>> rep = requests.get(url)
>>> rep.json()
{'type': 'FeatureCollection', 'name': 'sql_statement', 'crs': {'type': 'name', 'properties': {'name': 'urn:ogc:def:crs:OGC:1.3:CRS84'}}, 'features': [{'type': 'Feature', 'properties': {'osm_id': 'node/1584907282', 'type': 'library', 'name': 'Bibliothèque Municipale', 'ref_isil': None, 'operator': None, 'wheelchair': None, 'opening_hours': None, 'com_insee': '59178', 'com_nom': 'Douai'}, 'geometry': {'type': 'Point', 'coordinates': [3.0736988, 50.367642999371625]}}, {'type': 'Feature', 'properties': {'osm_id': 'way/101423464', 'type': 'library', 'name': 'Bibliothèque La Micheline', 'ref_isil': None, 'operator': None, 'wheelchair': None, 'opening_hours': None, 'com_insee': '59178', 'com_nom': 'Douai'}, 'geometry': {'type': 'Polygon', 'coordinates': [[[3.081319, 50.35417699937445], [3.081369, 50.35411399937449], [3.081567, 50.35418099937446], [3.081515, 50.35424399937444], [3.081319, 50.35417699937445]]]}}, {'type': 'Feature', 'properties': {'osm_id': 'way/101636376', 'type': 'library', 'name': 'Bibliothèque La Péniche', 'ref_isil': None, 'operator': None, 'wheelchair': None, 'opening_hours': None, 'com_insee': '59178', 'com_nom': 'Douai'}, 'geometry': {'type': 'Polygon', 'coordinates': [[[3.083737, 50.39405099936605], [3.083743, 50.39404799936606], [3.083822, 50.39399899936607], [3.083857, 50.39401699936608], [3.08385, 50.39402299936606], [3.08391, 50.39405499936606], [3.083843, 50.39410399936604], [3.083737, 50.39405099936605]]]}}]}
>>> rep.json()['features']
[{'type': 'Feature', 'properties': {'osm_id': 'node/1584907282', 'type': 'library', 'name': 'Bibliothèque Municipale', 'ref_isil': None, 'operator': None, 'wheelchair': None, 'opening_hours': None, 'com_insee': '59178', 'com_nom': 'Douai'}, 'geometry': {'type': 'Point', 'coordinates': [3.0736988, 50.367642999371625]}}, {'type': 'Feature', 'properties': {'osm_id': 'way/101423464', 'type': 'library', 'name': 'Bibliothèque La Micheline', 'ref_isil': None, 'operator': None, 'wheelchair': None, 'opening_hours': None, 'com_insee': '59178', 'com_nom': 'Douai'}, 'geometry': {'type': 'Polygon', 'coordinates': [[[3.081319, 50.35417699937445], [3.081369, 50.35411399937449], [3.081567, 50.35418099937446], [3.081515, 50.35424399937444], [3.081319, 50.35417699937445]]]}}, {'type': 'Feature', 'properties': {'osm_id': 'way/101636376', 'type': 'library', 'name': 'Bibliothèque La Péniche', 'ref_isil': None, 'operator': None, 'wheelchair': None, 'opening_hours': None, 'com_insee': '59178', 'com_nom': 'Douai'}, 'geometry': {'type': 'Polygon', 'coordinates': [[[3.083737, 50.39405099936605], [3.083743, 50.39404799936606], [3.083822, 50.39399899936607], [3.083857, 50.39401699936608], [3.08385, 50.39402299936606], [3.08391, 50.39405499936606], [3.083843, 50.39410399936604], [3.083737, 50.39405099936605]]]}}]
>>> rep.json()['features'][0]
{'type': 'Feature', 'properties': {'osm_id': 'node/1584907282', 'type': 'library', 
'name': 'Bibliothèque Municipale', 'ref_isil': None, 'operator': None, 'wheelchair': None,
 'opening_hours': None, 'com_insee': '59178', 'com_nom': 'Douai'}, 
 'geometry': {'type': 'Point', 'coordinates': [3.0736988, 50.367642999371625]}}
```
# Exercices
## Exercice
1. Créer un module `stats` qui contient deux fonctions `somme` et `moyenne`. Ces deux fonctions prennent en paramètre un objet de type `list` non vide. La fonction `somme` renvoie la somme des éléments de la liste et la fonction `moyenne` renvoie la moyenne des éléments de la liste.
2. Tester ce module en l'important dans un autre fichier où les deux fonctions sont utilisées.
3. Compléter ce module par d'autres fonctions statistiques : minimum, maximum, étendue, etc.

## Exercice
1. En utilisation la documentation du module nommé `statistics`, inclus dans la bibliothèque standard, trouver une fonction permettant le calcul de moyenne de plusieurs nombres ainsi qu'une fonction calculant la médiane.
2. Comment utiliser ces fonctions ? Ecrire plusieurs exemples.

## Exercice
Consulter le site à l'adresse [http://api.open-notify.org](http://api.open-notify.org) qui concerne l'ISS, la Station Spatiale Internationale.  

Ecrire des requêtes en langage Python pour obtenir :  

1. les personnes à bord de l'ISS ;
2. la position de l'ISS.

Les passages de l'ISS au dessus d'un point donné n'est plus disponible.  

\   

\   

\underline{{\textit{\textbf{Sources}}}}  

- Serge Bays, _numérique et sciences informatiques, Tle_, Ed. ellipses. p53 à 64, 88 et 89. ISBN 978-2-340-03844-8.