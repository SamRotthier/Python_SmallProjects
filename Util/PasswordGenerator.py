import string
import secrets

def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    
    return False # There were no uppercase chars

def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    
    return False # There were no uppercase chars

def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    """
    Generates a password based on the users specifications

    :param length: The length of the password
    :param symbols: Password should include symbols
    :param upparcase: Password should include uppercase letters
    :return: str
    """

    # Create a combination of characters to choose from
    combination: str = string.ascii_lowercase + string.digits

    # If the user wants symbols, add punctuation to the combination
    if symbols:
        combination += string.punctuation
    
    # If the user wants uppercase, add uppercase to the combination
    if uppercase:
        combination += string.ascii_uppercase
    
    #Get the length of the combination characters
    combination_length = len(combination)

    #create a new password variable
    new_password: str = ''

    # Append to the new_password a new random character for each iteration
    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    # Makes sure there is a symbol if needed
    if symbols and contains_symbols(new_password) == False:
        return generate_password(length, symbols, uppercase)

    # Makes sure there is an uppercase if needed
    if uppercase and contains_upper(new_password) == False:
       return generate_password(length, symbols, uppercase)


    return new_password


#print(string.punctuation, string.ascii_lowercase, string.ascii_uppercase, string.digits)

def password_generator_start(): # Dynamic questions to generate a password
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

if __name__ == '__main__':
    for i in range(1,6): #amounts of passwords generated here 
        new_pass: str = generate_password(length=10, symbols=True, uppercase= True) #Password parameters here
        specs: str = f'U: {contains_upper(new_pass)}, S:{contains_symbols(new_pass)}' #Checks if passwords pass the wanted checks
        print(f'{i}-> {new_pass} ({specs})')

# Improvements:
#   - Make sure the options (uper and symbols) are in the password when needed -> Done
#   - Make it more dynamic -> Done