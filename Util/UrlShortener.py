# Pip install requests
#https://cutt.ly/
#Example link to use: https://www.python.org/doc/ -> This gave https://cutt.ly/neSCBhA3

from typing import Final
import requests

# Constants
API_KEY: Final[str]='3b4364b4ce4fc9bf8f5ab9512c06b1fa' #Api key from tutorial, this account can only do 30 shortens per month so might not work because of that
BASE_URL: Final[str]= 'https://cutt.ly/api/api.php'

# Function to shorten any link with a custom name
def shorten_link(full_link: str):
    payload: dict = {'key': API_KEY, 'short': full_link}
    request = requests.get(BASE_URL, params=payload)
    data: dict=  request.json()

    # Gets the relevant information we need
    if url_data := data.get('url'):
        if url_data['status'] == 7:
            short_link: str = url_data['shortLink']
            print('Link: ',short_link)
        else:
            print('Errpr status: ', url_data['status'])

def main_url_shortener():
    # Take user input
    input_link: str = input('Enter a link: ')

    # Shorten the link
    shorten_link(input_link)

if __name__ == '__main__':
    main_url_shortener()

# Improvements:
#   - Implement other statusses from api