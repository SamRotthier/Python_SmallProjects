import string
import secrets

def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    
    return False

def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    
    return False

def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    combination: str = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation
    
    if uppercase:
        combination += string.ascii_uppercase
    
    combination_length = len(combination)
    new_password: str = ''

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    if symbols and contains_symbols(new_password) == False:
        return generate_password(length, symbols, uppercase)

    if uppercase and contains_upper(new_password) == False:
       return generate_password(length, symbols, uppercase)


    return new_password


#print(string.punctuation, string.ascii_lowercase, string.ascii_uppercase, string.digits)

def password_generator_start():
    print('How many examples do you want?')
    amount_passwords: int = int(input('Choice (1-99): '))
    print('What length would you like the password examples to be.')
    length_passwords: int = int(input('Choice (1-99): '))
    print('Would you like to use symbols?')
    symbols_passwords: bool = bool(input('Choice (True/False): '))
    print('Would you like to use uppercase?')
    uppercase_passwords: bool = bool(input('Choice (True/False): '))

    for i in range(1,amount_passwords + 1): 
        new_pass: str = generate_password(length=length_passwords, symbols=symbols_passwords, uppercase= uppercase_passwords)
        specs: str = f'U: {contains_upper(new_pass)}, S:{contains_symbols(new_pass)}' 
        print(f'{i}-> {new_pass} ({specs})')

#if __name__ == '__main__':
#    for i in range(1,6): #amounts of passwords generated here 
#        new_pass: str = generate_password(length=10, symbols=True, uppercase= True) #Password parameters here
#        specs: str = f'U: {contains_upper(new_pass)}, S:{contains_symbols(new_pass)}' #Checks if passwords pass the wanted checks
#        print(f'{i}-> {new_pass} ({specs})')
