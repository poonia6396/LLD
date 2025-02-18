from abc import abstractmethod, ABC
from typing import List

from .elevator_controller import ElevatorController

from model.request import Request


class ElevatorDispatchStrategy(ABC):

    @abstractmethod
    def select_elevator_to_dispatch(self, elevator_controllers: List[ElevatorController], request: Request) -> ElevatorController:
        pass


class BasicElevatorDispatchStrategy(ElevatorDispatchStrategy):

    def select_elevator_to_dispatch(self, elevator_controllers: List[ElevatorController], request: Request) -> ElevatorController:
        pass