from database import ShapeList
from shapes import Point, Line, Circle, Square

def main():
    shape_list = ShapeList()
    help_list = """Список всех команд: 
                    add - создать фигуру
                    list - вывести список всех фигур
                    delete - удалить фигуру
                    help - вывести список всех команд
                    exit - выход"""
    print("Вас привествует векторный редактор версии 0.01.")
    print(help_list)
    while True:
        command = input("Введите команду: ").strip()
        if command == "add":
            while True:
                try:
                    print("Если хотите вернуться в предыдущее меню, введите Возврат")
                    shape = input("Введите название фигуры которую вы ходите создать: точка, линия, окружность, квадрат: ").lower().strip()
                    if shape == 'точка':
                        x, y = map(int, input("Введите координаты точки x и y через пробел: ").split())
                        shape_list.add_shape(Point(x, y))
                    elif shape == 'линия':
                        x1, y1, x2, y2 = map(int, input("Введите координаты линии x1 y1 x2 y2 через пробел: ").split())
                        shape_list.add_shape(Line(Point(x1, y1), Point(x2, y2)))
                    elif shape == 'окружность':
                        x, y, r = map(int, input("Введите координаты центра окружности и радиуса x y r через пробел: ").split())
                        shape_list.add_shape(Circle(Point(x, y), r))
                    elif shape == 'квадрат':
                        x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input("Введите координаты вершин квадрата x1 y1 x2 y2 x3 y3 x4 y4 через пробел: ").split())
                        shape_list.add_shape(Square(Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4)))
                    elif shape == 'возврат':
                        break
                    else:
                        print("Неверное название фигуры")
                        continue
                except ValueError as e:
                    print("Введите корректные значения")
                    continue
        elif command == "list":
            shape_list.get_list_shape()
        elif command == "delete":
            while True:
                try:
                    id = int(input("Введите id фигуры: "))
                    shape_list.delete_shape(id)
                except NameError as e:
                    print(str(e))
                except ValueError:
                    print("Введите число")
                finally:
                    break
        elif command == "help":
            print(help_list)
        elif command == "exit":
            break
        else:
            print("Неверно введенная команда")

if __name__ == "__main__":
    main()
        

            
