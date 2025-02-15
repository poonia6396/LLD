from .winner_calculator import WinnerCalculator

class BasicWinnerCalculator(WinnerCalculator):

    def is_there_a_winner(self, player_position, board):
        return player_position == board.dimension*board.dimension