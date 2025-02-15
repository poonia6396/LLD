import itertools

class Player:
    id_iter = itertools.count()
    def __init__(self, name):
        self.id = next(self.id_iter)
        self.name = name
        self.position = 0