# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 10:38:42 2019

@author: mluci
"""
import requests 

#####File to test individual API's and their JSON formats####
########################ANIMAL API######################
try:
    pet_endpoint="http://api.petfinder.com/pet.getRandom?&"
    payload={"key": "API_ID", "format": "json", "output": "basic"}
    
    pet_response=requests.get(pet_endpoint, params=payload)
    print(pet_response)
    
    created_pet=pet_response.json()
    print(created_pet)
    
    pet_name=created_pet['petfinder']['pet']['name']['$t']
    print(pet_name)
    pet_breed=created_pet['petfinder']['pet']['breeds']['breed']['$t']
    print(pet_breed)
    pet_type=created_pet['petfinder']['pet']['animal']['$t']
    print(pet_type)
except TypeError:
    pet_breed="pitbull"
    print(pet_breed)


##########################COLOUR API#####################
try:
    endpoint_colour="http://www.colr.org/json/color/random"

    colour_response=requests.get(endpoint_colour)
    print(colour_response)

    created_colour=colour_response.json()
    print(created_colour)
    colour=created_colour["colors"][0]["tags"][0]["name"]
    print(colour)
except IndexError:
    print("rainbow")

#if colour_response == 200:
#    created_colour=colour_response.json()
#    print(created_colour)
    
#    colour=created_colour["colors"][0]["tags"][1]["name"]
#    print(colour)
#elif colour_response == 400:
#    colour_response=requests.get(endpoint_colour)   
#    colour=created_colour["colors"][0]["tags"][1]["name"]
#    print(colour)


















####Testing sections of code if needed###
##gender#
#endpoint_name="https://api.genderize.io/?name=[input from gender]"

#activity#
#endpoint_activity="https://www.boredapi.com/api/activity"
#
#payload=activity={"activity"}

#randomise name choice in Python#
#first_names = {'Andrea', 'Anthony' 'Bob', 'Claire', 'Dan', 'Sarah', 'John', 'Jane'}
#name=random.sample(first_names, 1)
#strname=str(name)
#final_name=strname.strip("[]''")
#
#print(final_name)


#add randomly generated name as variable that can be added to API link#
#name_response = requests.get(endpoint_name + final_name)
#print(name_response)