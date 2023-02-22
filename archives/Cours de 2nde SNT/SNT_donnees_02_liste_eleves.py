import random

def fonction_lecture_csv(fichier_source, fichier_dest):
    fichier = open(fichier_source, "r")
    entete = fichier.readline()
    nom_prenom = []
    nom = []
    prenom = []
    classe = []
    date = []
    opt1 = []
    opt2 = []
    opt3 = []
    opt4 = []
    for ligne in fichier:
        donnee = ligne.rstrip('\n\r').split(";")
        nom_prenom = donnee[0].split(' ')
        nom.append(nom_prenom[0])
        prenom.append(nom_prenom[1])
        classe.append(donnee[1])
        date.append(donnee[2])
        opt1.append(donnee[4])
        opt2.append(donnee[5])
        opt3.append(donnee[6])
        opt4.append(donnee[7])
    random.shuffle(nom)
    random.shuffle(prenom)
    random.shuffle(classe)
    random.shuffle(opt1)
    random.shuffle(opt2)
    random.shuffle(opt3)
    random.shuffle(opt4)
    donnees = []
    for i in range(len(nom)):
        donnees.append([nom[i],prenom[i],date[i],opt1[i],opt2[i],opt3[i],opt4[i]])
    
    fichier2=open(fichier_dest, "w")
    fichier2.write(entete)
    for elmt in donnees:
        ligne=";".join(elmt)+'\n'
        fichier2.write(ligne)
    fichier2.close()
    return

fonction_lecture_csv('liste_eleves.csv', 'liste_eleves_modifiee.csv')
