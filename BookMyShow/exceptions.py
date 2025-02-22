class NotFoundError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class AlreadyExistError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class SeatAlreadyBookedError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class SeatTemporarilyUnavailableError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class InvalidStateError(Exception):
    def __init__(self, *args):
        super().__init__(*args)