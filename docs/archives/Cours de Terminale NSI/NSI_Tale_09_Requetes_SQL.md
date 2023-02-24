---
title: "Thème 2 - Chapitre 3 : Requêtes en langage SQL"
author: [Sébastien SAUVAGE]
date: "14/12/2022"
keywords: [NSI, terminale, SQL]
discipline: NSI
---

\huge \textbf{Thème 2}\normalsize  

\ 

\Large \textbf{Chapitre  : Requêtes en langage SQL}\normalsize  

\  

\  

Le but de ce TP est de découvrir le langage SQL sur des données réelles simples.  

Nous utiliserons des données issues de la base ouverte [https://opendata.lillemetropole.fr/](opendata.lillemetropole.fr/) plus précisément les données sur la population des communes du Nord en 2012 [téléchargeables ici](https://opendata.lillemetropole.fr/explore/dataset/evolution-et-structure-de-la-population-france-2012-categories-socio-professionn/information/).  

Les données ont été récupérées et organisées en deux tables pour simplifier leur manipulation :  

- la table `ville`
    - composée de cinq attributs de type `TEXT` appelés `code`, `region`, `departement`, `nom`, `coordonnees`.
    - l'attribut `code` est la clé primaire.
- la table `evolution`
    - composée de quatre attributs appelés `code`, `categorie`, `genre`, `effectif`.
    - les attributs `code`, `categorie`, `sexe` sont de type `TEXT` et `effectif` est de type `INTEGER`.
    - l'attribut `code` est une clé étrangère référençant l'attribut `code` de la table `ville`.

# Préparation
Récupérez le fichier [categories-socio-nord.db](./categories-socio-nord.db) et ouvrez-le à l'aide de l'application [DB Browser for SQLite - sqlitebrowser.org/](https://sqlitebrowser.org/).  

Cette application est un client du SGBD (Système de gestion de bases de données) SQLite qui permet de manipuler les tables et leur contenu de façon simplifiée et graphique.

# Consultation des données
Le DB Browser permet de consulter les données présentes dans chaque table, à l'aide de l'onglet "Parcourir les données".  

- Les attributs, aussi appelés champs, sont représentés en colonnes.
- Les enregistrements, aussi appelés entrées, sont représentés en lignes.

Vous pouvez noter le nombre d'enregistrements des deux tables, cela vous aidera à mieux comprendre ce qu'il se passe lors de l'exécution de certaines requêtes.  

# Extraction de données
Le DB Browser permet d'exécuter des requêtes SQL, à l'aide de l'onglet "Exécuter le SQL".  

- `SELECT` : en SQL, permet de sélectionner tout ou partie des données d'une ou plusieurs tables de la base.

Testez les requêtes suivantes, en essayant de deviner à l'avance ce que la requête va afficher et le nombre de lignes qui seront affichées.  

Certaines requêtes génèrent des erreurs, c'est voulu.  

Si vous copiez-collez plusieurs requêtes à la suite, seule l'exécution de la dernière sera visible. Vous pouvez exécuter les requêtes une par une en mettant les autres en commentaire en ajoutant `--` devant celles-ci. Vous pouvez aussi surligner la requête que vous souhaitez exécuter et cliquer sur le bouton pour exécuter le code.    

## Extraction de données d'une seule table

$\rightarrow$ Commençons par afficher tout ou une partie des attributs :  

```SQL
SELECT * FROM ville;
SELECT nom, code FROM ville;
```

$\rightarrow$ On peut renommer les colonnes pour un affichage plus explicite :  

```SQL
SELECT nom AS LIBELLE, code FROM ville;
```

\newpage

$\rightarrow$ `DISTINCT` élimine les doublons :  

```SQL
SELECT code FROM evolution;
SELECT DISTINCT code FROM evolution;
```

$\rightarrow$ `ORDER BY` ordonne les résultats :  

```SQL
SELECT DISTINCT code FROM evolution ORDER BY code DESC;
```

$\rightarrow$ La clause `WHERE` permet de préciser un critère pour filtrer les données :  

```SQL
SELECT * FROM ville WHERE code='59140';
SELECT nom, code FROM ville WHERE code='67340';
SELECT nom, code FROM ville WHERE code='59140' OR code='59260';
SELECT * FROM evolution WHERE code='59140';
```

$\rightarrow$ On peut récupérer le `MIN`, le `MAX`, le nombre de lignes avec `COUNT` ou la moyenne d'un attribut numérique avec `AVG` (\textit{average}, moyenne en anglais)  

```SQL
SELECT MIN(nom) AS MIN FROM ville;
SELECT COUNT(*) AS NbLignes FROM ville;
SELECT MAX(effectif) AS MAX, MIN(effectif) AS MIN, SUM(effectif) AS TOTAL, AVG(effectif) AS MOYENNE
      FROM evolution;
```

### Exercice
Construisez les requêtes permettant d'afficher les données qui répondent aux questions suivantes.  

1. Quels sont les différents libellés des catégories socioprofessionnelles par ordre alphabétique croissant ?
2. Combien de catégories différentes sont utilisées dans ce jeu de données ?
3. Quel est le code INSEE de Caullery ?
4. Affichez toutes les informations de la table évolution pour la ville de Caullery (en utilisant le code INSEE), triées par effectifs croissants.
5. Quels sont les codes postaux des villes ayant des catégories socioprofessionnelles dont les effectifs dépassent 2000 individus ?
6. Combien y a-t-il de femmes agricultrices dans le Nord ?
7. Quel est le nombre moyen d'employés par commune dans le Nord ?

## Extraction croisée de données de plusieurs tables
Observez les lignes, le nombre de lignes et le nombre de colonnes des résultats des requêtes montrées en exemple. Essayez d'en déduire le croisement qui a été fait.  

$\rightarrow$ Produit cartésien :

```SQL
SELECT * FROM ville, evolution;
SELECT * FROM ville, evolution WHERE nom='Caullery';
SELECT nom, categorie
    FROM ville, evolution
    WHERE nom='Caullery';
```

$\rightarrow$ Attributs qui ont le même nom dans des tables différentes :  

Lorsque des attributs ont le même nom dans des tables différentes, il est nécessaire de préciser le nom de la table dont viennent les données que l'on veut afficher.

```SQL
SELECT ville.code AS code1, evolution.code AS code2, nom
    FROM ville, evolution
    WHERE nom='Caullery';
```

$\rightarrow$ On peut renommer les tables :

```SQL
SELECT nom, v.code AS code1, effectif
    FROM ville AS v, evolution AS e
    WHERE nom='Caullery';
```

\newpage

$\rightarrow$ Si on renomme une table, seul le nouveau nom existe dans la requête :

```SQL
SELECT nom, ville.code AS code1, e.code AS code2, effectif
    FROM ville AS v, evolution AS e
    WHERE nom='Caullery';
```

$\rightarrow$ Utilisation de la jointure entre tables : `JOIN` :  

Attention ! Il faut préciser sur quelles clés la jointure doit être faite.

```SQL
SELECT v.code, nom AS ville, categorie, genre, effectif
    FROM ville AS v JOIN evolution AS e ON v.code=e.code
    WHERE nom='Caullery';
```

$\rightarrow$ Un exemple de sous-requête, pas explicitement au programme :

```SQL
SELECT v.code AS code, nom, categorie, genre, effectif
    FROM ville AS v JOIN evolution AS e ON v.code=e.code
    WHERE  effectif=(SELECT max(effectif) FROM evolution);
```

### Exercice
Construisez les requêtes permettant d'afficher les données qui répondent aux questions suivantes.  

1. Affichez les catégories socioprofessionnelles, genres et effectifs pour la ville de Caullery, sans utiliser le code INSEE, triées par effectifs croissants.
2. Affichez les noms des villes, ainsi que les catégories et genres des données ayant des effectifs à 0, triés par catégories.
3. Quelles sont les noms des villes ayant des catégories socioprofessionnelles dont les effectifs dépassent 2000 individus ?
4. Ordonnez le résultat par effectifs décroissants.
5. Même question en supprimant la ville de Lille des résultats possibles.

# Modification des données

- la requête `INSERT` permet d'insérer des données (d'ajouter des lignes dans la table),
- la requête `UPDATE` permet de mettre à jour les données,
- la requête `DELETE` permet de supprimer des lignes.

Testez les requêtes suivantes. Consultez les données à l'aide d'un `SELECT`, avant et après avoir fait les modifications.  

Pourquoi certaines requêtes sont refusées ?  

$\rightarrow$ Insertion de données :  

```SQL
INSERT INTO ville VALUES ('62000','31','62','Calais','50.291048,2.7772211');
INSERT INTO ville VALUES ('59140','31','59','Caullery','50.0824546804,3.37276572782');
INSERT INTO evolution VALUES ('59140','Professions Intermédiaires','Femmes',45);
INSERT INTO evolution VALUES ('59140','Enseignants','Hommes',45);
INSERT INTO evolution VALUES ('62200','Professions Intermédiaires','Femmes',45);
```

$\rightarrow$ Mise à jour de données :

```SQL
UPDATE ville SET code='62001' WHERE code='62000';
UPDATE ville SET code='59000' WHERE nom='Lille';
```

$\rightarrow$ Suppression de données :

```SQL
DELETE FROM ville WHERE code='62001';
DELETE FROM ville WHERE code='62000';
DELETE FROM evolution WHERE code='59140' AND categorie='Professions Intermédiaires' AND genre='Femmes' AND effectif=45;
DELETE FROM evolution WHERE categorie="Enseignants";
```

### Exercice
Construisez les requêtes permettant de modifier les données qui répondent aux questions suivantes.  

1. Insérez les données correspondants à une nouvelle ville de votre choix dans la table ville.
2. Modifiez le nom de cette ville.
3. Finalement, supprimez-la.
4. Insérez un effectif de catégorie socioprofessionnelle associée à une nouvelle ville.
5. Supprimez ces données.

\   

\   

\underline{{\textit{\textbf{Sources}}}}  

- Université de LILLE (2020, 16 novembre). _Découverte du langage SQL_. DIU EIL.  

[https://gitlab-fil.univ-lille.fr/diu-eil-lil/portail/-/blob/master/bloc4-5/sql1/Readme.md](https://gitlab-fil.univ-lille.fr/diu-eil-lil/portail/-/blob/master/bloc4-5/sql1/Readme.md)
