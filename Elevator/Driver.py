import threading
import time
import random

from ElevatorSystem import ElevatorSystem

from service.button_dispatcher import ExternalButtonDispatcher, InternalButtonDispatcher
from service.elevator_dispatch_strategy import BasicElevatorDispatchStrategy

from model.building import Building
from model.floor import Floor
from model.direction import Direction
from model.elevator_car import ElevatorCar
from model.external_button import ExternalButton
from model.internal_button import InternalButtonConsole


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
            internal_buttons = [i for i in range(floor_num)]
            internal_buttons_console = InternalButtonConsole(internal_buttons, internal_button_dispatcher)
            elevator = ElevatorCar(internal_buttons_console)
            elevators.append(elevator)

        return elevators
    
    def simulate_requests(self, floors, elevators, num_requests, num_floors):
        
        def generate_external_requests():
            
            for _ in range(num_requests):
                # Random floor and random direction for external request
                floor_num = random.randint(0, num_floors - 1)
                direction = random.choice([Direction.UP, Direction.DOWN])
                print(f"[External] Dispatching request: floor {floor_num}, direction {direction}")
                floors[floor_num].press_lift_button(direction)
                time.sleep(random.uniform(0.05, 0.2))  # simulate time between requests

        def generate_internal_requests():
            num_elevators = len(elevators)
            for _ in range(num_requests):
                # Random floor for internal request (no direction)
                floor_num = random.randint(0, num_floors - 1)
                elevator_id = random.randint(0, num_elevators - 1)
                print(f"[Internal] Dispatching request: floor {floor_num}")
                elevators[elevator_id].press_internal_button(floor_num)
                time.sleep(random.uniform(0.05, 0.2))
        
        threads = []
        num_threads = 5  
        
        for _ in range(num_threads):
            t = threading.Thread(target=generate_external_requests)
            threads.append(t)
            t.start()
            time.sleep(0.5)

        
        for _ in range(num_threads):
            t = threading.Thread(target=generate_internal_requests)
            threads.append(t)
            t.start()
            time.sleep(0.5)

        # Wait for all threads to finish generating requests
        for t in threads:
            t.join()

    def test_elevator(self, num_floors, num_elevators):
        external_button_dispatcher = ExternalButtonDispatcher([], BasicElevatorDispatchStrategy())
        internal_button_dispatcher = InternalButtonDispatcher([])
        elevator_system = ElevatorSystem([external_button_dispatcher, internal_button_dispatcher])
        elevators = self.__create_elevators(num_elevators, num_floors, internal_button_dispatcher)

        for elevator in elevators:
            elevator_system.add_elevator(elevator)

        floors = self.__create_floors(num_floors,external_button_dispatcher)
        # building = Building(floors)

        for elevator in elevators:
            elevator_system.start_elevator(elevator.get_id())
        
        simulation_thread = threading.Thread(
            target=self.simulate_requests,
            args=(floors, elevators, 1, num_floors)
        )
        simulation_thread.start()

        simulation_thread.join()
        time.sleep(15)

        for elevator in elevators:
            elevator_system.stop_elevator(elevator.get_id())

        print("Test run complete.")
          

if __name__ == "__main__":
    driver = Driver()
    driver.test_elevator(5,2)