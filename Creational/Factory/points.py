from enum import Enum, auto
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = auto()
    POLAR = auto()


# print(CoordinateSystem.CARTESIAN.name, CoordinateSystem.CARTESIAN.value)
# print(CoordinateSystem.POLAR.name, CoordinateSystem.POLAR.value)

# --------------------------- Method 1 ---------------------------- #
class Point:
    def __init__(self, x, y, system=CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = x
            self.y = y
        elif system == CoordinateSystem.POLAR:
            self.x = x * cos(y)
            self.y = x * sin(y)

    def __str__(self):
        return f"({self.x}, {self.y})"


print("Method 1")
p1 = Point(1, 2)
p2 = Point(5, 0.93, CoordinateSystem.POLAR)
print(p1, p2, "\n")

"""
REMARKS: 
Not a good method it cann't work well for OCP, LSP.
"""


# ----------------------- Method 2 ------------------------------ #
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_cartesian_coordinates(cls, x, y):
        return cls(x, y)

    @classmethod
    def from_polar_coordinates(cls, rho, theta):
        return cls(rho * cos(theta), rho * sin(theta))

    def __str__(self):
        return f"({self.x}, {self.y})"


print("Method 2")
p1 = Point.from_cartesian_coordinates(3, 4)
p2 = Point.from_polar_coordinates(rho=5, theta=0.93)
p3 = Point(3, 4)
print(p1, p2, p3, "\n")

"""
REMARKS: 
Following LSP. 
As code grows class will have too many methods inside it.
Class will become bulkier and will be hard to debug.
Not good for clean code.
We need to seprate those classmethod or custom constructal methods.
"""

# -------------------- Mehod 3 --------------------------- #


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    class Factory:

        @staticmethod
        def from_cartesian_coordinates(x, y):
            return Point(x, y)

        @staticmethod
        def from_polar_coordinates(rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))


print("Method 3")
p1 = Point.Factory.from_cartesian_coordinates(3, 4)
p2 = Point.Factory.from_polar_coordinates(rho=5, theta=0.93)
print(p1, p2, "\n")

"""
REMARK:
We have seprated the Product Class (Point) and constructing intializers.
This helpful for client to initialize the class.
"""

# ----------------- Method 4 --------------------------------- #


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class PointFactory:

    @staticmethod
    def from_cartesian_coordinates(x, y):
        return Point(x, y)

    @staticmethod
    def from_polar_coordinates(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


print("Method 4")
p1 = PointFactory.from_cartesian_coordinates(3, 4)
p2 = PointFactory.from_polar_coordinates(rho=5, theta=0.93)
print(p1, p2, "\n")


"""
REMARKS: 
Suppose, we don't want to reveal too much about how to initialize
or client doesn't care about the construction for Point class. 

Client wants to use only the Point class methods.

Then we can use this pattern. 
"""
