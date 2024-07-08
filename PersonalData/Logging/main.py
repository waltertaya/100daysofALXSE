import logging

def subtract(num1, num2):
    return num1 - num2

def add(num1, num2):
    return num1 + num2

def divide(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

logging.basicConfig(filename='test.log',format='%(asctime)s:%(levelname)s:%(message)s' ,level=logging.DEBUG)

num1 = 20
num2 = 5

if __name__ == '__main__':
    result = add(num2, num1)
    logging.debug(f'Add result: {result}')
    result = subtract(num1, num2)
    logging.debug(f'Subtract result: {result}')
    result = divide(num1, num2)
    logging.debug(f'Divide result: {result}')
    result = multiply(num1, num2)
    logging.debug(f'Multiply result: {result}')
