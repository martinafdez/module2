# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:35:10 2019

@author: mluci
"""

####Chapter 15: API, Weather app#####

import requests

endpoint="http://api.openweathermap.org/data/2.5/weather" #where exactly our database we want is located
payload={"q": "Quito, Ecuador", "units":"metric", "appid":"API_CODE"}#information passing to API to get our data

response=requests.get(endpoint, params=payload)
data=response.json()


print(data)
print("this is data \n")

print(response.url)
print(response.status_code)
print(response.headers["content-type"])

