import math


class Vector:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y, self.z + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y, self.z - other.y)

    def __mul__(self, k: float) -> "Vector":
        return Vector(self.x * k, self.y * k, self.z * k)

    def __equal__(self, other: "Vector") -> "Vector":
        return self.x == other.x and self.y == other.y and self.z == other.z

    def norme(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

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
        return f"({self.x:4.2};{self.y:4.2};{self.z})"
    def quadratique(self)->float:
        return self.x * self.x + self.y * self.y + self.z * self.z
    
    def __neg__(self)->'Vector':
        return Vector(-self.x,-self.y,-self.z)
    
    def angle(self)->float:
        
        return math.atan2(self.y,self.x)
    

print(f"{Vector(1.0,0)} => {Vector(1,0).angle():.2} =={0} == {Vector(1,0).unit().angle():.2} == {Vector(1,0).unit()}")
print(f"{Vector(1,1)} => {Vector(1,1).angle():.2} =={math.pi/4:.2} == {Vector(1,1).unit().angle():.2} == {Vector(1,1).unit()}")
print(f"{Vector(0,1)} => {Vector(0,1).angle():.2} =={math.pi/2:.2} == {Vector(0,1).unit().angle():.2} == {Vector(0,1).unit()}")
print(f"{Vector(-1,1)} => {Vector(-1,1).angle():.2} =={3*math.pi/4:.2} == {Vector(-1,1).unit().angle():.2} == {Vector(-1,1).unit()}")
print(f"{Vector(-1,0)} => {Vector(-1,0).angle():.2} =={math.pi:.2} == {Vector(-1,0).unit().angle():.2} == {Vector(-1,0).unit()}")
print(f"{Vector(-1,-1)} => {Vector(-1,-1).angle():.2} =={-3*math.pi/4:.2} == {Vector(-1,-1).unit().angle():.2} == {Vector(-1,-1).unit()}")
print(f"{Vector(0,-1)} => {Vector(0,-1).angle():.2} =={(-math.pi/2):.2} == {Vector(0,-1).unit().angle():.2}== {Vector(0,-1).unit()}")
print(f"{Vector(1,-1)} => {Vector(1,-1).angle():.2} =={(-math.pi/4):.2} == {Vector(1,-1).unit().angle():.2} == {Vector(1,-1).unit()}")

