def kgToLb(kgs: float) -> str:
    lbs = int(kgs * 2.204623) # weight in pounds
    return f'{lbs} lbs'


if __name__ == '__main__':
    kgs = input('Enter your weight (kgs): ')
    try:
        print(kgToLb(float(kgs)))
    except:
        print('Enter valid weight in kg')
