class Board:

    def __init__(self, length = 3, breadth =3):
        self.length = length
        self.breadth = breadth
        self.board = [[None]*breadth for i in range(length)]
    
    def is_valid_move(self, move_cordinates):
        if len(move_cordinates) != 2:
            return False
            
        if not(move_cordinates[0].isdigit() and int(move_cordinates[0]) < self.length):
            return False
        
        if not(move_cordinates[1].isdigit() and int(move_cordinates[0]) < self.breadth):
            return False
        
        return self.board[int(move_cordinates[0])][int(move_cordinates[1])] == None
    
    def register_move(self, move_cordinates, playing_piece):
        
        if self.is_valid_move(move_cordinates):
            row = int(move_cordinates[0])
            column = int(move_cordinates[1])
            self.board[row][column] = playing_piece
            return True
        
        return False

    def has_free_spaces(self):
        for i in range(self.length):
            for j in range(self.breadth):
                if self.board[i][j] == None:
                    return True
        return False
    
    def print_board(self):
        print("\n")
        content = ""
        for i in range(self.length):
            content += "     "+str(i)
        print(content+" ")
        for i in range(self.length):
            content = str(i)+" |"
            for j in range(self.breadth):
                cell_content = " . "
                if self.board[i][j]:
                    cell_content = " "+self.board[i][j].name+" "
                content += " " + cell_content + " |"
            print(content)