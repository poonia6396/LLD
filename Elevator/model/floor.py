class Floor:
    
    def __init__(self, floor_number, external_buuton):
        self.floor_number = floor_number
        self.external_button = external_buuton
    
    def press_lift_button(self, direction):
        self.external_button.press(self.floor_number, direction)