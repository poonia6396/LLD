class ExternalButton:
    
    def __init__(self, external_button_dispatcher):
        self.external_button_dispatcher = external_button_dispatcher
    
    def press(self, floor_number, direction):
        self.external_button_dispatcher.make_request(floor_number, direction)