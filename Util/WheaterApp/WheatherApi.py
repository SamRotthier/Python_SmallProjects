import os
from typing import Final
import requests
import json
from Model import Weather, dt

dummy_dataJson = os.path.join(os.path.dirname(__file__),'./dummy_data.json')
API_KEY: Final[str] = '00529a96f3800d047fe1f3cf36b326c1'
BASE_URL: Final[str] = 'https://api.openweathermap.org/data/2.5/forecast'

def get_weather(city_name: str, mock: bool = True) -> dict:
    if mock:
        with open(dummy_dataJson) as file:
            return json.load(file)
        
    #request live data
    payload: dict = {'q': city_name, 'appid' : API_KEY, 'units': 'metric'}
    request = requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()

    #with open(dummy_dataJson, 'w') as file:
    #     json.dump(data, file)

    return data


def get_weather_details(weather: dict) -> list[Weather]:
    days: list[dict] = weather.get('list')

    if not days:
        raise Exception(f'Problem with json: {weather}')
    
    list_of_weather: list[Weather] = []
    for day in days:
        w: Weather = Weather(date=dt.fromtimestamp(day.get('dt')),
                              details=(details := day.get('main')),
                              temp=details.get('temp'),
                              weather=(weather := day.get('weather')),
                              description=weather[0].get('description'))
        list_of_weather.append(w)
    
    return list_of_weather
         
    
#if __name__ == '__main__':
#        current_weather: dict = get_weather('tokyo', mock=True)
#        weather: list[Weather] = get_weather_details(current_weather)
#        #print(get_weather('tokyo', mock=True))
#        for w in weather:
#            print(w)