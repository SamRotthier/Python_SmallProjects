import itertools
import string
import time
import os

txt_path = os.path.join(os.path.dirname(__file__), 'words.txt')

def common_guess(word: str) -> str | None:
    """Checks a file filled with common words"""

    with open(txt_path, 'r')as words:
        word_list : list[str] = words.read().splitlines()

    for i, match in enumerate(word_list, start=1):
        if match == word:
            return f'Common Match: {match} (#{i})'
        
# Goes through every combination of chars
def brute_force(word: str, length: int, digits:bool = False, symbols: bool = False) -> str | None:
    """Performs brute force on finding a word"""

    # Modify this for total symbols
    chars: str = string.ascii_lowercase

    if digits:
        chars += string.digits
    
    if symbols:
        chars += string.punctuation

    attempts: int = 0
    for guess in itertools.product(chars, repeat=length):
        attempts +=1
        guess: str = ''.join(guess)

        if guess == word:
            return f'"{word}" was cracked in {attempts:,} guesses.'
         
        print(guess, attempts) # Comment this out when you're not testing (will speed up processing)
         
def hasDigits(s):
    return any(i.isdigit() for i in s)

def hasSymbols(s):
    for i in s:
        if (not i.isnumeric() and not i.isdigit()):
            return True

def main_bruteForce():
    print('Searching...')
    password: str = input('What password should we check for brute force: ') #'bbbbb' #enter word here
    digits_password: bool = hasDigits(password)
    symbols_password: str = hasSymbols(password)

    # Get the start time
    start_time: float = time.perf_counter()

    # Search for common words before using the actual brute force
    if common_match:=common_guess(password):
        print(common_match)
    else:
        for i in range(1,len(password)+1): #Enter the length of the search here, range(3,6) for the example above
            if cracked :=brute_force(password,length= i, digits= digits_password ,symbols=symbols_password):
                print(cracked)
                break
            else:
                print('There was no match...')

    # Get the end time
    end_time: float = time.perf_counter()
    
    # Display the time it took
    print(round(end_time - start_time, 2), 's')


if __name__ == '__main__':
        main_bruteForce()

# Improvements:
#   - Make it more dynamic with user input -> Done