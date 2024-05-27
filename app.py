import flask;
import requests;
import os;

API_KEY = "czqy38iyh3P8Jhoni0E0XSisPetjTcEP"

LocationName = input("Where are you located?\n")




WeatherDataCall = requests.get('https://api.tomorrow.io/v4/weather/location=${LocationName}&apikey=czqy38iyh3P8Jhoni0E0XSisPetjTcEP')

WeatherDataBlob = WeatherDataCall.json()

WeatherTemperature = WeatherDataBlob['timelines']['minutely'][0]['values']['temperatureApparent']


print(WeatherDataBlob)