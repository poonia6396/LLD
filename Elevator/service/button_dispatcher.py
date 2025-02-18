from abc import ABC, abstractmethod
from typing import List

from .elevator_controller import ElevatorController
from .elevator_dispatch_strategy import ElevatorDispatchStrategy

from model.request import Request


class ButtonDispatcher(ABC):

    @abstractmethod
    def make_request(self, request: Request):
        pass


class InternalButtonDispatcher(ButtonDispatcher):

    def __init__(self, elevator_controllers: List[ElevatorController]):
        self.elevator_controllers = elevator_controllers
    
    def make_request(self, request: Request):
        elvator_id = request.elevator_id
        for elevator_controller in self.elevator_controllers:
            if elevator_controller.get_elevator_id() == elvator_id:
                elevator_controller.accept_request(request)


class ExternalButtonDispatcher(ButtonDispatcher):

    def __init__(self, elevator_controllers: List[ElevatorController], elevator_dispatch_strategy: ElevatorDispatchStrategy):
        self.elevator_controllers = elevator_controllers
        self.elevator_dispatch_strategy = elevator_dispatch_strategy
    
    def make_request(self, request: Request):
        elevator_controller = self.elevator_dispatch_strategy.select_elevator_to_dispatch(self.elevator_controllers, request)
        elevator_controller.accept_request(request)