import uuid
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
logger.propagate = False
handler = logging.StreamHandler()
file_handler = logging.FileHandler('users.log')

logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(handler)

class User:
    userDB = []

    def __init__(self, username, password):
        self._username = username
        self._password = password

        user = self.add_user()
        User.userDB.append(user)
        
        logger.info(f'User {user["username"]} added successfully with ID {user["userId"]}')
    
    @property
    def user_id(self):
        return uuid.uuid4()
    
    def add_user(self):
        userData = {
            'username': self._username,
            'password': self._password,  # In a real application, passwords should be hashed.
            'userId': self.user_id,
            'created_at': datetime.now()
        }
        return userData
    
if __name__ == '__main__':
    user1 = User('taya', 'taya1234')
    user2 = User('brett', 'cooper123')
