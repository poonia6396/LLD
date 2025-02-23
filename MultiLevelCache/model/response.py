class ReadResponse:

    def __init__(self, value, response_time):
        self.__value = value
        self.__response_time = response_time
    
    def get_value(self):
        return self.__value
    
    def get_response_time(self):
        return self.__response_time


class WriteResponse:

    def __init__(self, response_time):
        self.__response_time = response_time
    
    def get_response_time(self):
        return self.__response_time
