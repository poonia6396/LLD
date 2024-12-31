from abc import ABC, abstractmethod

class WinnerCalculator(ABC):

    @abstractmethod
    def is_there_a_winner(self, last_move_cordinates, board):
        pass
