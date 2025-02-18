from abc import abstractmethod, ABC
from typing import List

from .elevator_controller import ElevatorController
from model.direction import Direction

from model.request import Request


class ElevatorDispatchStrategy(ABC):

    @abstractmethod
    def select_elevator_to_dispatch(self, elevator_controllers: List[ElevatorController], request: Request) -> ElevatorController:
        pass


class BasicElevatorDispatchStrategy(ElevatorDispatchStrategy):

    def select_elevator_to_dispatch(self, elevator_controllers: List[ElevatorController], request: Request) -> ElevatorController:
        for elevator_controller in elevator_controllers:
            elevator_direction = elevator_controller.get_elevator_direction()
            elevator_floor = elevator_controller.get_elevator_floor()

            if request.direction == elevator_direction:
                if (request.direction == Direction.UP and request.floor < elevator_floor) or (request.direction == Direction.DOWN and request.floor > elevator_floor):
                    return elevator_controller
            
            else:
                if elevator_direction == Direction.IDLE:
                    return elevator_controller
            
        return elevator_controllers[0]