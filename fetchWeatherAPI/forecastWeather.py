import json
import sys
import requests

class WeatherForecast:
    def __init__(self):
        pass

    def set_location(self):
        if len(sys.argv) < 2:
            print("\nUsage: weatherForecast.py location")
            sys.exit()

        location = ' '.join(sys.argv[1:])
        print(location)
        return location

    def get_json(self, location, apiKey):
        url = f"https://api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt=3&appid={apiKey}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            sys.exit()

    def json_to_dict(self, json_obj, location):
        list_data = json_obj['list']
        print(f"Current weather in {location} is: {list_data}.")

def main():
    print("\nWelcome to Kartik's weather forecasts!")
    weather = WeatherForecast()
    apiKey = input("Enter the API Key: ")

    location = weather.set_location()
    json_obj = weather.get_json(location, apiKey)
    weather.json_to_dict(json_obj, location)

if __name__ == "__main__":
    main()
