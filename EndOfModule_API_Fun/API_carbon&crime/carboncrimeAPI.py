#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 14:42:49 2019

@author: martinafernandez
"""

import requests

######GET AIR POLLUTION API#####
##summer##
endpoint_carbon_summer = "https://api.carbonintensity.org.uk/regional/intensity/2018-06-01/2018-06-02/regionid/13"


carbon_response_sum = requests.get(endpoint_carbon_summer)
#print(carbon_response_sum)

data_carbon = carbon_response_sum.json()
print(data_carbon)

print(data_carbon["data"]["data"][0]["intensity"]["index"])

#england




###winter##
#endpoint_carbon_winter = "https://api.carbonintensity.org.uk/regional/intensity/2018-12-01/2018-12-14"
#
#
#carbon_response_wint = requests.get(endpoint_carbon_winter)
#print(carbon_response_wint)
#
#data_carbon_wint = carbon_response_wint.json()
##print(data_carbon_wint)


######GET POLICE CRIME API######
#endpoint_police = "https://data.police.uk/api/crimes-at-location?date=2017-02&location_id=884227"
#
#
#police_response = requests.get(endpoint_police)
#print(police_response)
#
#data_police = police_response .json()
#print(data_police)





#####CREATE SQL BASED ON THIS####



####DISPLAY ######



#
## To be able to read the data you need to look at what you actually get.
## Look at the type of brackets that surrounds each item in your json file.
## If it's {} it will work like a dictionary
## If it's [] it will work like a list
#print(data_weather['weather'][0]['description'])
#print(data_postcode['result']['longitude'])
