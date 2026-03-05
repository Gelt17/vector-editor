from math import sqrt

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(abs(self.x - other.x), abs(self.y - other.y))
        return NotImplemented 
    
    def __rsub__(self, other):
        if isinstance(other, Point):
            return Point(abs(other.x - self.x), abs(other.y - self.y))
        return NotImplemented 

    def __str__(self) -> str:
        return f"Точка:({self.x}, {self.y})"

class Line:
    def __init__(self, point_1: Point, point_2: Point,):
        self.point_1 = point_1
        self.point_2 = point_2

    def __len__(self) -> float:
        point = self.point_1 - self.point_2
        return sqrt(point.x ** 2 + point.y ** 2)

    def __str__(self) -> str:
        return f"Линия длиной {self.__len__():.3f} и координатами ({self.point_1.x, self.point_1.y}), ({self.point_2.x, self.point_2.y})"

class Circle:
    def __init__(self, center: Point, radius: int):
        self.center = center
        self.radius = radius
    
    def __str__(self) -> str:
        return f"Окружность с центром ({self.center.x, self.center.y}) и радиусом {self.radius}"
    
class Square:
    def __new__(cls, point_1: Point, point_2: Point, point_3: Point, point_4: Point):
        line_1 = Line(point_1, point_2)
        line_2 = Line(point_2, point_3)
        line_3 = Line(point_3, point_4)
        line_4 = Line(point_4, point_1)
        line_d1 = Line(point_1, point_3)
        line_d2 = Line(point_2, point_4)


        if line_1.__len__() == line_2.__len__() == line_3.__len__() == line_4.__len__() and line_d1.__len__() == line_d2.__len__():
            return super().__new__(cls)
        else:
            raise ValueError("Введите валидные данные")


    def __init__(self, point_1: Point, point_2: Point, point_3: Point, point_4: Point):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
        self.point_4 = point_4
        self.line = Line(point_1, point_2)
    
    def __str__(self) -> str:
        return f"Квадрат с координатами ({self.point_1.x, self.point_1.y}), ({self.point_2.x, self.point_2.y}), ({self.point_3.x, self.point_3.y}), ({self.point_4.x, self.point_4.y}), имеющий периметр {self.line.__len__() * 4:.3f} и площадь {self.line.__len__() ** 2:.3f}"
    

