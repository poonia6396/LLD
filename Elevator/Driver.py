from .ElevatorSystem import ElevatorSystem

from service.button_dispatcher import ButtonDispatcher, ExternalButtonDispatcher, InternalButtonDispatcher
from service.elevator_controller import ElevatorController
from service.elevator_dispatch_strategy import BasicElevatorDispatchStrategy

from model.building import Building
from model.floor import Floor
from model.elevator_car import ElevatorCar
from model.external_button import ExternalButton
from model.internal_button import InternalButton, InternalButtonConsole


class Driver:
    def __init__(self):
        pass

    def __create_floors(self, num, external_button_dispatcher):
        floors = []
        for i in range(num):
            floor = Floor(i, ExternalButton(external_button_dispatcher))
            floors.append(floor)
        return floors

    def __create_elevators(self, num, floor_num, internal_button_dispatcher):
        elevators = []
        for i in range(num):
            internal_buttons = [InternalButton(i) for i in range(floor_num)]
            internal_buttons_console = InternalButtonConsole(internal_buttons, internal_button_dispatcher)
            elevator = ElevatorCar(internal_buttons_console)
            elevators.append[elevator]

        return elevators

    def start_elevator(self):
        external_button_dispatcher = ExternalButtonDispatcher([], BasicElevatorDispatchStrategy())
        interal_button_dispatcher = InternalButtonDispatcher([])
        elevator_system = ElevatorSystem([external_button_dispatcher, interal_button_dispatcher])
        elevators = self.__create_elevators(2, 5, interal_button_dispatcher)
        external_buttons = self.__create_external_buttons(5,external_button_dispatcher)
        floors = self.__create_floors(5,external_buttons)
        building = Building(floors)

          

if __name__ == "__main__":
    driver = Driver()
    driver.start_elevator()