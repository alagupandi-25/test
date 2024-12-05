import requests
import urllib.parse

API_KEY = 'af9e65722413ec1cbc3f68cdbb04794c'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city_name):
    if not city_name.strip():
        int("City name cannot be empty!")
        return
    city_name_encoded = urllib.parse.quote(city_name)
    url = BASE_URL + "q=" + city_name_encoded + "&appid=" + API_KEY + "&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_desc = data['weather'][0]['description']
        print(f'City: {city_name}')
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")
        print(f"Weather Description: {weather_desc.capitalize()}")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print(f'City {city_name} not found, please check the city name.')

city = input("Enter city name: ").strip()
get_weather(city)