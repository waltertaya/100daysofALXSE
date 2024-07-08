import uuid
from datetime import datetime

import logging

logging.basicConfig(filename='users.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password

        userDB = []

        userDB.append(self.add_user())
        
        # print(f'Added {self._username} successfully to the database')
        logging.info(f'User {str(userDB)} added successfully')
    
    @property
    def user_id(self):
        return uuid.uuid4()
    
    def add_user(self):
        userData = {}

        userData['username'] = self._username
        userData['password'] = self._password
        userData['userId'] = self.user_id
        userData['created_at'] = datetime.now()

        return userData
    
if __name__ == '__main__':
    user1 = User('taya', 'taya1234')
    user2 = User('brett', 'cooper123')
