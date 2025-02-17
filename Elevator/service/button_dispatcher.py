from abc import ABC, abstractmethod
from typing import List
from .elevator_controller import ElevatorController
class ButtonDispatcher(ABC):

    @abstractmethod
    def make_request():
        pass


class InternalButtonDispatcher(ButtonDispatcher):

    def __init__(self, elevator_controllers: List[ElevatorController]):
        self.elevator_controllers = elevator_controllers
    
    def make_request():
        pass

class ExternalButtonDispatcher(ButtonDispatcher):

    def __init__(self, elevator_controllers: List[ElevatorController]):
        self.elevator_controllers = elevator_controllers
    
    def make_request():
        pass