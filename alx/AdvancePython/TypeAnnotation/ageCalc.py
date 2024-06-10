from datetime import date
def ageCalc(dob: str) -> str:
    current_date = date.today()
    try:
        dob = dob.split(' ')
        dateOfBirth = date(int(dob[2]), int(dob[1]), int(dob[0]))
        # print('dob: {}, current: {}, dateOfBirth: {}'.format(dob, current_date, dateOfBirth))
        date_difference = current_date - dateOfBirth
        return str(date_difference)
    except:
        return 'Not a valid date!'


if __name__ == "__main__":
    dob = input('Enter the DOB in the format (DD MMM YYYY): ')
    print(ageCalc(dob))
