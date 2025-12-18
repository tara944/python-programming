from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# Square Class
class Square(Shape):

    def _init_(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        print("Area of Square =", self.a * self.b)


# Circle Class
class Circle(Shape):

    def _init_(self, r):
        self.r = r

    def area(self):
        print("Area of Circle =", 3.14 * self.r * self.r)


# -------- MAIN --------
sq = Square(10, 10)
sq.area()

cr = Circle(5)
cr.area()