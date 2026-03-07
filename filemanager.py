import json

class FileManager:
    @staticmethod
    def save_file(database: dict, path_file: str):
        if path_file.endswith(".json"):
            with open(path_file, "w+", encoding="utf-8") as file:
                json.dump(database, file, ensure_ascii=False)
                print(f"Данные записаны в файл {str(file.name)}")
        else:
            print("Неверный формат файла")
            return 

    @staticmethod
    def load_file(path_file: str) -> dict:
        if path_file.endswith(".json"):
            with open(path_file, "r", encoding="utf-8") as file:
                loaded_data = json.load(file)
                print(f"Данные загружены из файла {str(file.name)}")
            return loaded_data
        else:
            print("Неверный формат файла")
            return 