from queue import Queue
import heapq
import time
import threading

from model.elevator_car import ElevatorCar
from model.request import Request
from model.direction import Direction

class ElevatorController:

    def __init__(self, elevator_car: ElevatorCar):
        self.__elevator_car = elevator_car
        self.__queue = Queue()
        self.__down_requests = []
        self.__up_requests = []
        self.__lock = threading.Lock()
        self.__running = False

    def get_elevator_id(self):
        return self.__elevator_car.get_id()
    
    def accept_request(self, request: Request) -> bool:
        elevator_direction = self.__elevator_car.get_direction()
        elevator_floor = self.__elevator_car.get_current_floor()
        
        with self.__lock:
            if request.direction:
                if request.direction == elevator_direction:
                    if (request.direction == Direction.UP and request.floor < elevator_floor) or (request.direction == Direction.DOWN and request.floor > elevator_floor):
                        self.__queue.put(request.floor)
                    else:
                        if request.direction == Direction.UP:
                            heapq.heappush(self.__up_requests, request.floor)
                        if request.direction == Direction.DOWN:
                            heapq.heappush(self.__down_requests, -request.floor)
                else:
                    if request.direction == Direction.UP:
                        heapq.heappush(self.__up_requests, request.floor)
                    if request.direction == Direction.DOWN:
                        heapq.heappush(self.__down_requests, -request.floor)
            else:
                if (elevator_direction == Direction.UP and request.floor < elevator_floor) or (elevator_direction == Direction.DOWN and request.floor > elevator_floor):
                    print("Invalid Request. Can't accept it")
                    return False
                
                if elevator_direction == Direction.UP:
                    heapq.heappush(self.__up_requests, request.floor)
                if elevator_direction == Direction.DOWN:
                    heapq.heappush(self.__down_requests, -request.floor)
        return True

    def process_next_request(self):

        elevator_direction = self.__elevator_car.get_direction()
        next_floor = None
        
        with self.__lock:
            if elevator_direction == Direction.UP:
                if self.__up_requests:
                    next_floor = heapq.heappop(self.__up_requests)
                elif self.__down_requests:
                    # No more upward stops; change direction.
                    self.__elevator_car.set_direction(Direction.DOWN)
                    next_floor = -heapq.heappop(self.__down_requests)
            elif elevator_direction == Direction.DOWN:
                if self.__down_requests:
                    next_floor = -heapq.heappop(self.__down_requests)
                elif self.__up_requests:
                    self.__elevator_car.set_direction(Direction.UP)
                    next_floor = heapq.heappop(self.__up_requests)
            else:
                # Elevator is idle. Decide based on available requests.
                if self.__up_requests:
                    self.__elevator_car.set_direction(Direction.UP)
                    next_floor = heapq.heappop(self.__up_requests)
                elif self.__down_requests:
                    self.__elevator_car.set_direction(Direction.DOWN)
                    next_floor = -heapq.heappop(self.__down_requests)

        if next_floor is not None:
            self.__move_to_floor(next_floor)
        else:
            # No pending requests.
            time.sleep(1)

    def __move_to_floor(self, destination_floor):
        self.__elevator_car.move(destination_floor)

    def __run(self):
        while self.__running:
            self.process_next_request()

    def start(self):
        if not self.__running:
            self.__running = True
            threading.Thread(target=self.__run, daemon=True).start()

    def stop(self):
        self.__running = False