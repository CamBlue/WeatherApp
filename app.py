import flask;
import requests;
import os
from geopy.geocoders import Nominatim

#API_KEY = "czqy38iyh3P8Jhoni0E0XSisPetjTcEP"

loc = Nominatim(user_agent="GetLoc")


LocationName = input("Where are you located?\n")

getLoc = loc.geocode("LocationName")
print(getLoc)
'''
WeatherDataCall = requests.get('https://api.tomorrow.io/v4/weather/location=${LocationName}&apikey=czqy38iyh3P8Jhoni0E0XSisPetjTcEP')

WeatherDataBlob = WeatherDataCall.json()

WeatherTemperature = WeatherDataBlob['timelines']['minutely'][0]['values']['temperatureApparent']


print(WeatherDataBlob)
'''