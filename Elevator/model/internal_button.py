from typing import List
from service.button_dispatcher import ButtonDispatcher

from model.request import Request

class InternalButtonConsole:
    
    def __init__(self, internal_buttons: List[int], internal_button_dispatcher: ButtonDispatcher):
        self.internal_buttons = internal_buttons
        self.internal_button_dispatcher = internal_button_dispatcher
    
    def press_button(self, internal_button, elevator_car_id: int):
        self.internal_button_dispatcher.make_request(Request(internal_button, elevator_id=elevator_car_id))