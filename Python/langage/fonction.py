#écrire du code avec des variables est des conditions
#va généralement mener à réecrire certaine séquence de code
#et à écrire des gros pavé incompréhensible pour un autre ou
#même pour vous à long terme

#ainsi on prefère séparer le code en block distincts et réutilisable
#des fonctions

#pour définir une fonction 
"""
def nom_de_la_fontion_sans_espace (argument1,argument2,.....) :
    code....
    ....
    return valeur_de_retour

    on retient le mot clé 'def'
    les parenthèses avec les arguments si il y en a
    les ':'
    l'indentation pour le bloc de la fonction
    le mot clé 'return' pour retourner une valeur

l'utilisation d'une fonction en informatique est très proche des mathématiques
on appelle la fonction en mettant :
nom_de_la_fontion (arguments)

exemple:
"""

def f(x):
    return x*x #fonction carré


x = 5
y = f(x) #y = 25

#il également possible de définir une fonction sans argument
def f():
    return 5

x = f()

#et/ou sans valeur de retour

def f():
    print("fonction f")

f()

#noté que f est alors une variable dont l'objet est de type function
#il est donc possible de passer une fonction en argument d'une autre fonction
#exemple:

def appliquer_fonction_a_une_variable(variable,fonction):
    return fonction(variable)

def f(x):
    x+1

x = 0
y = appliquer_fonction_a_une_variable(x,f) #y=1

#dans ce genre de cas la définition de f peut paraître trop longue et lourde à lire 
#pour une seule et unique utilisation
#python permet de définir une fonction 'lambda' sur une seule ligne généralement
f = lambda a: a+1 #est équivalent de def f(x): [retour à la ligne]return x+1

#ainsi l'exemple plus haut devient
x = 0
y = appliquer_fonction_a_une_variable(x,lambda z:z+1)



#à l'intérieur d'une fonction, les variables sont locales
#elles n'existent que dans la fonction et disparaissent à la fin de celle-ci
#de plus les variables extérieurs sont accessible depuis la fonction qu'en lecture
#pour écrire sur des variables global depuis une fonction il faut utiliser le mot clé 'global' nom_var au d"ébut de la fonction
#même chose pour des variable non local, mais pas global avec le mot clé 'nonlocal'

x = "salut"
y = 5
def f():
    global x
    print(x) #c'est possible lecture seulement

    x = "hello world" #écriture
    y = x
    def h():
        nonlocal y
        print(y)#"hello world"

    h()
    
f()