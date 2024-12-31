class TicTacToe:

    def __init__(self, board, players, winner_calculator):
        self.board = board
        self.players = players
        self.winner_calculator = winner_calculator
    
    def is_valid_move_cordinates(self, move_cordinates):
        if len(move_cordinates) != 2:
            return False
            
        if not(move_cordinates[0].isdigit() and int(move_cordinates[0]) < self.board.length):
            return False
        
        if not(move_cordinates[1].isdigit() and int(move_cordinates[0]) < self.board.breadth):
            return False

        return True

    def is_there_a_winner(self, move_cordinates):
        return self.winner_calculator.is_there_a_winner(move_cordinates, self.board)


    def start_game(self):
        no_winner = False
        while not no_winner:
            
            self.board.print_board()
            if not self.board.has_free_spaces():
                no_winner = True
                break

            current_player = self.players.pop(0)
            
            player_input = input("\n\n"+current_player.name+" please enter your move cordinates: (e.g row,column)\n")
            move_cordinates = player_input.split(",")

            if not self.is_valid_move_cordinates(move_cordinates) or not self.board.register_move(move_cordinates, current_player.player_piece):
                print("Not a valid move. Please retry")
                self.players.insert(0, current_player)
                continue
            
            self.players.append(current_player)

            if self.is_there_a_winner(move_cordinates):
                self.board.print_board()
                return current_player.name + " wins!!"

        return "It's a Tie"
