import random

def emailGenerator(firstName: str, lastName: str) -> str:
    try:
        if (firstName == '' or lastName == ''):
            raise Exception('Enter valid names')
        number = random.choice([22, 23, 18, 19, 20, 21])
        return f'{firstName}.{lastName}{number}@students.dkut.ac.ke'
    except:
        return 'Enter valid names'

if __name__ == '__main__':
    firstName = input('Enter your first name: ')
    lastName = input('Enter your last name: ')
    print(emailGenerator(firstName, lastName))