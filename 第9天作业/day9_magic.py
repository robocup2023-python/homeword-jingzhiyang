import math
from typing import *


class Point:
    def __init__(self, x: int | float, y: int | float, z=0):
        self.x = x
        self.y = y
        self.z = z
        print(f"Create {self}")
    
    def __str__(self):
        return f"Point({self.x:.3f},{self.y:3f},{self.z:.3f})"
    
    def __add__(self, other: 'Optional[Vector]') -> 'Optional[Point]':
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other: 'Optional[Vector|Point]') -> 'Optional[Point|Vector]':
        if isinstance(other, Point):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, Vector):
            return Point(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __lt__(self, other):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) < (other.x ** 2 + other.y ** 2 + other.z ** 2)
    
    def __del__(self):
        print(f"Delete {self}")


class Vector:
    def __init__(self, x: int | float, y: int | float, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"Vector({self.x:.3f},{self.y:.3f},{self.z:.3f})"
        # return f"Vector({self.x},{self.y},{self.z})"
    
    def __add__(self, other: 'Optional[Vector]'):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other: 'Optional[Vector]'):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __lt__(self, other):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) < (other.x ** 2 + other.y ** 2 + other.z ** 2)
    
    def __mul__(self, other: int | float):
        deg = other / 360 * math.pi * 2
        x = self.x * math.cos(deg) - self.y * math.sin(deg)
        y = self.x * math.sin(deg) + self.y * math.cos(deg)
        return Vector(x, y, self.z)
    
    def __truediv__(self, other: int | float):
        return self.__mul__(-other)


v1 = Vector(1, 2, 0)
print(v1 * 90)
print(v1 * -90)
print(v1 * -30)
print(v1 / 30)
