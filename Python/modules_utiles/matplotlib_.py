"""
Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations.
En d'autre terme, matplotlib est un SUPER et INCROYABLE module qui permet d'afficher des graphiques et des animations.

n'étant pas inclus dans python il faut installer matplotlib avec
pip install matplotlib
vous pouvez alors lancer l'execution du programme en même temps que vous lisez ce cours
"""



if 1:#juste pour indenter les parties
    """
        1 : Des graphes statiques

        La première utilisation de matplotlib est l'affichage d'une courbe ou d'un nuage de point

    """
    import matplotlib.pyplot

    #on instancie deux listes qui vont représenter notre courbe

    X = [0,1,2,3,4,5,6,7,8,9,10] #les abscisses des points
    Y = [0,1,2,3,4,5,6,7,8,9,10] #les ordonnées des points

    matplotlib.pyplot.plot(X,Y) #on demande à matplotlib de creer un "plot" (un tracé)
                                #à partir des points (0;0) (1;1) (2;2) etc...
                                #matplotlib va par défaut faire une interpolation linéaire de ces points
                                #en d'autre terme il va relier les points dans l'odre par des segments
                                #ici comme les point forment une fonction linéaire, il va tracer un droite du point (0;0) au point (10;10)

    matplotlib.pyplot.show() #on demande à matplotlib d'afficher les plots

    #on peut imaginer des formes plus poussée
    def f(x):
        return x*x #fonction carré

    Y = [f(x) for x in X]

    matplotlib.pyplot.plot(X,Y)
    matplotlib.pyplot.show()

    #on peut également faire des formes géométriques
    #un carré par exemple
    X = [0,1,1,0,0]     
    Y = [0,0,1,1,0]
    # (0;0) -> (1;0) ->(1;1) -> (0;1) -> (0;0) 
    #                                   pour fermer la figure il faut revenir au point de départ
    matplotlib.pyplot.plot(X,Y)
    matplotlib.pyplot.show()



    #il également possible d'afficher plusieurs courbes/figures en même temps dans le même "plot"

    X = list(range(10)) #produit une séquence de nombre linéaire [0,1,2,3,4,5,......,99,100]
    Y1 = [x for x in X]
    Y2 = [f(x) for x in X]


    matplotlib.pyplot.plot(X,Y1,label="Y1",color=(1,0,0)) 
    matplotlib.pyplot.plot(X,Y2,label="Y2",color=(0,0,1))
    matplotlib.pyplot.xlabel("Abscisse X")  #on donne un titre à l'axe X
    matplotlib.pyplot.ylabel("Ordonnées Y") #on donne uin titre à l'axe Y
    matplotlib.pyplot.title("Un super cours python sur matplotlib")#on donne un titre à la figure
    matplotlib.pyplot.legend() #on affiche une légende pour les courbe en utilisant les labels "Y1" et "X1" donnés précédemment
    matplotlib.pyplot.show()



    #pour plus de contrôle, on peut instancier un objet figure 
    fig = matplotlib.pyplot.figure()

    #on va maintenant faire nos opération sur cette objet
    plot1 = fig.add_subplot(1,2,1)#1 ligne, 2 colonnes, premier subplot #on ajoute un plot à notre figure   
    #les arguments permettent de placer le graphes dans la figure ici la figure aura deux graphes
    #répartis sur une ligne et deux colonnes et nous créons le premier des deux graphes

    plot1.plot(X,Y1,'ro',label="Y1") #on ajout notre fonction linéaire, 'o' signifie d'afficher les points uniquement et le 'r' pour red
    plot1.set_title("Fonction linéaire")
    plot1.legend()

    plot2 = fig.add_subplot(1,2,2)#1 ligne, 2 colonnes, deuxième subplot #on ajoute un plot à notre figure   
    plot2.plot(X,Y2,'bo',label="Y2") #on ajout notre fonction linéaire, 'o' signifie d'afficher les points uniquement et le 'b' pour blue
    plot2.set_title("Fonction carré")
    plot2.legend()

    fig.show() #on affiche la figure
    #fig.waitforbuttonpress() #on attend que l'utilisateur presse un bouton de sa souris sur la fenêtre

    matplotlib.pyplot.show() #noter que fig.show() ne vas pas attendre, si vous voulez attendre que l'utilisateur ferme la fenêtre
    #matplotlib.pyplot.show est obligatoire !


    #matplotlib permet de faire d'autre type de graphes

    #des diagrammes de disperssion pour afficher des points indépendant les uns des autres
    from random import random
    import numpy as np
    X = [random() for n in range(10)]
    Y = [random() for n in range(10)]
    plt = matplotlib.pyplot #on a la flemme d'écrire matplotlib on écrira plt à la place
    plt.scatter(X,Y,color=(0,0,1), label="Points")

    mean_dot = (np.mean(X),np.mean(Y)) #on ajoute le point moyen en rouge
    plt.scatter(mean_dot[0],mean_dot[1],color=(1,0,0))

    plt.grid() #on affiche un quadrillage

    plt.show()





    # Créer une nouvelle figure
    fig = plt.figure()
    # Ajouter des subplots à la figure
    ax1 = fig.add_subplot(2, 2, 1)  # 2 lignes, 2 colonnes, premier subplot
    ax2 = fig.add_subplot(2, 2, 2)  # 2 lignes, 2 colonnes, deuxième subplot
    ax3 = fig.add_subplot(2, 2, 3)  # 2 lignes, 2 colonnes, troisième subplot
    ax4 = fig.add_subplot(2, 2, 4)  # 2 lignes, 2 colonnes, quatrième subplot

    #quelques données 
    x = np.arange(0, 10, 2)
    ay = [1, 1.25, 2, 2.75, 3]
    by = [1, 1, 1, 1, 1]
    cy = [2, 1, 2, 1, 2]


    #graphique en aires empilées
    ax1.stackplot(x, ay,by,cy)
    ax1.set_title("stackplot")
    
    #camembert
    colors = [(1,0,0),((1,0.3,1)),(0.3,0,0.7),(0,0,1)]
    labels=["NFP","Ensemble","LR","RN"]
    ax2.pie([182, 168, 45,143],colors=colors,labels=labels) #camembert sur l'assemblée nationale
    ax2.set_title("pie")

    #graphique en bar
    ax3.bar([1, 2, 3], [4, 5, 6])
    ax3.set_title("bar")
    
    #histogramme
    ax4.hist([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    ax4.set_title("hist")

    # Afficher la figure
    plt.show()


    #On peut également vouloir représenter trois dimensions
    #pour cela on peut mettre de la couleur
    X = list(range(10))
    Y = list(range(10))
    Z = [[abs(x-y) for x in X] for y in Y]

    plt.pcolormesh(X,Y,Z, cmap='viridis')
    plt.colorbar()
    plt.title('Diagramme de densité avec couleur pour la différence absolue')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

    #on peut également utiliser de la 'vraie' 3D même si ce n'est pas forcément plus lisible

    #plot en 3d
    fig = plt.figure()
    #on spécifie projection="3d"
    plot = fig.add_subplot(1,1,1,projection="3d")
    #on passe les trois axes avec len(Z)=len(X)*len(Y)
    plot.plot(X,Y,Z)
    plot.set_title('Courbe 3D pour la différence absolue')
    plot.set_xlabel('X')
    plot.set_ylabel('Y')
    plot.set_zlabel('différence absolue')
    plt.show()

    #plot_surface pour faire de la 3D continue en rajoutant de la couleur en prime
    Z = np.array(Z)
    fig = plt.figure()
    #on spécifie projection="3d"
    plot = fig.add_subplot(1,1,1,projection="3d")
    #on passe les trois axes avec len(Z)=len(X)*len(Y)
    surface = plot.plot_surface(X,Y,Z,cmap="viridis")
    plot.set_title('Surface 3D avec couleur pour la différence absolue')
    plot.set_xlabel('X')
    plot.set_ylabel('Y')
    plot.set_zlabel('différence absolue')
    plt.colorbar(surface)
    plt.show()


    #plot_wireframe pour des courbures (de l'espace temps)
    fig = plt.figure()
    #on spécifie projection="3d"
    plot = fig.add_subplot(1,1,1,projection="3d")
    #on passe les trois axes avec len(Z)=len(X)*len(Y)
    surface = plot.plot_wireframe(X,Y,Z)
    plot.set_title('Lignes 3D pour la différence absolue')
    plot.set_xlabel('X')
    plot.set_ylabel('Y')
    plot.set_zlabel('différence absolue')
    plt.show()



    #équivalent pour des vecteurs 2D sur un plan 2D
    #ou des vecteurs 3D dans un espace 3D

    #valeurs des vecteurs
    Vx = [[x-y for x in X] for y in Y]
    Vy = [[y-x for x in X] for y in Y]
    Vz = [[abs(y-x) for x in X] for y in Y]

    #2D
    plt.quiver(X,Y,Vx,Vy)

    plt.title('Vecteur 2D pour la différence absolue')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

    #3D
    fig = plt.figure()
    #on spécifie projection="3d"
    plot = fig.add_subplot(1,1,1,projection="3d")
    Z = list(range(10))
    surface = plot.quiver(X,Y,Z,Vy,Vy,Vz)
    plot.set_title('Vecteurs 3D pour la différence absolue')
    plot.set_xlabel('X')
    plot.set_ylabel('Y')
    plot.set_zlabel('Z')
    plt.show()



if 2:
    """
    2 : Des animations dynamiques
    matplotlib permet d'afficher une succession de graphes pour former une animation
    cela permet en pratique de visualiser et de représenter une évolution d'une situation à une autre
    """
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation #nous utilisaons maintenant matplotlib.animation

    def f(x):
        return np.sin(x) #fonction sinus

    #la méthode principale consiste à créer une animation avec  les fonctions init et update
    #qui doivent retourner une liste d'Artist, un artist étant un objet à dessiner
    #init est executé au début de l'animation et update à chaque rafraichissement de l'image

    fig = plt.figure()  #on instancie une figure
    plot = fig.add_subplot(1,1,1) #ainsi qu'un plot
    xdata, ydata = [], [] #les coordonnées de nos points
    ln, = plot.plot([], [], 'ro') #l'objet qui représente la courbe

    def init(): 
        plot.set_xlim(0, 10) #on définit l'échelle pour les dernières valeurs de l'animation
        plot.set_ylim(-1.2, 1.2)
        return ln, #on retourne la courbe dans un tuple

    def update(frame):#frame est le numéro de la frame
        print(f"update : {frame}")
        xdata.append(frame)#on utilise frame comme abscisse
        ydata.append(f(frame))#on ajoute la valeur en ordonnée 
        ln.set_data(xdata, ydata)#on acualise la courbe
        return ln, #on retourne les objets actualisés à redessiner

    #on instancie maintenant notre animation:
    # fig : la figure à utiliser 
    # update : la fonction à appeler à chaque itération
    # frames : permet de décrire les valeurs successives de frame et ainsi de choisir le nombre d'image et la durée de l'animation
    # blit : ne redessine que les objets retournés par update permet d'optimise, l'enlever résout bien des problèmes mais on n'aime pas la facilité
    # interval : nombres de milisecondes de délai entre chaque update
    # repeat : si l'animation se recommence en boucle 
    # repeat_delay : trivial
    ani = matplotlib.animation.FuncAnimation(fig, update, frames=10,init_func=init, blit=True,interval = 300 , repeat = False)
    plt.show()



    #on peut évidemment appliquer une animation sur tous les types de figures et de plot vu ci-dessus
    #Exemple, chûte d'un objet dans un champ de pesanteur constant avec vitesse initiale

    g = 8
    vx = 30
    vy = 50
    x = 0
    y = 0
    X = [x]
    Y = [y]

    fig = plt.figure()
    plot = fig.add_subplot(1,1,1)

    line, = plot.plot(X,Y,'o',label="Position de l'objet")
    plot.set_xlabel("x en m")
    plot.set_ylabel("y en m")
    plot.legend()

    def update(frame):
        global x, y ,vx , vy
        x+=vx
        y+=vy
        vy-=g
        X.append(x)
        Y.append(y)
        line.set_data(X,Y)#actualise la courbe
        # ↓ actualiste les axes(échelle)
        plot.relim()# Recompute the data limits
        plot.autoscale_view()# Autoscale the view to the new data limits
        print(f"update {frame}: pos = {x};{y} v = {vx};{vy}")
        if y<0:
            ani.event_source.stop()
        return line,
    

    ani = matplotlib.animation.FuncAnimation(fig,update,None,blit=True,interval=500)
    plt.show()

if 3:
    """
    3 : Des graphes interactifs
    matplotlib permet une  interaction avec l'utilisateur,
    cela peut ainsi permettre à l'utilisateur d'influer la simulation ou d'en choisir une nouvelle
    """


    #capturer des événements
    #la méthode la plus brutales et de récupérer les événements
    #un événement est par exemple un clic souris ou une touche du clavier pressé par l'utilisateur
    #à ce moment la Windows envoie un message à matplotlib que nous pouvons récupérer

    import matplotlib.pyplot as plt

    X = list(range(-10,10)) #on définit nos données
    Y = [x for x in X]
    power = 1

    def f(x):
        return x**power #on va afficher une puissance que nous augmenterons à chaque clique souris

    def on_click(event): #fonction called lors de l'événement
        global power,Y
        print(f'Vous avez cliqué à ({event.xdata}, {event.ydata})')
        print(f"incrémentation de la puissance: {power} -> {power+1}")
        power+=1
        Y = [f(x) for x in X]
        ax.clear()
        ax.plot(X,Y)
        fig.canvas.draw()

    fig, ax = plt.subplots() #on instancie notre figure et notre graphe
    courbe, = ax.plot(X, Y) #notre courbe
    fig.canvas.mpl_connect('button_press_event', on_click) #on indique à matplolib d'appeler notre fonction à la récéption de l'événement 'button_press_event'
    plt.show()#on affiche




    #Il est également possible d'ajouter des "widget" dan snos figures
    #exemple de widget : Button Cursor TextBox
    import matplotlib.widgets
    
    
    #on va reprendre le principe précédent en remplacent le click souris par un bouton et un curseur et la fonction
    X = list(range(-10,10)) #on définit nos données
    Y = [x for x in X]
    power = 1

    def f(x):
        return x**power #on va afficher une puissance que nous augmenterons à chaque clique souris

    def update_cursor(value:float):
        global power,Y
        print(f'Vous avez bougé le curseur de {power} à {value}')
        power = int(value)
        Y = [f(x) for x in X]
        ax.clear()
        ax.plot(X,Y)
        fig.canvas.draw()

    def on_click(event): #fonction called lorsque notre bouton va être presser
        global power,Y
        print(f'Vous avez cliqué sur le bouton')
        print(f"incrémentation de la puissance: {power} -> {power+1}")
        power+=1
        Y = [f(x) for x in X]
        ax.clear()
        ax.plot(X,Y)
        cursor.set_val(power)
        fig.canvas.draw()

    fig, ax = plt.subplots() #on instancie notre figure et notre graphe
    fig.subplots_adjust(bottom=0.30) #on fait de la place pour loger nos widgets en dessous
    courbe, = ax.plot(X, Y) #notre courbe

    button_ax = fig.add_axes([0.10,0.05,0.30,0.15]) #on ajoute un tracé/plot/ax qui contiendra notre bouton
                        # [left, bottom, width, height], spécifie la position et la taille de l'ax
                        #on 0.30 en dessous de la figure donc height = 0.15 
                        #on veut notre bouton presque carré donc width = 0.30
                        #et on le veut en bas à gauche de notre figure donc left,bottom = 0.15 ,0.30
    b = matplotlib.widgets.Button(button_ax,"incremente la puissance")#on instancie notre bouton
    b.on_clicked(on_click) #on lie notre fonction on_click avec notre bouton

    cursor_ax = fig.add_axes([0.10+0.30+0.10,0.05,0.30,0.10])#même chose
    cursor = matplotlib.widgets.Slider(cursor_ax,"power",0,20,valinit=1)
    cursor.on_changed(update_cursor)

    plt.show()#on affiche