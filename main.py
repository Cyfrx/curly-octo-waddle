import os
from time import sleep

from papirus import PapirusComposite


# import required modules
import requests
import json

# Enter your API key here
api_key = "8070d64866baebc8dcd33a6b08074a7f"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = "Monterey Park"

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module
# return response object
# response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
# x = response.json()

DIRECTORY = os.path.dirname(os.path.realpath(__file__))

# 200x96 resolution

# example for accessing files in same directory as main.py
# self.display.AddImg(os.path.join(DIRECTORY, 'maplearu.jpg'), 168, 20, (32, 32), Id="ForecaaastIconOne")

class PiDisplay:

    def update(self):
        # API interaction
        response = requests.get(complete_url)
        x = response.json()
        y = x["main"]
        w = x["weather"]
        desc = w[0]['description']
        temp_min = y['temp_min']
        temp_max = y['temp_max']
        current_temperature = y["temp"]
        americanunits = (9/5) * (current_temperature - 273.15) + 32
        current_temperature = americanunits
        #end of API interaction



        self.display = PapirusComposite(False)
        condition_icon = w[0]['icon']
        self.display.AddImg(os.path.join(DIRECTORY, 'weather_condition_icons', condition_icon + '@2x.png'), -5, -5, (40, 40))
        self.display.AddText(str(round(current_temperature)) + ' ℉', 25, 0, size=12)
        self.display.AddText(str(round(temp_min)) + '/' + str(round(temp_min)) + ' ℉', 25, 14, size=12)

        self.display.AddText(str(desc), 20, 40, size=12, Id="lin2ne")
        # self.display.AddText(z, 20, 190, size = 16, Id = "test")
        # self.display.AddImg(os.path.join(DIRECTORY, self.unknown_icon),0,0, (100,100), Id = "testimg")
        self.display.AddImg(os.path.join(DIRECTORY, 'placeholder.jpg'), 168, 64, (32, 32))
        self.display.AddImg(os.path.join(DIRECTORY, 'maplearu.jpg'), 168, 20, (32, 32))
        # self.display.AddImg(os.path.join(), 1, 63, (32, 32), Id="ForecastIconOne")
        self.display.WriteAll()







PI = PiDisplay()


PI.update()
while True:
    sleep(60*20)
    PI.update()