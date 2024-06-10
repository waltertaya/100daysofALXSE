import time
def drinkCoffee():
    print('Pour coffee into the cup and start drinking')
    time.sleep(3)
    print('Finish drinking coffee')
    return 'Finished drinking coffee, start next task'

def study():
    print('Start studying for the exams')
    time.sleep(8)
    print('Take a break')
    return 'Finished reading'

def main():
    start_time = time.time()
    result_drink = drinkCoffee()
    result_study = study()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Result for drinking coffee: {result_drink}')
    print(f'Result for studying for exams: {result_study}')
    print(elapsed_time)
    return

if __name__ == '__main__':
    main()