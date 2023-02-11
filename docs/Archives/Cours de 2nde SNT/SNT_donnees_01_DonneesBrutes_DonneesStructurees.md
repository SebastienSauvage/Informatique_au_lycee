---
title: "Thème Les donnees structurées et leur traitement - Chapitre 1 : Des données brutes aux données structurées"
author: [Sébastien SAUVAGE]
date: "04/10/2022"
keywords: [SNT, données structurées]
discipline: SNT
...
[^OGI]: Wikipédia. _Open Government Initiative_ [en ligne]. 2010-2019 [consulté le 12 août 2019].
[^OGI_image]: [https://upload.wikimedia.org/wikipedia/commons/3/32/Opengov.png](https://upload.wikimedia.org/wikipedia/commons/3/32/Opengov.png)
[^Def_donneesperso]: Wikipédia. _Données personnelles_ [en ligne]. 2006-2019 [consulté le 13 août 2019].  
[https://fr.wikipedia.org/wiki/Données_personnelles#étendue_de_la_notion_de_donnée_à_caractère_personnel](https://fr.wikipedia.org/wiki/Données\_personnelles\#étendue\_de\_la\_notion\_de\_donnée\_à\_caractère\_personnel)
[^FormatsFichiers]: Auteur de l'image : [Mohamed HASSAN](https://pixabay.com/fr/users/mohamed_hassan-5229782/), sous licence [Pixabay](https://pixabay.com/fr/service/terms/)
[^métadonnées]: [https://www.larousse.fr/dictionnaires/francais/métadonnée/186919](https://www.larousse.fr/dictionnaires/francais/métadonnée/186919)
[^ExempleVCard]: Wikipédia. _VCard_ [en ligne]. 2006-2019 [consulté le 14 août 2019]. [https://fr.wikipedia.org/wiki/VCard](https://fr.wikipedia.org/wiki/VCard}
[^vcard_wiki]:[https://fr.wikipedia.org/wiki/VCard#Propriétés]([https://fr.wikipedia.org/wiki/VCard#Propriétés])

\huge \textbf{Thème 4 : Les données structurées et leur traitement}\normalsize  

\ 

\Large \textbf{Chapitre 1 : Des données brutes aux données structurées}\normalsize

\ 

# Repères historiques
**2009** : **Open Government Initiative**[^OGI] du président Obama. ![Open Government Initiative](./SNT_donnees_01_DonneesBrutes_DonneesStructurees_Opengov.png)[^OGI_image]\ \   

**2013** : Charte du G8 pour l'**ouverture des données publiques**.  

# Premières données : les données à caractère personnel
## Définition[^Def_donneesperso]
**Une donnée à caractère personnel** (couramment "données personnelles") correspond, en droit français, à toute information relative à une personne physique identifiée ou qui peut être identifiée, directement ou indirectement, par référence à un numéro d'identification ou à un ou plusieurs éléments qui lui sont propres.  

Sont considérées comme des données à caractère personnel des informations directement nominatives telles que le nom, le prénom, la photographie du visage, mais aussi indirectement nominatives, telles que la date et le lieu de naissance, l'adresse du domicile, l'adresse électronique, le pseudonyme ou le numéro de téléphone, qui peuvent être reliées à la personne par recoupement d'informations. Une adresse IP est également considérée comme une donnée à caractère personnel, qu'elle soit fixe ou dynamique.  

Ces données peuvent être objectives, comme le groupe sanguin, le numéro de sécurité sociale ou de carte bancaire, ou subjectives, comme des avis ou des appréciations sur la personne concernées, lesquels n'ont même pas besoin d'être vrais.  

Ces données, comme tous les types de données sont protégées et soumises au droit national. Nous aborderons cet aspect lors du chapitre 3 de ce thème.  

## Exercice
Selon cette définition, citer d'autres exemples de données personnelles objectives et de données personnelles subjectives.  
\   
Données personnelles objectives : ............................................................................................................  
\   
Données personnelles subjectives : ...........................................................................................................  

# Les formats de données
## Différentes données, différents formats
Il existe de nombreux **types de données** : les données personnelles, mais aussi, la musique, les images, la vidéo, les pages web, les tableaux, les documents textuels, les présentations, les programmes exécutables, ...  

Ces données peuvent se présenter sous différents formats. Par exemple, _un document texte_ peut être au format `TXT`, `RTF`, `DOC`, `DOCX`, `ODT`, ...  

## Exercice
L'image ci-dessous indique différents formats de fichiers.  

![Différents formats de fichiers](./SNT_donnees_01_DonneesBrutes_DonneesStructurees_FormatsFichiers.jpg)[^FormatsFichiers]\ \   

1. Classer, si possible, les formats par type de fichiers.  
\   
Fichiers images : .............................................................................................................................  
\   
Fichiers multimédia : .........................................................................................................................  
\   
Fichiers de programmation : ...................................................................................................................  
\   
Autres : ......................................................................................................................................  

2. Trouver d'autres formats pour la plupart de ces types de fichiers.  
\   
Fichiers images : .............................................................................................................................  
\   
Fichiers multimédia : .........................................................................................................................  
\   
Fichiers de programmation : ...................................................................................................................  

3. Proposer quelques formats de fichiers musicaux.  
\   
....................................................................................................................................  
\   
....................................................................................................................................  

## Formats propriétaires ou libres, fermés ou ouvertes
### Exercice
Voici trois articles sur le web :  

- [https://www.halpanet.org/content/formats-libres-propri-taires](https://www.halpanet.org/content/formats-libres-propri-taires)
- [https://doranum.fr/wp-content/uploads/FS2_formats_ouverts_fermes_V1.pdf](https://doranum.fr/wp-content/uploads/FS2\_formats\_ouverts\_fermes\_V1.pdf)
- [https://fr.wikipedia.org/wiki/Correspondance_entre_formats_ouverts_et_formats_fermés](https://fr.wikipedia.org/wiki/Correspondance\_entre\_formats\_ouverts\_et\_formats\_fermés)   

1. Lire les trois articles.
2. A l'aide de ces trois documents, résumer, sous forme de tableau par exemple, les différences entre les formats propriétaire et fermés, les formats propriétaires et ouverts, les formats libres et ouverts.  
\   
\   
\   
\   
\   
\   
\   
\   
\   
\   
\   
\   
\   
\   

3. Pourquoi n'existe-t-il pas de format libre et fermé ?  
\   
....................................................................................................................................  
\   
....................................................................................................................................  

4. Citer un exemple de format de données audio de chacun des trois types de format cités précédemment.  
\   
Fermé et propriétaire : ............................................................................................................  
\   
Ouvert et propriétaire : ...........................................................................................................  
\   
Ouvert et libre : ..................................................................................................................  

## Les métadonnées
### Définition
**Une métadonnée** est une donnée servant à caractériser une autre donnée, physique ou numérique : Les métadonnées sont à la base de l’archivage.[^métadonnées]  

Par exemple, pour un fichier de type vidéo, cela peut être le titre du film, la date de création du fichier, la résolution de l'image, le débit du son, ...  

Evidemment, les métadonnées sont elles-mêmes des données !  

### Intérêts
Les métadonnées sont des plus-values non négligeables pour un utilisateur, une entreprise, ...  

Les intérêts sont multiples :  

- **Faciliter l'accès à l'information** : sans connaissance particulière, cela permet d'accéder à des informations sur la donnée initiale ;
- **évaluer la donnée** : on accède facilement à la qualité des données (résolution d'une vidéo, date de la prise d'une photo, ...). _Pratique pour savoir si un agrandissement d'une photo de copain prise la veille peut être agrandie et de bonne qualité avant même son impression_ ;
- **gain de temps** : on peut filtrer des données par leurs métadonnées et ainsi obtenir rapidement des données correspondant à un besoin particulier._Par exemple, on peut faire une recherche de fichiers musicaux de son chanteur préféré sans devoir parcourir l'ensemble des dossiers d'un disque dur_ ;
- **l'exploitation de données "oubliées"** : l'existence de métadonnées permet d'utiliser des données, cela permet le traitement de ces données. _Ca n'est pas pratique par exemple d'écouter des fichiers musicaux nommés "piste 1", "piste 2", ... Ces fichiers sont rarement (jamais ?) écoutés_ ;
- **...**

### Exercice
1. Se rendre sur le site de musique libre \href{https://www.auboutdufil.com/}{https://www.auboutdufil.com/} et y choisir un fichier musical au choix. Sur la gauche, des filtres permettent d'obtenir des musiques selon le genre, l'usage ou l'humeur.  (Eviter de passer 3 heures à faire son choix ou de copier sur le voisin ...)
2. Avez-vous le droit de télécharger ce morceau musical ? Si oui, à quelles conditions ?  
\   
....................................................................................................................................  
\   
....................................................................................................................................  

3. Télécharger le fichier musical choisi et le placer dans votre espace personnel, correctement organisé.
4. Déterminer l'ensemble des métadonnées liées à la musique que vous avez téléchargée.
5. Quelles sont les métadonnées saisies par l'utilisateur et quelles sont les métadonnées ajoutées par des logiciels ?  
\   
Exemples de métadonnées saisies par l'utilisateur : ................................................................................  
\   
Exemples de métadonnées ajoutées par les logiciels : ...............................................................................  

6. Dans les métadonnées du fichier, compléter le genre de votre morceau de musique ou d'autres métadonnées éventuelles.
7. Proposer une manière de présenter l'ensemble des réponses des élèves de la classe.  
\   
....................................................................................................................................  

# Structuration de données
## Un premier exemple : synthèse des réponses de l'exercice précédent
### Exercice
Se rendre sur le tableur collaboratif en ligne [https://lite.framacalc.org/9m8w-snt-metadonnees](https://lite.framacalc.org/9m8w-snt-metadonnees) et compléter une ligne du tableau avec les métadonnées de votre fichier musical de l'exercice précédent.  

## Descripteurs et valeurs de données
Afin de décrire et d'organiser un ensemble de données, il est nécessaire de donner des "noms" pour indiquer à quoi correspond chaque donnée. Dans l'exercice précédent, par exemple, si le morceau est _Stop One More Time Remix 2011_ de Ghost k, "titre" est **un descripteur** et "Stop One More Time Remix 2011" est **une valeur** de ce descripteur.  

Lorsque l'on dispose d'une ou plusieurs bases de données, les descripteurs permettent ainsi de pouvoir filtrer, classer l'ensemble des données et ainsi répondre à un besoin particulier. Dans notre base de données musicale, nous pouvons alors filtrer par exemple les morceaux musicaux choisis par la classe de l'année 2011 ("année" est le descripteur, "2011" en est une valeur), puis les trier dans l'ordre alphabétique des titres ("titre" est le descripteur). Nous verrons ces manipulations lors du deuxième chapitre.  

## Exercice
1. Donner la liste des descripteurs des données récoltées par la classe sur l'ensemble des fichiers musicaux.  
\   
....................................................................................................................................  
\   
....................................................................................................................................  

2. Donner une valeur pour chacun des descripteurs de notre base de données.  
\   
....................................................................................................................................  
\   
....................................................................................................................................  
\   
....................................................................................................................................  
\   
....................................................................................................................................  
\   
....................................................................................................................................  
\   
....................................................................................................................................  

Afin de pouvoir assurer une comptabilité des structures de données d'un ordinateur à l'autre, d'une entreprise à l'autre, il existe des conventions et des modèles pour des données usuelles. En effet, il est plus simple pour deux entreprises partenaires qui échangent des données de pouvoir les traiter rapidement sans devoir modifier d'abord la manière dont elles sont structurées. Cela permet aussi parfois d'être indépendant des logiciels utilisés pour les exploiter.  

## Un deuxième exemple : le format VCard
### Description du format
Le format VCard est un format standard de carte de visite électronique. Ce format est reconnu à la fois par l'application "contacts" des téléphones portables (ce qui permet de transmettre par exemple le numéro de téléphone à un camarade par sms sans devoir tout saisir, quel que soit les modèles de téléphones), les sites et logiciels de messagerie (pour les coordonnées mail et autres informations des contacts), les agendas électroniques, ...  

Les fichiers au format `VCard` ont pour suffixe `VCF` : _ma\_carte\_de\_visite\_electronique.vcf_  

Voici un exemple de contenu d'un fichier au format VCard[^ExempleVCard] :  

```VCARD
BEGIN:VCARD  
VERSION:4.0  
N:Gump;Forrest;;Mr.;  
FN:Forrest Gump  
ORG:Bubba Gump Shrimp Co.  
TITLE:Shrimp Man  
PHOTO;MEDIATYPE=image/gif:http://www.example.com/dir_photos/my_photo.gif  
TEL;TYPE=work,voice;VALUE=uri:tel:+1-111-555-1212  
TEL;TYPE=home,voice;VALUE=uri:tel:+1-404-555-1212  
ADR;TYPE=WORK;PREF=1;LABEL="100 Waters Edge Baytown, LA 30314\nUnited States of America":;;100 Waters Edge;Baytown;LA;30314;United States of America  
ADR;TYPE=HOME;LABEL="42 Plantation St. Baytown, LA 30314 United States of America":;;42 Plantation St.;Baytown;LA;30314;United States of America  
EMAIL:forrestgump@example.com  
REV:20080424T195243Z  
x-qq:21588891  
END:VCARD  
```

Il faut bien respecter la structure :  

- les lignes `BEGIN:VCARD`, `END:VCARD` ainsi que les descripteurs `VERSION`, `N` et `FN` sont obligatoires ;
- utiliser les bons noms pour les descripteurs (exemple, "EMAIL"), écrits en majuscules ;
- respecter la syntaxe : "`:`" collé au descripteur, utilisation correcte des "`;`", ...

Ne pas hésiter à lire la page wikipédia sur le format VCard[^vcard_wiki] pour compléter ce qui est écrit ci-dessus.  

Il existe d'autres formats dérivés du format `VCard` pour les cartes de visite électronique : `XCard` par exemple répondant à une autre structure ...  

### Exercice
Certains logiciels (payants ou gratuits) proposent de vous créer votre VCard, mais est-ce vraiment utile quand on a compris le principe ?  

1. Ouvrir un éditeur de texte simple : blocnote, notepad, atom, mousepad, ...
2. Sauvegarder tout de suite votre fichier vide sous la forme \texttt{NOM\_Prenom.vcf} dans votre espace de travail de SNT.
3. Saisir votre carte de visite électronique :
- sans forcément indiquer vos réelles données personnelles.
- en respectant la structure du format VCF.
- Vous n'êtes pas obliger le remplir tous les champs de l'exemple.
- Vous ajouterez un ou plusieurs champs supplémentaires (voir le lien wikipédia ci-dessus par exemple).
- Sauvegarder votre fichier et fermer le logiciel.

\   

\   

**Sources**  

- Wikipédia. _Open Government Initiative_ [en ligne]. 2010-2019 [consulté le 12 août 2019].  
[https://fr.wikipedia.org/wiki/Open_Government_Initiative](https://fr.wikipedia.org/wiki/Open\_Government\_Initiative)
- Wikipédia. _Données personnelles_ [en ligne]. 2006-2019 [consulté le 13 août 2019].  
[https://fr.wikipedia.org/wiki/Données_personnelles#étendue_de_la_notion_de_donnée_à_caractère_personnel](https://fr.wikipedia.org/wiki/Données\_personnelles\#étendue\_de\_la\_notion\_de\_donnée\_à\_caractère\_personnel)
- Dictionnaire Larousse. _Définition d'une métadonnée_ [en ligne]. [consulté le 13 août 2019].  
[https://www.larousse.fr/dictionnaires/francais/métadonnée/186919](https://www.larousse.fr/dictionnaires/francais/métadonnée/186919)
- Wikipédia. _VCard_ [en ligne]. 2006-2019 [consulté le 14 août 2019].  
[https://fr.wikipedia.org/wiki/VCard](https://fr.wikipedia.org/wiki/VCard)
- Open Knowledge Foundation Blog. _Defining Open Data_ [en ligne]. 3 octobre 2013 [consulté le 14 août 2019].  
[https://blog.okfn.org/2013/10/03/defining-open-data/](https://blog.okfn.org/2013/10/03/defining-open-data/)
