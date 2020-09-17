import pyttsx3
import requests
from pprint import pprint
from pyttsx3 import speak
import json
speak('enter your city sir')
city = input('Enter your city sir : ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=your api here &units=metric'.format(city)

res = requests.get(url)

data = res.json()

temp = data['main']['temp']
wind_speed = data['wind']['speed']

latitude = data['coord']['lat']
longitude = data['coord']['lon']

description = data['weather'][0]['description']

speak('Temperature : {} degree celcius'.format(temp))
print('Temperature : {} degree celcius'.format(temp))
speak('Longitude : {}'.format(longitude))
print('Longitude : {}'.format(longitude))
print('Wind Speed : {} meter per second'.format(wind_speed))
speak('Wind Speed : {} meter per second'.format(wind_speed))
print('Latitude : {}'.format(latitude))
speak('Latitude : {}'.format(latitude))
speak('Description : {}'.format(description))
print('Description : {}'.format(description))
