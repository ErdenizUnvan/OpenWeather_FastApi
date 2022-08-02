from fastapi import FastAPI, Path
import requests
import urllib3
import time
import json

weather_condition=json.load(open('open_weather.json'))

app=FastAPI()

@app.get("/get_weather_condition/{city_name}")
def get_weather_condition(city_name: str = Path(None, description="The name of the city you want to learn weather condition")):
	if city_name in weather_condition:
		ID = weather_condition[city_name]
		url ='https://api.openweathermap.org/data/2.5/weather'
		apikey='97afb3c84a9f644b9bd5b9586ea5497a'
		query_params = {'id':ID,'appid':apikey,'units':'metric'}
		response= requests.get(url,params=query_params,verify=False)
		res = response.json()['main']['temp']
		message=(f'The temperature for the city of {city_name} is {res} degrees in Celcius at {time.ctime()}.')
		return message
	else:
		return {"Data":"Not Found"}