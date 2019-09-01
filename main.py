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




class PiDisplay:

    def update(self):
        # API interaction
        response = requests.get(complete_url)
        x = response.json()
        y = x["main"]
        weath = x["weather"]
        z = weath[2]
        current_temperature = y["temp"]
        americanunits = (9/5) * (current_temperature - 273.15) + 32
        current_temperature = americanunits
        #end of API interaction

        self.display = PapirusComposite(False)
        self.display.AddText('Degrees: ' + str(current_temperature), 0, 0, size=12, Id="lineOne")
        self.display.AddText("HORTLER", 100, 80, size=12, Id="lineOne")
        self.display.AddText(z, 20, 190, size = 16, Id = "test")
        # self.display.AddImg(os.path.join(DIRECTORY, 'test', 'images', self.placeholder),0,0, (100,100), Id = "prototype")
        # self.display.AddImg(os.path.join(), 1, 63, (32, 32), Id="ForecastIconOne")
        self.display.WriteAll()




PI = PiDisplay()


PI.update()
while True:
    sleep(10)
    PI.update()