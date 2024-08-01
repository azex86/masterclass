# Voici le code pour simuler le mouvement de deux astres dans un univers vierge
# et afficher leur position dans un graphe
# le but de l'exercice et d'ajouter un troisième astre 
# Les deux astres simulés ici sont la Terre et le Soleil
# on va donc essayer d'ajouter une planète de notre système


# Pour cela on utilisera une class Vector afin de simplifier les calculs dans l'espace
# exemple avec des listes:
# pos = [0,0,0]
# v = [5,1,-2]
# on avance de v
# pos = [pos[0]+v[0],pos[1]+v[1],pos[2]+v[2]]

# avec une class Vector
# pos = Vector(0,0,0)
# v = Vector(5,5,5)
# on avance de v
# pos = pos + v
import math

import numpy


class Vector:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, k: float) -> "Vector":
        return Vector(self.x * k, self.y * k)

    def __equal__(self, other: "Vector") -> "Vector":
        return self.x == other.x and self.y == other.y

    def norme(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def unit(self) -> "Vector":
        """
        Retourne le vecteur unité de ce vecteur:
            u = vec.unit()
            k = vec.norm()
            assert u*k == vec
        """
        n = self.norme()
        return Vector(self.x / n, self.y / n)

    def __repr__(self) -> str:
        return f"({self.x:5.2};{self.y:5.2})"

    def quadratique(self) -> float:
        return self.x * self.x + self.y * self.y

    def __neg__(self) -> "Vector":
        return Vector(-self.x, -self.y)

    def angle(self) -> float:
        return math.atan2(self.y, self.x)


G = 6.67428e-11  # m3 kg-1 s-2 la constante de l'attraction universelle

# on rappel que la force entre deux astre est G * M1 * M2 / d**2 où M1 et M2 sont les masses repectives des deux astres (en kg) et d la distance entre eux (en m)
# on rappel que l'accélération d'un astre est m * a = somme_des_forces <=> a = somme_des_forces / m


def calcul_force(
    masse_1: float, position_astre1: Vector, masse_2: float, position_astre2: Vector
) -> tuple[float, Vector]:
    """
    Retourne la force exercée entre deux astres par la seule force de gravitation newtonnienne
    en N ainsi qu'un vecteur coefficient d'application (équivalent d'un angle)

    ex: force,angle = calcul_force(M1,P1,M2,P2) #force est en N et angle est un vecteur unitaire
    force_vecteur = angle * force #on a ainsi le vecteur force en multipliant les deux

    """
    return G * masse_1 * masse_2 / (
        (position_astre2 - position_astre1).quadratique()
    ), (position_astre2 - position_astre1).unit()


def calcul_acceleration(force: float, masse: float) -> float:
    "retourne l'accélération produite par la force 'force' sur le corps de masse 'masse'"
    return force / masse


STEP = 10  # précision de la simulation en s
DURATION = 300 * 24 * 60 * 60  # on simule pendant 600 jours


S_pos = Vector(0, 0)  # position du Soleil en m, on le met au centre du repère
S_v = Vector(0, 0)  # vitesse du Soleil, nulle au début
S_masse = 2e30  # 1.98892e30  # en kg

T_pos = Vector(
    149_597_870_700, 0
)  # position de la Terre, à une unité astronomique du soleil, à l'horizontal
T_v = Vector(
    0, 29_800
)  # vitesse de la Terre, comme celle-ci est à l'extrême droite du soleil et la vitesse étant tangentielle, la vitesse est selon y
T_masse = 5.972e24  # en kg


T = numpy.arange(0, DURATION, STEP, numpy.float32)  # abscisse : temps en s
T_POS_X = numpy.zeros(T.shape)  # liste des position succesives de l'astre T
T_POS_Y = numpy.zeros(T.shape)

S_POS_X = numpy.zeros(T.shape)  # identique pour S
S_POS_Y = numpy.zeros(T.shape)


for i in range(len(T)):
    f, angle = calcul_force(
        S_masse, S_pos, T_masse, T_pos
    )  # on calcul la force d'attraction ainsi que son angle d'application

    S_a = angle * calcul_acceleration(
        f, S_masse
    )  # on détermine l'accélération du Soleil
    S_v = S_v + S_a * STEP  # on incrémente la vitesse du soleil par son accélération
    S_pos = S_pos + S_v * STEP  # on incrémente la position du soleil par sa vitesse

    S_POS_X[i] = S_pos.x  # on insère ces valeurs dans nos listes
    S_POS_Y[i] = S_pos.y

    T_a = (
        -angle * calcul_acceleration(f, T_masse)
    )  # même chose que pour le soleil, on inverse l'angle car on inverse le point de vue
    T_v = T_v + T_a * STEP
    T_pos = T_pos + T_v * STEP
    T_POS_X[i] = T_pos.x
    T_POS_Y[i] = T_pos.y

    if not i % 10000: #on va printer l'avancement de la simulation
                      #mais pour ne pas la ralentir on ne print qu'une fois sur 10000
        t = T[i]
        print(
            f"simulation en cours : {t}/{DURATION} : {(t/DURATION*100):6.2}%", end="\r"
        )

print()#on saute une ligne


import matplotlib.pyplot as plt #on import matplotlib sous le nom de plt

fig = plt.figure() #on instancie nore figure

positions = fig.add_subplot(1, 2, 1) #on ajoute un graph pour les positions (x en fonction de y)

positions.plot(T_POS_X, T_POS_Y, label="Terre")
positions.plot(S_POS_X, S_POS_Y, label="Soleil")
positions.axis("equal")  # Ensuring both axes have the same scale
positions.set_xlabel("position en m")
positions.set_ylabel("position en m")
positions.set_title("Simulation du mouvement de deux astres")
positions.legend()

pos_from_time_plot = fig.add_subplot(1, 2, 2)
pos_from_time_plot.plot(T, T_POS_X, label="Terre X")
pos_from_time_plot.plot(T, T_POS_Y, label="Terre Y")
pos_from_time_plot.plot(T, S_POS_X, label="Soleil X")
pos_from_time_plot.plot(T, S_POS_Y, label="Soleil Y")
pos_from_time_plot.legend()
pos_from_time_plot.set_xlabel("position en m")
pos_from_time_plot.set_ylabel("positon en m")

plt.show()#on affiche les graphiques
