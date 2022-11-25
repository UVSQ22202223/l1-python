"""1"""
def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    a=temps[0]*86400+temps[1]*3600+temps[2]*60+temps[3]
    return a

temps = (1,3,46,40)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    b=seconde//86400
    c=(seconde% 86400)//3600
    d=((seconde% 86400)%3600)//60
    e=((seconde% 86400)%3600)%60
    return (b,c,d,e)

seconde = secondeEnTemps(100000)
print(seconde[0],"jours",seconde[1], "heures",seconde[2],"minutes",seconde[3],"secondes" )

"""2"""
def afficheTemps(temps):
    if temps[0]>1 :
        f="jours"
    elif temps[0]==1 :
        f="jour"
    if temps[1]>1 :
        g="heures"
    elif temps[1]==1 :
        g="heure"
    if temps[2]>1 :
        h="minutes"
    elif temps[2]==1 :
        h="minute"
    if temps[3]>1 :
        i="secondes"
    elif temps[3]==1 :
        i="seconde"
    print(temps[0],f,temps[1],g, temps[2],h, temps[3],i,)
    
temps=(1,1,14,23) 
afficheTemps(temps)

"""autre méthode plus facile"""

def affichePluriel(val,mot):
    if val!=0 :
        print(" ",val,mot,end="")
    if val>1 :
        print("s",end="")

def afficheTemps(temps) :
    affichePluriel(temps[0],"jour")
    affichePluriel(temps[1],"heure")
    affichePluriel(temps[2],"minute")
    affichePluriel(temps[3],"seconde")
    print("\n")

afficheTemps((1,0,14,23))

"""3"""
def demandeTemps():
    j=int(input("rentrer un nombre de jours"))
    k=int(input("rentrer un nombre d'heures"))
    l=int(input("rentrer un nombre de minutes"))
    m=int(input("rentrer un nombre de secondes"))
    if k>24 or l>60 or m>60:
        print("Erreur")
        exit()
    else :
        pass
    return(j,k,l,m,)

afficheTemps(demandeTemps())

"""4"""
def sommeTemps(temps1,temps2):
    p=tempsEnSeconde(temps1)
    s=tempsEnSeconde(temps2)
    return secondeEnTemps(p+s)

print(sommeTemps((2,3,4,25),(5,22,57,1)))

"""5"""
def proportionTemps(proportion,temps):
    temps=tempsEnSeconde(temps)
    prop=temps*proportion
    final=secondeEnTemps(prop)
    return temps,proportion,final


print(proportionTemps(0.2,(2,0,36,0)))

"""6"""
def tempsEndate(temps) :
    tempsa=temps[0]//365
    tempsj=temps[0]%365+temps[1]
    return tempsa,tempsj
tempsa,tempsj=tempsEndate((568,23,34,10))

print((tempsa,tempsj,temps[2],temps[3]))

"""correction"""
def tempsEndate(temps):
    jour,heure,min,sec=temps
    annee=jour//365+1970
    return(annee,jour,heure,min,sec)
def afficheDate(date=-1) :
    annee,jour,heure,min,sec=date
    print("année",annee,end="")
    afficheTemps((jour,heure,min,sec))

import time
print(time.time(1))
print(time.gmtime(time.time(1)))