from cell import Cell

class Board:

    def __init__(self, dimension):
        self.dimension = dimension
        self.cells = [[Cell() for i in range(dimension)] for i in range(dimension)]