# langage/list.py
#  langage/fonction.py 

#Consignes :

#écrire un programme qui :
#   lit un nombre depuis le terminal (n)
#   calcul et affiche le n premiers nombre premiers

#exemple:
#n>> 4
#2
#3
#5
#7

#aide
def divisible(n:int,d:int)->bool:
    #Retourne True si n est divisible par n
    #Retourne False si n n'est pas divisble par n
    reste = n % d
    if reste == 0 :
        return True
    else:
        return False
    

#CORRECTION

n = int(input("Entrez le nombre de nombre premiers désirés >>"))#on suppose que l'utilisateur est OK

premiers = [] #liste des nombre premiers

x = 2 #nombre dont nous testons la primalité (=est-il premier)

def is_prime(x:int)->bool:
    #Retourne si un nombre est premier
    for d in range(2,x): #on test la division par tous les nombre entier naturels inférieur à x (i exclu)
        if divisible(x,d): #si il est divisible 
            return False #il n'est pas premier on met fin à la recherce
    return True #si il n'est divisible par aucun il est premier


while len(premiers) < n:  #noter que l'usage de len est facultatif, on peut lui substituer une variable 
    if is_prime(x): #si x est premier
        premiers.append(x) #on l'ajoute à notre liste
    
    x = x + 1 #dans tous les cas on itère x 

#on affiche nos nombres premiers
for i in range(n):
    if i==1:
        print(f"Le premier nombre premier est {premiers[i]}")
    else:
        print(f"Le {i} ème nombre premier est {premiers[i]}")


