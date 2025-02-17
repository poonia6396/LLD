from typing import List
from service.button_dispatcher import ButtonDispatcher

class InternalButton:
    def __init__(self, value):
        self.value = value


class InternalButtonConsole:
    
    def __init__(self, internal_buttons: List[InternalButton], internal_button_dispatcher: ButtonDispatcher):
        self.internal_buttons = internal_buttons
        self.internal_button_dispatcher = internal_button_dispatcher
    
    def press_button(self, internal_button, elevator_car):
        self.internal_button_dispatcher.make_request(internal_button.value, elevator_car)