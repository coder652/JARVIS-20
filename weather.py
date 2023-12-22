import pyttsx3
import requests
from pyttsx3 import speak
import json
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
speak('enter your location sir ')
city = input('Enter your Location sir <<.>> ')
speak('Detail Regarding Location ')
print('Detail Regarding  Location')
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=4c82acb8e80be6c1e9c49b78f86072cb&units=metric'.format(city)
res = requests.get(url)
data = res.json()
temp = data['main']['temp']
wind_speed = data['wind']['speed']
longitude = data['coord']['lon']
latitude = data['coord']['lat']
humidity = data['main']['temp']
pressure = data['main']['pressure']
country = data['sys']['country']
sunrise = data['sys']['sunrise']
sunset = data['sys']['sunset']
time = data['timezone']
visibility = data['visibility']


print('Temperature <<.>> {} degree celcius'.format(temp))
speak('Temperature : {} degree celcius'.format(temp))
print('Wind Speed <<.>> {} meter per second'.format(wind_speed))
speak('Wind Speed : {} meter per second'.format(wind_speed))
print('Humidity <<.>> {}'.format(humidity))
speak('Humidity : {}'.format(humidity))
print('Latitude <<.>> {}'.format(latitude))
speak('Latitude : {}'.format(latitude))
print('Longitude <<.>> {}'.format(longitude))
speak('Longitude : {}'.format(longitude))
print('Country <<.>> {}'.format(country))
speak('country : {}'.format(country))
print('Pressure <<.>> {}'.format(pressure))
speak('pressure : {}'.format(pressure))
print('sunrise <<.>> {}'.format(sunrise))
speak('sunrise : {}'.format(sunrise))
print('sunset <<.>> {}'.format(sunset))
speak('sunset : {}'.format(sunset))
print('visibility <<.>> {}'.format(visibility))
speak('visibility : {}'.format(visibility))
print('Conclusion')
speak('End of the report')
