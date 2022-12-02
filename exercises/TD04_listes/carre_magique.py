"""1/C'est bien un carré magique sa constante est 34 """

"""2"""
carre_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]

"""3"""
carre_pas_mag=[list(l) for l in carre_mag]
carre_pas_mag[3][2]=7
carre_pas_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,7,13]]

"""4"""
def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for l in carre:
        print(l)

print("carré magique :")
afficheCarre(carre_mag)
print("carré pas magique :")
afficheCarre(carre_pas_mag)

"""5"""
def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme,
     et -1 sinon """
    sum1ligne=sum(carre[0])
    for l in carre[1 :] :
        sum(l)
    if sum(l)==sum1ligne :
        return sum(l)
    else :
        return -1

print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))

"""6"""
def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, 
    et -1 sinon """
    l1=[l[0] for l in carre]
    l2=[l[1] for l in carre]
    l3=[l[2] for l in carre]
    l4=[l[3] for l in carre]
    if sum(l1)==sum(l2)==sum(l3)==sum(l4) :
        return sum(l1)
    else:
        return -1

print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))

"""7"""
def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme,
    et -1 sinon """
    diago1=[carre[0][0],carre[1][1],carre[2][2],carre[3][3]]
    diago2=[carre[0][-1],carre[1][-2],carre[2][-3],carre[3][-4]]
    sommediago1=sum(diago1)
    sommediago2=sum(diago2)
    if sommediago1==sommediago2 :
        return sommediago1
    else :
        return -1

print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))

"""8"""
def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    a=testDiagonalesEgales(carre) 
    b=testColonnesEgales(carre) 
    c=testLignesEgales(carre)
    return a==b and b==c

print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))

"""9"""
def estNormal(carre):
    """Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon"""
    n=len(carre)
    for i in range(1,n*n+1) :
        trouve=False
        for l in carre :
            if i in l :
                trouve=True 
        if not trouve :
            return False
    return True

"""correction"""

def estNormal2(carre):
    """Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    n=len(carre)
    nombres=list(range(1,n*n+1))
    for i in range(n):
        for j in range(n):
            if carre[i][j] in nombres :
                nombres.remove(carre[i][j])
    return len(nombres)==0


print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))

print(estNormal2(carre_mag))
print(estNormal2(carre_pas_mag))