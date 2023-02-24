def egalite_flottants(a: float, b: float, precision: float = 0.00000001)-> bool:
    '''
    Vérifie si les deux nombres passés en paramètre sont égaux à la précision donnée
    en dernier paramètre près.
    Renvoie True si a et b sont égaux à la précision près, sinon, retourne False.

    :param:
    a, b : les deux nombres à comparer.
    precision : précision acceptée. Valeur par défaut 0,00 000 001.

    :exemple:
    >>> egalite_flottants(0.1 + 0.2, 0.3, 0.0001) == True
    True
    >>> egalite_flottants(0.1 + 0.2, 0.3) == True
    True
    >>> egalite_flottants(1/3, 0.33333333333333333333) == True
    True
    >>> egalite_flottants(1/3, 0.3333333) == False
    True
    '''
    if abs(a - b) < precision :
        nb_egaux = True
    else:
        nb_egaux = False
    return nb_egaux

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = False)