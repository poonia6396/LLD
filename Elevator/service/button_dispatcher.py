from abc import ABC, abstractmethod

class ButtonDispatcher(ABC):

    @abstractmethod
    def make_request():
        pass


class InternalButtonDispatcher(ButtonDispatcher):

    def __init__(self, elevator_controllers):
        self.elevator_controllers = elevator_controllers
    
    def make_request():
        pass

class ExternalButtonDispatcher(ButtonDispatcher):

    def __init__(self, elevator_controllers):
        self.elevator_controllers = elevator_controllers
    
    def make_request():
        pass