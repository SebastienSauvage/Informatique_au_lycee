joueur = 1
partie_en_cours = True


def init_grille()->list:
    '''Initialise une grille de jeu
    :param:
    None
    :renvoie:
    Une grille vide
    :exemple:
    >>> init_grille()
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    '''
    return [[0 for col in range(3)] for ligne in range(3)]

def afficher_grille(grille):
    '''Affiche la grille du jeu
    :param:
    grille : grille du jeu composée d'entiers de 0 à 4
    :renvoie:
    None
    :Effet de bord:
    Affichage dans la console / fenêtre Pygame
    :exemple:
    >>> afficher_grille([[4, 1, 1],[1, 4, 1], [0, 2, 4]])
    O x x 
    x O x 
    _ o O 
    '''
    elmts_graphiques = ['_', 'x', 'o', 'X', 'O']
    for ligne in grille:
        for elmt in ligne:
            elmt_a_afficher = elmts_graphiques[elmt]
            print(elmt_a_afficher, end = ' ')
        print('')
        
def verifier_ligne(grille, num_lig):
    global partie_en_cours
    prod = 1
    ligne = grille[num_lig]
    for elmt in ligne:
        prod = prod * elmt
    
    if prod in (1, 8):
        for num_col in range(3):
            grille[num_lig][num_col] = grille[num_lig][num_col] + 2
        partie_en_cours = False
    
def verifier_toutes_lignes(grille):
    for num_lig in range(3):
        verifier_ligne(grille, num_lig)
        
def verifier_colonne(grille, num_col):
    global partie_en_cours
    prod = 1
    for ligne in grille:
        elmt = ligne[num_col]
        prod = prod * elmt
    if prod in (1, 8):
        for num_lig in range(3):
            grille[num_lig][num_col] = grille[num_lig][num_col] + 2
        partie_en_cours = False
    
def verifier_toutes_colonnes(grille):
    for num_col in range(3):
        verifier_colonne(grille, num_col)
        
def verifier_diagonale1(grille):
    prod = 1
    for i in range(3):
        elmt = grille[2 - i][i]
        prod = prod * elmt
        
    if prod in (1, 8):
        for i in range(3):
            grille[2 - i][i] = grille[2 - i][i] + 2
            
def verifier_diagonale2(grille):
    prod = 1
    for i in range(3):
        elmt = grille[i][i]
        prod = prod * elmt
        
    if prod in (1, 8):
        for i in range(3):
            grille[i][i] = grille[i][i] + 2
        
def verifier_toutes_diagonales(grille):
    verifier_diagonale1(grille)
    verifier_diagonale2(grille)

def verifier_grille(grille):
    '''
    :exemples:
    >>> g = [[2, 1, 1],[0, 2, 1], [0, 0, 2]]
    >>> verifier_grille(g)
    >>> g
    [[4, 1, 1], [0, 4, 1], [0, 0, 4]]
    '''
    verifier_toutes_lignes(grille)
    verifier_toutes_lignes(grille)
    verifier_toutes_diagonales(grille)




if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)