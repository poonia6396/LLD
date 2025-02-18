from model.elevator_car import ElevatorCar
from service.elevator_controller import ElevatorController

class ElevatorSystem:

    def __init__(self, button_dispatchers):
        self.button_dispatchers = button_dispatchers
        self.elevator_controllers = []
    
    def __get_controller_with_id(self, elevator_controllers, elevator_id):
        for elevator_controller in elevator_controllers:
            if elevator_controller.get_elevator_id() == elevator_id:
                return elevator_controller
            
    def __remove_controller_with_id(self, elevator_controllers, elevator_id):
        elevator_controller = self.__get_controller_with_id(elevator_controllers, elevator_id)
        elevator_controllers.remove(elevator_controller)

    def add_elevator(self, elevator: ElevatorCar):
        elevator_controller = ElevatorController(elevator)
        self.elevator_controllers.append(elevator_controller)
        for button_dispatcher in self.button_dispatchers:
            button_dispatcher.elevator_controllers.append(elevator_controller)
    
    def remove_elevator(self, elevator_id: int):
        self.__remove_controller_with_id(self.elevator_controllers, elevator_id)
        for button_dispatcher in self.button_dispatchers:
            self.__remove_controller_with_id(button_dispatcher.elevator_controllers, elevator_id)
    
    def start_elevator(self, elevator_id: int):
        elevator_controller = self.__get_controller_with_id(self.elevator_controllers, elevator_id)
        elevator_controller.start()
    
    def stop_elevator(self, elevator_id: int):
        elevator_controller = self.__get_controller_with_id(self.elevator_controllers, elevator_id)
        elevator_controller.stop()