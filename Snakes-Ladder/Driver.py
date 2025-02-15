from SnakesLadder import SnakesLadder
from model import player
from service.basic_winner_calculator import BasicWinnerCalculator
from service.BoardGenerator import BasicBoardGenerator

class Driver:
    def __init__(self):
        pass

    def play(self):
        
        player_1 = player.Player("Player1")
        player_2 = player.Player("Player2")


        basic_winner_calculator = BasicWinnerCalculator()
        basic_board_generator = BasicBoardGenerator()
        game = SnakesLadder(basic_winner_calculator, basic_board_generator, [player_1, player_2])
        game.initialise_board(5, 5, 10)
        result = game.start_game()

        print(result)

if __name__ == "__main__":
    driver = Driver()
    driver.play()