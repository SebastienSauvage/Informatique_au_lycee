---
title: "Thème Les donnees structurées et leur traitement - Chapitre 2 : Traitement des données structurées"
author: [Sébastien SAUVAGE]
date: "04/10/2022"
keywords: [SNT, données structurées]
discipline: SNT
...
[^ModeleRelationnel]:Wikipédia. _Modèle relationnel_ [en ligne]. 2012-2019 [consulté le 12 août 2019]. [wikipédia](https://fr.wikipedia.org/wiki/Modèle_relationnel}{https://fr.wikipedia.org/wiki/Modèle\_relationnel) (E.L.Codd) pour la structuration et l'indexation des bases de données.

\huge \textbf{Thème 4 : Les données structurées et leur traitement}\normalsize  

\ 

\Large \textbf{Chapitre 2 : Traitement des données structurées}\normalsize

\ 

# Repères historiques
**1970** : Invention du **modèle relationnel**[^ModeleRelationnel]  

**1979** : Création du **premier tableur VisiCalc**.

# Utilisation d'un site d'Open Data
## Qu'est-ce qu'une Open Data (données ouverte)
D'après l'**Open Knowledge Foundation** (O.K.F.), **une Open Data** est une donnée qui peut être librement utilisée, réutilisée et redistribuée par quiconque. Elle est seulement sujette, au plus, à une exigence d'attribution et de partage à l'identique sinon.  

Autrement dit, c'est une donnée qui est en libre accès. On peut la consulter, la télécharger, l'utiliser et la distribuer à d'autres librement. Selon les termes d'utilisation, il faut lors de son utilisation ou sa distribution indiquer l'auteur. On peut la modifier si les conditions d'utilisation le permettent ou les garder à l'identique.  

Quelques accès à des données ouvertes :  

- Portail des données ouvertes de l’UE : [https://data.europa.eu/euodp/fr/data](https://data.europa.eu/euodp/fr/data)
- Portail européen de données : [https://www.europeandataportal.eu/fr/homepage](https://www.europeandataportal.eu/fr/homepage)
- Plateforme ouverte des données publiques françaises : [https://www.data.gouv.fr/fr/](https://www.data.gouv.fr/fr/)
- Plateforme Open Data de l’Éducation nationale : [https://data.education.gouv.fr/pages/accueil/](https://data.education.gouv.fr/pages/accueil/)  

## Exercice
Tom Lefebvre habite les Hauts-de-France et son père vient d'obtenir une mutation dans la région de Bordeaux. Comme Tom se débrouille bien en informatique, ses parents lui demande de leur donner une liste des établissements susceptibles d'accueillir sa sœur qui est au collège. Pour cela, ils lui donne comme critères que ce soit une école publique dans la ville où ils sont susceptibles d'habiter. Dans cet exercice nous allons aider Tom ...  

1. Il faut accéder à la liste des établissements en France. Pour cela, nous allons utiliser les données ouvertes proposées par le Ministère de l'Education Nationale :
    - Se rendre sur le site Open Data de l'Education Nationale.
    - Indiquer "établissements" comme mot clé dans la zone de recherche.
    - Choisir les données nommées "Adresse et géolocalisation des établissements d'enseignement du premier et second degrés".
2. Avant d'utiliser des données en ligne, il faut s'assurer des droits d'utilisation de celles-ci. Cliquer sur l'onglet "Informations".
    a. Sous quelle licence se trouvent ces données ?  
    \   
    ....................................................................................................................................
    b. Dans le cas présent, peut-on :
        - utiliser les données pour sa propre information ? [] Oui - [] Non
        - copier (télécharger) les données ? [] Oui - [] Non
        - les transmettre telles quelles à quelqu'un ? [] Oui - [] Non
        - modifier les données ? [] Oui - [] Non
        - les transmettre si on les a modifiées ? [] Oui - [] Non
        - les vendre ? [] Oui - [] Non
    c. Pour les utilisations ci-dessus possibles, y a-t-il des conditions à respecter ?  
    \   
    ....................................................................................................................................
3. Nous allons maintenant filtrer les données afin d'obtenir uniquement celles qui nous intéressent. Sur la gauche, choisir les éléments suivants :
    - Secteur Public/Privé : `public` ; Localité d'acheminement : `Bordeaux` ; Nature : `collège`
4. Observer la liste les établissements qui répondent à la demande des parents de Tom. Inutile de recopier les informations. Il doit y en avoir sept ...

# Le format CSV
### Une base de données
**Exercice**  

Dans l'espace `public` de la classe, copier dans votre dossier personnel le fichier `liste_eleves_modifiee.csv`.  

**Le format `CSV`** est un format de fichier qui est libre et ouvert. Il permet ainsi avec des logiciels différents de pouvoir effectuer des traitements sur des données le contenant. A noter que le séparateur (ici, c'est un `;`) peut aussi être un autre caractère (comme `,` ou une tabulation).  

1. Ouvrir le logiciel **Bloc-Note** ou tout autre logiciel simple de traitement de texte.  
A l'aide du menu adéquat, ouvrir le fichier `liste_eleves_modifiee.csv`.
2. A quoi correspond la première ligne du fichier ?  
\   
........................................................................................................................................
3. En comparant la première ligne avec les suivantes, que remarquez-vous ?  
\   
........................................................................................................................................
4. Décrire le contenu d'un fichier au format CSV de manière succincte.  
\   
........................................................................................................................................  
\   
........................................................................................................................................  
\   
........................................................................................................................................  

Pour traiter des bases de données, il existe différents moyens, adaptés selon les besoins et la quantité de données à traiter.  Par exemple, si vous devez traiter une très grande quantité de données sans que l'aspect graphique soit important, il possible utiliser un script écrit par exemple en langage python pour gagner en efficacité, le temps de traitement étant très rapide. Si au contraire, la base de données est petite, l'usage d'une feuille de calcul peut être une solution. Il existe d'autres possibilités, comme l'usage d'un logiciel spécifique de traitement de base de données par exemple. Dans le cadre de l'enseignement SNT, nous allons voir comment exploiter une base de données à l'aide d'un script python et d'une feuille de calcul.

# Traitement de données avec un tableur
Lorsque la quantité de données n'est pas très importante, il est possible d'utiliser un tableur pour pouvoir exploiter les données.  

Avec ce type de logiciel, il est, par exemple possible d'afficher sous forme d'un tableau l'ensemble **des valeurs** de chaque **descripteur**, **trier** les valeurs selon un ou plusieurs critères, **filtrer** les valeurs pour ne retenir qu'une partie correspondante à des critères prédéfinis, enfin, tracer des graphiques pour représenter visuellement les valeurs.

## Ouvrir un fichier `CSV`
### Exercice

1. Executer un logiciel de type **tableur**, **LibreOffcie Calc** est parfait, mais on peut aussi utiliser d'autres logiciels gratuits, ou payants comme MsExcel.
2. Dans le menu **Fichier**, choisir **Ouvrir** ou simplement cliquer sur l'icône correspondant dans la barre d'outils.
3. **Décocher tabulation et virgule** puisque le séparateur, comme nous l'avons vu dans le paragraphe précédent est **le point-virgule** `;`.
4. Valider ensuite par **OK** pour obtenir une vue, sous forme de tableau, des données du fichier.  

## Observation des données affichées
### Exercice  

1. Où se trouvent les descripteurs ? Les valeurs correspondantes ?  
\   
........................................................................................................................................  
\   
........................................................................................................................................
2. Combien d'élèves sont répertoriés dans ce fichier ?  
\   
........................................................................................................................................
3. Quel est le nom du premier élève de la liste ? Quelle est la date de naissance du dernier ?  
\   
........................................................................................................................................  
\   
........................................................................................................................................  

## Trier
Comme les élèves ne sont pas classés pour le moment, nous allons dans un premier temps les trier.  

\   

**Exercice**  

1. Dans le menu **données**, choisir **trier**. Aller dans les **options** et cocher : la plage de données contient les étiquettes colonnes.
2. Par défaut, la **clé de tri** est le premier descripteur, ici c'est **nom**, ce qui est ce que l'on souhaite. L'ordre croissant permet d'être l'ordre alphabétique, ce qui nous convient également. Valider par **OK**.
3. Comment les élèves sont-ils triés ? Ce tri est-il convenable ?  
\   
.............................................................................................................................  
\   
.............................................................................................................................
4. Pour éviter une situation comme aux lignes 5 et 6 par exemple, il est nécessaire de classer les élèves avec le même patronyme selon l'ordre alphabétique de leur prénom. Pour cela, reprendre les questions _1._ et _2._ pour classer les élèves par ordre alphabétique selon leur nom puis, selon leur prénom en utilisant une **deuxième clé de tri**.
5. Améliorer encore le classement, en ajoutant comme troisième clé la `date de naissance`.
6. Classer l'ensemble des élèves selon l'ordre alphabétique de leur `option 1`, puis leur `option 2`, puis leur `option 3`, puis selon autre option et enfin selon leur `nom` et leur `prénom`.  
  
## Filtrer
Il est pratique, lorsque l'on dispose d'un fichier de données, de pouvoir filtrer les valeurs et n'en retenir que quelques unes.  

Pour cela, il suffit, dans le menu **données**, de choisir **autofiltre**. Un message demandant éventuellement si la première ligne est celle des descripteurs apparaît (valider si besoin).  

A ce moment-là, chaque cellule de la première ligne se voit affublé d'un petit triangle permettant de sélectionner le ou les critères retenus pour les valeurs de chaque descripteur.  

### Exercice
1. Dans le menu **données**, choisir **autofiltre**.
2. Trier les valeurs selon l'ordre alphabétique des `noms` puis `prénoms` puis `date de naissance`.
3. Filtrer les élèves ayant choisi `Italien` comme `option2`.
4. Parmi ces élèves, filtrer ceux qui ont choisi `Mathématiques` comme `option3`.
5. Retirer les deux filtres créés.
6. Filtrer les élèves faisant `Espagnol` en `option2`, `Mathématiques` ou `Sciences Economiques et Sociales` en `option3` et nés en `2002`.  

# Traitement de données à l'aide du langage Python
Nous allons dans ce paragraphe utiliser une base de données assez lourde concernant les établissements scolaires en France que nous allons d'abord télécharger au format `CSV`.  

## Une base de données
### Exercice
1. Rendez-vous sur la page de données ouvertes correspondant à notre base de données :  
[https://data.education.gouv.fr/explore/dataset/fr-en-annuaire-education/table/?disjunctive.nom_etablissement&disjunctive.type_etablissement&disjunctive.type_contrat_prive](https://data.education.gouv.fr/explore/dataset/fr-en-annuaire-education/table/?disjunctive.nom\_etablissement\&disjunctive.type\_etablissement\&disjunctive.type\_contrat\_prive)
2. Quelles sont les conditions d'utilisation de ces données (voir onglet **information**) ?  
\   
........................................................................................................................................  
3. L'onglet **Export** permet le téléchargement de la base de données dans différents formats. Quels sont ceux proposés ici ?  
\   
........................................................................................................................................  

4. Télécharger **le jeu de données entier** au **format `CSV`** et le placer correctement dans votre espace personnel de stockage.  

## Préambule
### Le module python `SNT_donnees`
**Exercice**  

Pour le traitement des données, une partie des scripts python ont déjà été écrits :  
Copier le module `SNT_donnees.py` situé dans le dossier public de la classe et le placer correctement dans votre espace personnel de stockage.  

### Logiciel Edupython
\textbf{Exercice}  

Pour traiter la base de données à l'aide d'un script écrit en langage python, nous allons utiliser le logiciel **Edupython**. Il en existe beaucoup d'autres, comme **IDLE**, **Thonny**, ...  

1. Executer le logiciel Edupython.
2. Sauvegarder tout de suite dans votre espace de travail le fichier vide sous le nom : `NOM_Prenom_traitement_donnees.py`.  

### Ouvrir la base de données
Saisir le script suivant :  

```Python
import SNT_donnees as snt_td

base = snt_td.lecture_base('fr-en-annuaire-education.csv')
```

**Attention à bien respecter la syntaxe et la mise en forme**. En particulier, `_` s'obtient avec la touche 8 au-dessus des touches U et I.  

Pour vérifier que la saisie est correcte, saisir dans le terminal/la console :  

```Python
>>> print(base[1])
('0351698F', 'Ecole primaire privée Ste Anne', 'Ecole', 'Privé', '4 rue de la Grotte de Freval', '', '35550 BRUC SUR AFF', '35550', '35045', 'Bruc-sur-Aff', '35', '14', '53', '1', '1', '', '', '', '0299344054', '', '', 'ec.0351698F@ac-rennes.fr', '1', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '77765937600019', '', '', '47.8154519202, -2.01896923152', "CONTRAT D'ASSOCIATION TOUTES CLASSES", 'Ille-et-Vilaine', 'Rennes', 'Bretagne', '324636.8', '6758050.8', 'EPSG:2154', "Circonscription d'inspection du 1er degré de Redon", '47.8154519202067', '-2.0189692315210532', 'Numéro de rue', '1972-05-03', '2019-08-26', 'OUVERT', "MINISTERE DE L'EDUCATION NATIONALE", '0', '0', '035017', '151', 'ECOLE DE NIVEAU ELEMENTAIRE')
```

### Afficher
**Le nombre de données**  

L'affichage des entêtes n'est pas implémentée dans le module python importé.  

Pour afficher le nombre de données dans notre base, il suffit d'ajouter la fonction suivante dans le script (penser à sauvegarder le fichier) :  

```Python
def nombre_donnees(bdd):
    nb = len (bdd) - 1
    return nb
```

**Attention à bien respecter la syntaxe et la mise en forme.** En particulier, les lignes décalées vers la droite commence par quatre espaces.  

Puis, saisir :  

```Python
>>> print(nombre_donnees(base))
```

**Les entêtes**  

Pour obtenir la liste des entêtes du fichier `CSV`, c'est à dire l'ensemble des descripteurs des données, saisir :  

```Python
>>> print(snt_td.affiche_entetes(base))
```

**Les données**  

Pour afficher les 3 premières lignes de données de la base, saisir :  

```Python
>>> snt_td.affiche_donnees(base, 3)
```

**Exercice**  
Afficher les 20 premières lignes de données de la base.  

### Filtrer
Evidemment, nous n'avons pas besoin de l'ensemble des informations de la base de données. Il faut donc limiter les données à celles correspondant à des critères de recherche.  

Par exemple, pour n'afficher que les établissements du Nord, il ne faut conserver que les données dont la valeur du descripteur `Code_departement` est `59`. Pour cela, saisir :  

```Python
>>> base_filtree = snt_td.filtrer_donnees(base, 'Code_departement', '59')
>>> snt_td.affiche_donnees(base_filtree)
```

On peut appliquer plusieurs filtres consécutifs pour effectuer une recherche multicritères. Par exemple, si on ne souhaite obtenir que les établissements publics du Pas-de-Calais, il faut filtrer selon le descripteur `Code_departement` (valeur : `62`) et le descripteur `Statut_public_prive` (valeur : `Public`). Pour cela, on procède en deux étapes en saisissant :  

```Python
>>> base_filtree1 = snt_td.filtrer_donnees(base, 'Code_departement', '62')
>>> base_filtree2 = snt_td.filtrer_donnees(base_filtree1, 'Statut_public_prive', 'Public')
>>> snt_td.affiche_donnees(base_filtree2)
```

**Exercice**  

1. Afficher uniquement les lycée généraux et technologiques publics du Nord.
2. Combien y en a-t-il ? (Ne pas les compter un par un ! Penser à utiliser une fonction vue dans l'un des paragraphes précédents)  

### Et après ?
Toujours à l'aide d'un script python, il est également possible, comme nous l'avons effectué avec le tableur de trier les valeurs selon un ou plusieurs descripteurs et de sauvegarder également ce tri dans un autre fichier.  

# Compléments
Pour compléter, vous pouvez lire les quelques articles en rapport avec les notions étudiées dans ce chapitre :  

- L’Open Data, l’ouverture des données pour de nouveaux usages [https://interstices.info/lopen-data-louverture-des-donnees-pour-de-nouveaux-usages/](https://interstices.info/lopen-data-louverture-des-donnees-pour-de-nouveaux-usages/)
- Calculer sur des données massives : [https://interstices.info/calculer-sur-des-donnees-massives/](https://interstices.info/calculer-sur-des-donnees-massives/)
- Un déluge de données : [https://interstices.info/un-deluge-de-donnees/](https://interstices.info/un-deluge-de-donnees/)
- Les ingrédients des algorithmes : [https://interstices.info/les-ingredients-des-algorithmes/](https://interstices.info/les-ingredients-des-algorithmes/)
- 10 questions sur les algorithmes : [https://interstices.info/10-questions-sur-les-algorithmes/](https://interstices.info/10-questions-sur-les-algorithmes/)
- Les algorithmes de tri : [https://interstices.info/les-algorithmes-de-tri/](https://interstices.info/les-algorithmes-de-tri/)
