from service.button_dispatcher import ButtonDispatcher

from model.request import Request

class ExternalButton:
    
    def __init__(self, external_button_dispatcher: ButtonDispatcher):
        self.external_button_dispatcher = external_button_dispatcher
    
    def press(self, floor_number, direction):
        self.external_button_dispatcher.make_request(Request(floor_number, direction))