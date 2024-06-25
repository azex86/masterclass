"""
une condition est un booléen 


if condition_1 :
    do action           

elif condition_2 :
    do action

else :
    do action
    
"""


#exemple
a = 10

if a > 5:
    print("a est supérieur à 5")
elif a == 5:
    print("a est égale à 5")
else:
    print("a est inférieur à 5")

#ce code va afficher "a est supérieur à 5"
# l'utilisation de if impose la présence de ':' et d'une 'indentation' 
# sur les bloc de code à executer si la condition est vérifiée
# il est possible d'enchaîner des 'elif' ou de n'utiliser que if ou if/else
"""
if ...:
    do action

do ....


if ...:
    ...
else:
    ...

"""


#la structure if/else est la méthode principale pour conditionner l'execution de code
#il existe une seconde structure 'match'
"""
match value:
    case filtre:
        do action
    case filtre:
        do action
    case _:
        do action

value est expression évaluable
filtre est un motif confrontable à l'expression         
        
"""

a = 4

match a:
    case 5:
        print("a est égale à 5")
    case n if n > 5:
        print("a est supérieur à 5")
    case n if n in [0,1,2,3,4]:
        print("a est un entier naturel inférieur à 5")




