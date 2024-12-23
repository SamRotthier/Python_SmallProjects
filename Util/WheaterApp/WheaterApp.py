#https://openweathermap.org/api

try:
    from .WheatherApi import get_weather, get_weather_details, Weather  # Relative import for package execution
except ImportError:
    from WheatherApi import get_weather, get_weather_details, Weather # Direct execution


def main_weatherApp():
    # Ask the user for their city
    user_city: str = input('Enter a city:')

    # Get the current weather details
    current_weather: dict = get_weather(user_city, mock=False)
    weather_details: list[Weather] = get_weather_details(current_weather)

    # Get the current days
    dfmt: str = '%d/%m/%y'
    days: list[str] = sorted(list({f'{date.date:{dfmt}}' for date in weather_details}))
    #print(days)

    for day in days:
        print(day)
        print('---')

        # Group the weather data by date to make it easier to read
        grouped: list[Weather] = [current for current in weather_details if f'{current.date:{dfmt}}' == day]
        for element in grouped:
            print(element)
        print('') # An Empty line

if __name__ == '__main__':
    main_weatherApp()

# Improvements:
#   - Catch the error when it does not find a city
#   - Get the users location via his IP and give him the weather via this way
#   - Make it more userfriendly (show the information in a cleaner way)
