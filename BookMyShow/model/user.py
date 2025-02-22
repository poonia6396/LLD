import itertools

class User:
    id_iter = itertools.count()
    def __init__(self, name):
        self.__id = next(self.id_iter)
        self.__name = name
    
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
        