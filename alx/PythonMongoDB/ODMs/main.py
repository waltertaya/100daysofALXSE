import ODMs.mongo_setup as mongoSetup
from ODMs.customer_model import Customer
from ODMs.owner_model import Owner

from datetime import datetime

mongoSetup.global_init()


def register_customer():
    full_name = input("Enter your full name: ")
    length = int(input("Enter your length: "))
    user_id = input("Enter a unique user ID: ")
    
    customer = Customer(
        registered_date=datetime.now(),
        full_name=full_name,
        length=length,
        user_id=user_id
    )
    customer.save()
    print(f"Customer {full_name} registered successfully!")

def view_customers():
    customers = Customer.objects()
    for customer in customers:
        print(customer.to_json())

def register_owner():
    full_name = input("Enter your full name: ")
    length = int(input("Enter your length: "))
    user_id = input("Enter a unique user ID: ")
    
    owner = Owner(
        lease_date=datetime.now(),
        full_name=full_name,
        length=length,
        user_id=user_id
    )
    owner.save()
    print(f"Owner {full_name} registered successfully!")

def view_owners():
    owners = Owner.objects()
    for owner in owners:
        print(owner.to_json())

condition = True

while condition:
    print('''
          Welcome to the Waltertaya AirBnB\n
          Choose the options below\n
          You are:\n
          0. Exit
          1. Customer
          2. Owner
          ''')
    choice = input('Enter your choice: ')
    if choice == '0':
        break
    elif choice == '1':
        print('''
              Customer Options:\n
              1. Register
              2. View all customers
              ''')
        customer_choice = input('Enter your choice: ')
        if customer_choice == '1':
            register_customer()
        elif customer_choice == '2':
            view_customers()
        else:
            print('Enter valid choice')
    elif choice == '2':
        print('''
              Owner Options:\n
              1. Register
              2. View all owners
              ''')
        owner_choice = input('Enter your choice: ')
        if owner_choice == '1':
            register_owner()
        elif owner_choice == '2':
            view_owners()
        else:
            print('Enter valid choice')
    else:
        print('Enter valid choice')