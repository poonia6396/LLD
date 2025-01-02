from direction import Direction

class ElevatorCar:
    
    def __init__(self, internal_button_console, display):
        self.internal_button_console = internal_button_console
        self.display = display
        self.current_floor = 0
        self.direction = Direction.UP

    def move(self, destination_floor):
        direction_adder = 0
        if self.current_floor > destination_floor:
            self.direction = Direction.DOWN
            direction_adder = -1
        else:
            self.direction = Direction.UP
            direction_adder = 1
        
        while self.current_floor != destination_floor:
            self.current_floor += direction_adder
            print("Lift at "+str(self.current_floor)+" and going "+self.direction.name)