#pip install requests
#pip install fake_useragent
import csv
import requests 
from fake_useragent import UserAgent
from http import HTTPStatus
import os

csv_path = os.path.join(os.path.dirname(__file__),'./website.csv') #Python_SmallProjects/Util/WebsiteChecker/website.csv

def get_websites(csv_path: str) -> list[str]:
    websites: list[str] = []
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' not in row[1]: #or 'http://' in row[1]:
                websites.append(f'https://{row[1]}')
            else:
                websites.append(row[1])
        
        return websites
   
#print(get_websites(csv_path))

def get_user_agent() -> str:
    ua = UserAgent()
    return ua.chrome #if you get back a forbidden, you can try other agents

#print(get_user_agent())

def get_status_description(status_code: int) -> str:
    for value in HTTPStatus:
        if value == status_code:
            description: str = f'({value} {value.name}) {value.description}'
            return description
        
    return '(???) Unknown status code'

def check_website(website: str, user_agent):
    try:
        code: int = requests.get(website,headers={'User-Agent': user_agent}).status_code
        print(website,get_status_description(code))
    except Exception:
        print(f'**Could not get information for the website:"{website}"')
    
def main_websiteChecker():
    sites: list[str] = get_websites(csv_path)
    user_agent: str = get_user_agent()

    for site in sites:
        check_website(site, user_agent)

if __name__ == '__main__':
        main_websiteChecker()