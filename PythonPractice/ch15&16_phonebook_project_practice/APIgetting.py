# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 14:51:19 2019

@author: mluci
"""

import requests

# The base url to access the API information

endpoint_postcode = "https://api.postcodes.io/postcodes/"

# The parameters to what exactly you need from the API
# The structure of this varies from API to API
payload = {"q": "Zermatt, CH", "units": "metric", "appid": "api-key-goes-here"}

# Sometimes you don't need a parameter, just a value
postcode = "postcode"

# Before requesting anything from an API test the url by going to it in a browser

test_postcode_url = (endpoint_postcode + postcode)
print(test_postcode_url)

# If you get a decent response in a browser, you can go ahead and request it with Python)
postcode_response = requests.get(endpoint_postcode + postcode)

# Convert your return into json

data_postcode = postcode_response.json()

# To be able to read the data you need to look at what you actually get.
# Look at the type of brackets that surrounds each item in your json file.
# If it's {} it will work like a dictionary
# If it's [] it will work like a list
print(data_weather['weather'][0]['description'])
print(data_postcode['result']['longitude'])







# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 10:06:31 2019

@author: mluci
"""

import sqlite3 
import json
import random
import requests


conn = sqlite3.connect('phonebook.db') 

c = conn.cursor()

###Get API###
endpoint="https://api.postcodes.io/postcodes/"
#postcode = "LE111LG"


#test_postcode_url = (endpoint + postcode)
#print(test_postcode_url)

#postcode_response = requests.get(endpoint + postcode)


#print(data_postcode['result']['longitude'])
#print(data_postcode['result']['latitude'])



def RemoveSpaces(): 
    c.execute('SELECT postcode FROM people')
#    with open('data_people.json') as p:
#        dataPeople = json.load(p)
#        for row in dataPeople:
    for row in c.fetchall():
        print(row)
#            postcode=row["postcode"]
#            postcode = postcode.replace(' ', '')
#            print(postcode)
#            postcode_response = requests.get(endpoint + postcode)
#            data_postcode = postcode_response.json()
#            if data_postcode['status'] == 200:
#                print(data_postcode['result']['longitude'])
#                print(data_postcode['result']['latitude'])


#            for pc in postcode:
#                
                
RemoveSpaces()


        