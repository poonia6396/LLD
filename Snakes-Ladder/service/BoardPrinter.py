from abc import ABC, abstractmethod

class BoardPrinter(ABC):

    @abstractmethod
    def print_board(self, board):
        pass

class BasicBoardPrinter(BoardPrinter):

    def print_cell_row(self, row, board):
        print("".join("[-------]"for _ in range(board.dimension)))
        print("".join("["+board.cells[row][col].get_value_string()+"]"for col in range(board.dimension)))
        print("".join("["+board.cells[row][col].get_player_string()+"]"for col in range(board.dimension)))
        print("".join("["+board.cells[row][col].get_jump_string()+"]"for col in range(board.dimension)))
        print("".join("[-------]"for _ in range(board.dimension)))
    
    def print_board(self, board):
        for row in range(board.dimension):
            self.print_cell_row(row, board)