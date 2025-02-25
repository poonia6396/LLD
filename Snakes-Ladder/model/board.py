from .cell import Cell
from service import BoardPrinter

class Board:

    def __init__(self, dimension, board_printer: BoardPrinter):
        self.dimension = dimension
        self.cells = [[Cell((row*dimension) + col + 1) for col in range(dimension)] for row in range(dimension)]
        self.board_printer = board_printer
    
    def get_cell_from_position(self, position):
        if position > 0 and position < (self.dimension*self.dimension):
            row = int((position-1)/self.dimension)
            col = position%self.dimension - 1
            return self.cells[row][col]
        return None
    
    def check_for_jumps(self, player_position):

        while True:
            cell = self.get_cell_from_position(player_position)
            if cell is None or cell.jump is None:
                break
            print("Jumping from position:",player_position,"to position:",cell.jump.end)
            player_position = cell.jump.end

        return player_position

    def register_move(self, dice_val, player):

        curr_cell = self.get_cell_from_position(player.position)
        if curr_cell is not None:
            curr_cell.players.remove(str(player.id))

        if player.position + dice_val <= self.dimension*self.dimension:
            player.position = player.position + dice_val
            player.position = self.check_for_jumps(player.position)

        new_cell = self.get_cell_from_position(player.position)
        if new_cell is not None:
            new_cell.players.append(str(player.id))

        return player.position

    def print_board(self):
        self.board_printer.print_board(self)
    


    


