from database import ShapeList
from shapes import Point, Line, Circle, Square
from filemanager import FileManager

def main():
    shape_list = ShapeList()
    help_list = """Список всех команд: 
                    add point <x> <y> - создать точку
                    add line <x1> <y1> <x2> <y2>- создать линию
                    add circle <x1> <y1> <radius> - создать окружность
                    add square <x1> <y1> <x2> <y2> <x3> <y3> <x4> <y4> - создать квадрат
                    add oval <x1> <y1> <radius1> <radius2> - создать овал
                    add rectangle <x1> <y1> <x2> <y2> <x3> <y3> <x4> <y4> - создать прямоугольник
                    list - вывести список всех фигур
                    delete - удалить фигуру
                    help - вывести список всех команд
                    load <имя файла> - загрузить из файла
                    save <имя файла> - сохранить в файл
                    exit - выход"""
    print("Вас привествует векторный редактор версии 0.02.\n Для вывода списка всех команд, введите help")
    while True:
        command = input("Введите команду: ").split()
        if command[0] == "add":
            shape_list.add_shape(command[1], command[2:])
        elif command[0] == "list":
            shape_list.get_list_shape()
        elif command[0] == "delete":
            shape_list.delete_shape(command[1])
        elif command[0] == "help":
            print(help_list)
        elif command[0] == "load":
            shape_list = ShapeList(FileManager.load_file(command[1]))
        elif command[0] == "save":
            FileManager.save_file(shape_list.shapelist, command[1])
        elif command[0] == "exit":
            break
        else:
            print("Неверно введенная команда")

if __name__ == "__main__":
    main()
