import os

txt_path = os.path.join(os.path.dirname(__file__),'./passwords.txt') #Python_SmallProjects/Util/PasswordChecker/passwords.txt

def check_password(password: str):
    """
    Checks whether a password is in the 100.000 most common passwords.
    Sourced from: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt
    """

    # Open up the file with most common passwords
    with open(txt_path, 'r') as file:
        common_passwords: list[str] = file.read().splitlines()
        #print(common_passwords)
    
    # If any of the words are equal to the password, return True
    for i, common_password in enumerate(common_passwords, start=1):
        if password.lower() == common_password: #the .lower it to check even if you have capital letters
            print(f'{password}: ❌ (#{i})')
            return # Exit the function as soon as we have a match
        
    # If the password is not located in the common passwords, it's unique
    print(f'{password}:✅ (Unique)')

def main_passwordChecker():
    # Check password
    user_password: str = input('Enter a password: ')
    check_password(user_password)

if __name__ == '__main__':
    main_passwordChecker()

# Improvements:
#   - Create a check where it prevents the user for entering nothing (an empty enter will come back as unique)