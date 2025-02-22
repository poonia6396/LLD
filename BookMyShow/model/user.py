import itertools

class User:
    id_iter = itertools.count()
    def __init__(self, name):
        self.__id = next(self.id_iter)
        self.__name = name
        