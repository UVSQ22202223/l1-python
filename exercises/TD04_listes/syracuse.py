"""2"""
def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    l=[n]
    while n>1 :
        if n%2==0:
            n=n//2
        else :
            n=n*3+1
        l.append(n)
    return l

print(syracuse(3))

"""3"""
def testeConjecture(n_max) :
    """ Teste la conjecture de Collatz pour toutes les valeurs de 1 à n_max """
    for i in range (2,n_max) :
        syracuse(i)
    return True
print(testeConjecture(10))

"""4"""
def tempsVol(n):
   """ Retourne le temps de vol de n """
   a=len(syracuse(n))-1
   return a

print("Le temps de vol de",10, "est", tempsVol(10))

""""5"""
def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    liste_tmpsVol=[]
    for i in range (1,n_max+1) :
        m=tempsVol(i)
        liste_tmpsVol.append(m)
    return liste_tmpsVol
"""6"""
L=tempsVolListe(10)
print(L.index(max(L))+1,max(L))

"""7"""
"""L’altitude maximale de l'entier n est la plus grande valeur par laquelle 
passe n au cours de son vol. Déterminer quel entier entre 1 et 10000 a la plus
 grande altitude maximale (réponse 27114424, atteint par l'entier 9663)"""

print(max(syracuse(33)))
def altMax(n) :
    l=syracuse(n)
    return max(l)
listeAlt=[altMax(i) for i in range (1,10001)]
altMaxListe=max(listeAlt)
entierMax=listeAlt.index(altMaxListe)+1
print(altMaxListe,entierMax)
