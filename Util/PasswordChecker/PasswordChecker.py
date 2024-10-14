import os

txt_path = os.path.join(os.path.dirname(__file__),'./passwords.txt') #Python_SmallProjects/Util/PasswordChecker/passwords.txt

def check_password(password: str):
    with open(txt_path, 'r') as file:
        common_passwords: list[str] = file.read().splitlines()
        #print(common_passwords)
    
    for i, common_password in enumerate(common_passwords, start=1):
        if password.lower() == common_password: #the .lower it to check even if you have capital letters
            print(f'{password}: ❌ (#{i})')
            return
    print(f'{password}:✅ (Unique)')

def main_passwordChecker():
    user_password: str = input('Enter a password: ')
    check_password(user_password)

if __name__ == '__main__':
    main_passwordChecker()