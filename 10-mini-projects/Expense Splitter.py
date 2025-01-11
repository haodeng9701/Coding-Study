def calculate_split(total_amount: float, number_of_people: int, currency: str) -> None:
    # if number_of_people < 1:
    #     raise ValueError('Number of people must be greater than one.')
    
    share_per_person: float = total_amount / number_of_people

    print(f'Total expense: {currency}{total_amount:,.2f}')
    print(f'Number of people: {number_of_people}')
    print(f'Each person should pay: {currency}{share_per_person:,.2f}')

def get_float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f'Invalid input. Please try again.')

def get_int_people(prompt: str) -> int:
    while True:
        try:
            if int(input(prompt)) > 0:
                return int(input(prompt))
            else:
                print('Number of people must be great than 0.')
        except ValueError:
            print(f'Number of people must be integer. Please try again.')    

def main() -> None:
    try:
        total_amount: float = get_float_input('Enter the total amount of the expense: ')
        number_of_people: int = get_int_people('Enter the number of people to share: ')
        calculate_split(total_amount, number_of_people, currency='$')
    except ValueError as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()