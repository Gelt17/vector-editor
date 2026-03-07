from shapes import Point, Line, Circle, Square

class ShapeList:
    def __init__(self, shapelist: dict = {}):
        self.shapelist = shapelist
        self.id = 1
    
    def add_shape(self, shape: str, coordinates: list[str]):
        print(coordinates)
        try:
            if shape == 'point':
                x, y = map(int, coordinates)
                self.shapelist[self.id] = str(Point(x, y))
            elif shape == 'line':
                x1, y1, x2, y2 = map(int, coordinates)
                self.shapelist[self.id] = str(Line(Point(x1, y1), Point(x2, y2)))
            elif shape == 'circle':
                x, y, r = map(int, coordinates)
                self.shapelist[self.id] = str(Circle(Point(x, y), r))
            elif shape == 'square':
                x1, y1, x2, y2, x3, y3, x4, y4 = map(int, coordinates)
                self.shapelist[self.id] = str(Square(Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4)))
            elif shape == 'oval':
                x, y, r1, r2 = map(int, coordinates)
                self.shapelist[self.id] = str(Circle(Point(x, y), r1, r2))
            elif shape == 'rectangle':
                x1, y1, x2, y2, x3, y3, x4, y4 = map(int, coordinates)
                self.shapelist[self.id] = str(Square(Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4)))
            else:
                print("Нет такой фигуры!")
                return 
        except Exception as e:
            print(str(e))
            print("Введены неккоректные параметры фигуры")
            return
        print(f"ID: {self.id}, Фигура: {str(shape)}")
        self.id += 1
        return self

    def delete_shape(self, id: str):
        try:
            id = int(id)
            if id in self.shapelist.keys():
                del self.shapelist[id]
                print(f"Фигура с ID {id} удалена.")
            else:
                print("Неверное ID")
                return
        except:
            print("Неверный формат ID")
            return

    def get_list_shape(self):
        print("-"*100)
        for k, v in self.shapelist.items():
            print(f"ID {k}: {v}")
            print("-"*100)
        
        