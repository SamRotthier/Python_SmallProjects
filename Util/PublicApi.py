#pip install flask
#You can host this code online with https://www.pythonanywhere.com/
#je zou dan met iets als dit de api calls kunnen uitvoeren:
#   import requests
#   request = requests.get('urlOfHost')
#   data=request.json()
#   print(data)

from flask import Flask, request
from random import randint, choice
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    """The home page of our api."""

    # Great the user with some random phrases and the date & time
    phrases: list[str] = ['Welcome to this page!', 'You are looking good today!', 'The weather is great!']
    return {'phrase': choice(phrases),
            'date': datetime.now()}

@app.route('/api/random') # /api/random?number=10000&text=helloworld
def random():
    """The random endpoint of our api."""

    # Define some queries for our api endpoint
    number_input = request.args.get('number', type=int) # you can add "", default=100" to the get /api/random?number=potato => input is 100. At this moment it will trow an error
    text_input = request.args.get('text', type=str, default='default_text') # /api/random?number=100&text=hello

    # Check that the number is of the correct type before doing anything
    if isinstance(number_input,int):
        return{
            'input': number_input,
            'random': randint(0,number_input),
            'text': text_input,
            'date': datetime.now()
        }
    else:
        return {'Error': 'Please only enter numbers.'}

def main_run_publicApi():
    app.run()

if __name__ == '__main__':
    main_run_publicApi()

# Improvements:
#   - Host it live
#   - create dummy data and create advanced functions