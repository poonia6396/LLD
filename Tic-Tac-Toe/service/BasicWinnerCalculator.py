from service import WinnerCalculator

class BasicWinnerCalculator(WinnerCalculator.WinnerCalculator):

    def is_there_a_winner(self, last_move_cordinates, board_obj):
        row = int(last_move_cordinates[0])
        column = int(last_move_cordinates[1])

        row_check = column_check = diag_check = anti_diag_check = True

        piece = board_obj.board[row][column]
        #check column
        for i in range(board_obj.breadth):
            if board_obj.board[i][column] != piece:
                column_check = False
                break
        
        #check row
        for i in range(board_obj.length):
            if board_obj.board[row][i] != piece:
                row_check = False
                break
        
        if row == column:
            for i in range(board_obj.length):
                if board_obj.board[i][i] != piece:
                    diag_check = False
                    break
        else:
            diag_check = False

        if row + column == board_obj.length-1:
            for i in range(board_obj.length):
                if board_obj.board[i][board_obj.length-i-1] != piece:
                    anti_diag_check = False
                    break
        else:
            anti_diag_check = False

        return row_check or column_check or diag_check or anti_diag_check