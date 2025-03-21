from abc import ABC, abstractmethod

class WinnerCalculator(ABC):

    @abstractmethod
    def is_there_a_winner(self, player_position, board):
        pass


class BasicWinnerCalculator(WinnerCalculator):

    def is_there_a_winner(self, player_position, board):
        return player_position == board.dimension*board.dimension