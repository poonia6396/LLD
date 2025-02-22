from typing import List

from model.user import User

class UserService:

    def __init__(self):
        self.__users = {}
    
    def create_user(self, username):
        if username in self.__users:  
            print("User creation failed. User with username:", username, "exists.")
        user = User(username)
        self.__users.append(user)
        return user
    
    def remove_user(self, username):
        if username in self.__users:
            self.__users.pop(username)
            return True
        print("User with username:", username, "not found")
        return False