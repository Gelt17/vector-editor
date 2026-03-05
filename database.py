class ShapeList:
    def __init__(self):
        self.shapelist = dict()
        self.id = 1
    
    def add_shape(self, shape):
        self.shapelist[self.id] = shape
        print(f"ID: {self.id}, Фигура: {str(shape)}")
        self.id += 1
        return self

    def delete_shape(self, id):
        if id in self.shapelist.keys():
            del self.shapelist[id]
            print(f"Фигура с ID {id} удалена.")
        else:
            raise NameError("Неверное ID")

    def get_list_shape(self):
        for k, v in self.shapelist.items():
            print(f"ID {k}: {v}")
        
        