#pip install keyboard ## first install keyboard library
#be careful with spaces before writing the city name!
import requests
import urllib3
import sys
import keyboard
import json
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
open_weather = json.load(open('open_weather.json'))
print("Press Space to Continue program or Esc to exit: ")
while True:
    if keyboard.is_pressed('Esc'):
        print("\nyou pressed Esc, so exiting...")
        #sys.exit(0)
        break
    elif keyboard.is_pressed('SPACE'):
        try:
            city = input('Type name of the city:')
            ID = open_weather[city]
            url='https://api.openweathermap.org/data/2.5/weather'
            apikey='97afb3c84a9f644b9bd5b9586ea5497a'
            query_params ={'id':ID,'appid':apikey,'units':'metric'}
            response = requests.get(url,params=query_params,verify=False)   
    
        except Exception as e:
            print(f'You have selected a wrong city name: {e}')
            print("Press Space to Continue program or Esc to exit: ")
            if keyboard.is_pressed('Esc'):
                print("\nyou pressed Esc, so exiting...")
                #sys.exit(0)
                break
            elif keyboard.is_pressed('SPACE'):
                continue

        else:
            res= response.json()['main']['temp']
            print(f"""
            The name of the city : {city}
            The temperature: {res} Celcius degrees
            At local time of: {time.ctime()}.
            """)
            break