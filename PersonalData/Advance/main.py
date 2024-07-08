import logging
import users  # Ensure 'users' module does not interfere with this script's logging

# Define basic arithmetic functions
def subtract(num1, num2):
    return num1 - num2

def add(num1, num2):
    return num1 + num2

def divide(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

# Configure the logger
logger = logging.getLogger('main_logger')
handler = logging.StreamHandler()
file_handler = logging.FileHandler('sample.log')

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(handler)

num1 = 20
num2 = 5

if __name__ == '__main__':
    result = add(num2, num1)
    logger.debug(f'Add result: {result}')
    result = subtract(num1, num2)
    logger.debug(f'Subtract result: {result}')
    result = divide(num1, num2)
    logger.debug(f'Divide result: {result}')
    result = multiply(num1, num2)
    logger.debug(f'Multiply result: {result}')
