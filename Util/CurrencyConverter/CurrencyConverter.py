#exchangeratesapi.io

import json
from typing import Final
import requests
import os

rates_path = os.path.join(os.path.dirname(__file__), 'rates.json')

# Constant
BASE_URL: Final[str] = 'http://api.exchangeratesapi.io/v1/latest'
API_KEY: Final[str] = 'cc28e1d462039055c5b3024d734bd632'

def get_rates(mock: bool = False) -> dict: 
    """Get the current rates from a currency api"""

    if mock:
        with open(rates_path , 'r') as file:#r -> read mode
            return json.load(file)
    
    # Make a live request for data
    payload: dict = {'access_key' : API_KEY}
    request = requests.get(url=BASE_URL,params=payload)
    data: dict = request.json()

    #Code below was used to make the rates.json file
    #with open('rates.json', 'w') as file: #w -> write mode
    #    json.dump(data, file)

    return data

#get_rates()
#print(get_rates(mock= True))

def get_currency(currency: str, rates: dict) -> float:
    """Get the exchange rate for the specified currency if it exists."""

    currency: str = currency.upper()
    if currency in rates.keys():
        return rates.get(currency)
    else:
        raise ValueError(f'"{currency}" is not a valid currency.')

def convert_currency(amount: float, base: str, vs: str, rates: dict) -> float:
    """Convert the base currency to the vs currency at the given rate."""

    # Get the rates
    base_rate: float = get_currency(base,rates)
    vs_rate: float = get_currency(vs,rates)

    # Make the conversion and return it
    conversion: float = round((vs_rate / base_rate) * amount,2)
    print(f'{amount:,.2f} ({base}) is: {conversion:,.2f} ({vs})')
    return conversion

def main_currencyConverter():
    data: dict = get_rates(mock=True) #Mock true will get data from file and mock false will get data from api
    rates: dict = data.get('rates')

    convert_currency(100,'EUR','JPY', rates=rates)
    #convert_currency(100,'abc','JPY', rates=rates)
    #convert_currency(100,'JPY','SEK', rates=rates)

if __name__ == '__main__':
        main()

# Improvements
#   - Nice user prompt with currency, versus currency and an amount
#   - Add error catched to the above (like please enter a valid number)