import requests
import urllib3
from bs4 import BeautifulSoup
import json
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url='https://web.archive.org/web/20180619015316/http://openweathermap.org/help/city_list.txt'
response = requests.get(url,verify=False)
soup = BeautifulSoup(response.content,'html.parser')
with open('open_weather.txt','w') as f:
    f.write(soup.text)
with open('open_weather.txt') as f:
    cities = f.readlines()
cities.pop(0)
weather_condition={}
for city in cities:
    weather_condition[city.strip().split('\t')[1]] =int(city.strip().split('\t')[0])
with open('open_weather.json','w') as f:
    f.write(json.dumps((weather_condition)))