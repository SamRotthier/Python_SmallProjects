#pip install flask
#You can host this code online with https://www.pythonanywhere.com/
#je zou dan met iets als dit de api calls kunnen uitvoeren:
#import requests
#request = requests.get('urlOfHost')
#data=request.json()
#print(data)

from flask import Flask, request
from random import randint, choice
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    phrases: list[str] = ['Welcome to this page!', 'You are looking good today!', 'The weather is great!']
    return {'phrase': choice(phrases),
            'date': datetime.now()}

@app.route('/api/random')
def random():
    number_input = request.args.get('number', type=int) # you can add "", default=100" to the get /api/random?number=potato => input is 100. At this moment it will trow an error
    text_input = request.args.get('text', type=str, default='default_text') # /api/random?number=100&text=hello

    if isinstance(number_input,int):
        return{
            'input': number_input,
            'random': randint(0,number_input),
            'text': text_input,
            'date': datetime.now()
        }
    else:
        return {'Error': 'Please only enter numbers.'}

if __name__ == '__main__':
    app.run()