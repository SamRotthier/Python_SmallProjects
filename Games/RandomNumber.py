from random import randint

def random_number():
    lower_num, higher_num = 1,10
    random_number : int = randint(lower_num, higher_num)
    print(f'guess the number in the range from {lower_num} to {higher_num}.')

    while True:
        try:
            user_guess : int = int(input('Guess: '))
        except ValueError as e:
            print('Please eneter a valid number.')
            continue

        if user_guess > random_number:
            print('The number is lower')
        elif user_guess < random_number:
            print('The number is higher')
        else:
            print('You guessed it!')
            break