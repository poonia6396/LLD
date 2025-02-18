import itertools
import time

from .direction import Direction


class ElevatorCar:
    id_iter = itertools.count()
    def __init__(self, internal_button_console, display):
        self.__id = next(self.id_iter)
        self.internal_button_console = internal_button_console
        self.display = display
        self.__current_floor = 0
        self.__direction = Direction.UP

    def move(self, destination_floor):
        direction_adder = 0
        if self.__current_floor > destination_floor:
            self.__direction = Direction.DOWN
            direction_adder = -1
        else:
            self.__direction = Direction.UP
            direction_adder = 1
        
        while self.__current_floor != destination_floor:
            self.__current_floor += direction_adder
            print("Lift at "+str(self.__current_floor)+" and going "+self.__direction.name)
            time.sleep(1)
    
    def get_id(self) -> int:
        return self.__id

    def get_direction(self) -> Direction:
        return self.__direction
    
    def set_direction(self, direction: Direction):
        self.__direction = direction

    def get_current_floor(self) -> int:
        return self.__current_floor