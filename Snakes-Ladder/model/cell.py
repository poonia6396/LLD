class Cell:

    def __init__(self, value):
        self.value = value
        self.jump = None
        self.players = []
    
    def add_extra_spaces(self, info_string):
        extra_spaces = 7 - len(info_string)
        for i in range(int(extra_spaces/2)):
            info_string = " " + info_string
        
        for i in range(extra_spaces - int(extra_spaces/2)):
            info_string += " "
        
        return info_string

    def get_player_string(self):
        players_info = "P:" + ",".join(self.players)
        players_info = self.add_extra_spaces(players_info)    
        return players_info

    def get_jump_string(self):
        if self.jump is not None:
            if self.jump.start > self.jump.end:
                jump_string = "SN"
            else:
                jump_string = "LD"
            jump_string += "->" + str(self.jump.end)
        else:
            jump_string = "NA"
        jump_string = self.add_extra_spaces(jump_string)    
        return jump_string

    def get_value_string(self):
        value_string = str(self.value)
        value_string = self.add_extra_spaces(value_string)    
        return value_string

    def print_cell(self):
        players_string = self.get_player_string()
        jump_string = self.get_jump_string()
        value_string = self.get_value_string()
        print("[-------]")
        print("[",value_string,"]")
        print("[",players_string,"]")
        print("[",jump_string,"]")
        print("[-------]")