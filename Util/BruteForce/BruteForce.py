import itertools
import string
import time
import os

txt_path = os.path.join(os.path.dirname(__file__), 'words.txt')

def common_guess(word: str) -> str | None:
    with open(txt_path, 'r')as words:
        word_list : list[str] = words.read().splitlines()

    for i, match in enumerate(word_list, start=1):
        if match == word:
            return f'Common Match: {match} (#{i})'
        

def brute_force(word: str, length: int, digits:bool = False, symbols: bool = False) -> str | None:
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
         
        print(guess, attempts)
         
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

    start_time: float = time.perf_counter()

    if common_match:=common_guess(password):
        print(common_match)
    else:
        for i in range(1,len(password)+1): #Enter the length of the search here, range(3,6) for the example above
            if cracked :=brute_force(password,length= i, digits= digits_password ,symbols=symbols_password):
                print(cracked)
                break
            else:
                print('There was no match...')

    end_time: float = time.perf_counter()
    print(round(end_time - start_time, 2), 's')


if __name__ == '__main__':
        main_bruteForce()

