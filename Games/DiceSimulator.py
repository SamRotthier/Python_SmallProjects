import random

def roll_dice(amount: int = 2) -> list [int]:
    if amount <= 0:
        raise ValueError
    
    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1,6)
        rolls.append(random_roll)

    return rolls

def DiceSimulator_main():
    while True:
        try:
            user_input: str = input('How many dice would you like to roll? (stop by typing exit)')

            # To exit the game
            if user_input.lower() == 'exit':
                print('Thanks you for playing!')
                break
            
            # Try to parse the user_input to int
            print(*roll_dice(int(user_input)), sep=', ')
        except ValueError:
            print('(Please enter a valid number)')

if __name__ == '__main__':
    DiceSimulator_main()

#Improvements:
#   - Get total sum of dice rolls









