from turtle import *

COTE = 50
COULEURS = ['black', 'white']

def carre(couleur):
    global COTE
    fillcolor(couleur)
    begin_fill()
    for _ in range(4):
        forward(COTE)
        right(90)
    end_fill()
    forward(COTE)
    
def retour_ligne(nb_col):
    global COTE
    backward(nb_col * COTE)
    right(90)
    forward(COTE)
    left(90)

def ligne1(nb):
    tab = []
    return [i % 2 for i in range(nb)]

def ligne2(nb):
    return [1 - i % 2 for i in range(nb)]

def grille(nb):
    g = []
    for i in range(nb):
        if i % 2:
            g.append(ligne1(nb))
        else:
            g.append(ligne2(nb))
    return g

def trace_grille(grille):
    global COULEURS
    for lig in grille:
        for elmt in lig:
            carre(COULEURS[elmt])
        retour_ligne(len(grille))

trace_grille(grille(10))