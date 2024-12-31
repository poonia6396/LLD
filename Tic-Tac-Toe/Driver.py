from TicTacToe import TicTacToe
from model import Player, PlayerPiece, Board
from service.BasicWinnerCalculator import BasicWinnerCalculator


class Driver:
    def __init__(self):
        pass

    def play(self):
        x_piece = PlayerPiece.PlayerPiece.X
        o_piece = PlayerPiece.PlayerPiece.O
        player_1 = Player.Player("Player1", x_piece)
        player_2 = Player.Player("Player2", o_piece)

        board = Board.Board()
        basic_winner_calculator = BasicWinnerCalculator()
        game = TicTacToe(board, [player_1, player_2], basic_winner_calculator)
        result = game.start_game()

        print(result)

if __name__ == "__main__":
    driver = Driver()
    driver.play()