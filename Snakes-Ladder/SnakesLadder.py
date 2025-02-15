from model.dice import Dice
class SnakesLadder:

    def __init__(self, winner_calculator, board_generator, players):
        self.players = players
        self.board_generator = board_generator
        self.winner_calculator = winner_calculator
        self.dice = Dice(1)

    def initialise_board(self, num_of_snakes, num_of_ladders, board_dimensions):
        self.board = self.board_generator.generate_board(num_of_snakes, num_of_ladders, board_dimensions)

    def start_game(self):

        while True:

            self.board.print_board()

            current_player = self.players.pop(0)
            input("\n\n"+current_player.name+" Press enter to roll the dice: \n")
            player_dice_val = self.dice.roll_dice()
            print(current_player.name,"got", player_dice_val, "on dice")
            current_player.position = self.board.register_move(player_dice_val, current_player)
        
            self.players.append(current_player)

            if self.is_there_a_winner(current_player.position):
                self.board.print_board()
                return current_player.name + " wins!!"

    def is_there_a_winner(self, players_position):
        return self.winner_calculator.is_there_a_winner(players_position, self.board)