#langage/module.py
#module_utiles/numpy_.py
#module_utile/matplotlib_.py  

#Nous allons tracer nos première courbes et apprivoiser matplotlib

#consigne - 1
#récupérer les valeurs n,max,min du terminal
#générer une liste de n nombres aléatoire compris dans [min;max]
#tracer le nuage de point
#calculer la moyenne, la valeur maximale et minimale
#tracer la courbe reliant ces trois points sur le même graphique

#aide

def frange(start,stop,step):
    """
        équivalent de range sauf que l'interval peut-être décimal
        exemple:

        for i in frange(0,1,0.1):
            print(i)
        #va afficher :
        #0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9
    """
    while start<= stop:
        yield start
        start+=step



import matplotlib.pyplot as plt 


X = [x for x in range(100)]
Y = [x*1 for x in X]
plt.plot(X,Y)
plt.show()


#consigne - 2
# Nous souhaitons tracer la fonction exponentielle
# et par la même trouver une valeur approchée de e
# rappel : e(x) est déinie comme
#       e(0) = 1
#       e'(x) = e(x) <=> (e(x+h)-e(x))/h = e(x) avec h qui tend vers 0 ou une très petite valeur (pour nous 0.1 suffit)
# 
#Bonne chance !





#consigne - 3
#Nous souhaitons tracer la fonction ln
#rappel : la fonction ln est la fonction inverse de e
# soit e(len(x)) = x ou ln(e(x)) = x 
# en d'autre terme ln est le symétrique de e par la droite d'équation y = x
# si on pose x et y = e(x) et x1 et y1 = ln(x1) 
# on sait que y1 = ln(y) = ln(e(x)) = x <=> y1 = x
# et comme y1 = ln(x1) = ln(y) <=> x1 = y

#en somme, ln revient à prendre le fonction  e(x) à laquelle vous intervertissez x et y




#consigne - 4
#tracer la suite de Fibonacci
