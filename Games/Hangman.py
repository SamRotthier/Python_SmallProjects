from random import choice
import string

def Hangman_game(): #run_game
    word: str = choice(['apple','secret','banana'])

    # A friendly interactive welcome Message
    username: str = input('What is your name? >>')
    print(f'Welcome to hangman,{username}!')

    # Setup
    guessed: str = ''
    tries: int = 3

    # The game
    while tries > 0:
        blanks: int = 0
        
        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks +=1

        print() # Adds a blank line

        # If there are no blanks left, that means the user won the game!
        if blanks == 0:
            print('You got it!')
            break

        # Get User input
        guess: str = input('Enter a letter: ')

        # Checks that the user isn't just guessing the same letter again
        if guess in guessed:
            print(f'You already used: "{guess}". Please try with another letter!')
            continue
        if len(guess)>1:
            print(f'You can not guess more then 1 letter')
            continue
        if guess in string.digits:
            print(f'You can not guess a number')
            continue

        # Adds the guess to the guessed string
        guessed += guess

        # Checks that the guess is in the word
        if guess not in word:
            tries -= 1
            print(f'Sorry, that was wrong ... ({tries} tries remaining)')

            # Game-over if tries reaches 0
            if tries == 0:
                print ('No more tries remaining ... You lose.')
                break

if __name__ == '__main__':
    Hangman_game()

#Improvements:
#   - Currently we can add multiple letters and it would only see it as 1 turn (check for only 1 letter or for the full word)
#   - Get the words from a different csv file