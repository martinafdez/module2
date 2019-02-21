# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 16:13:28 2019

@author: mluci
"""


####Flask and using Python and HTML together####

from flask import Flask, render_template
import requests
import random
from config import *



app = Flask("MyApp")#creating Flask object and passing one MyApp parameter to it
@app.route("/")#creates route to standard index page. / means top of the server.
def hello():
    
    ####NAME API###
    endpoint_name= "https://www.behindthename.com/api/random.json"
    payload={"key": config.name_api_key , "number": "1"}  
    
    name_response = requests.get(endpoint_name, params=payload)
    
    created_name=name_response.json()
    
    name = created_name['names']
    namestr=str(name)
    final_name=namestr.strip("[]''")

    
    ####activity API####
    endpoint_activity="https://www.boredapi.com/api/activity"
    
    act_response=requests.get(endpoint_activity)
    
    created_act=act_response.json()
    
    activity=created_act["activity"]
    actstr=str(activity)
    final_act=actstr.strip("[]''")
    
    ####API Advice slip####
    advice_endpoint= "https://api.adviceslip.com/advice"
    
    ad_response=requests.get(advice_endpoint)
    
    created_ad=ad_response.json()
    
    advice_slip=created_ad["slip"]["advice"]

    ###Cocktail API###
    cocktail_endpoint="https://www.thecocktaildb.com/api/json/v1/1/random.php"
    
    cocktail_response=requests.get(cocktail_endpoint)
    
    created_cocktail=cocktail_response.json()

    
    cocktail=created_cocktail["drinks"][0]["strDrink"]

    
    ####Colour API####
    try:
        endpoint_colour="http://www.colr.org/json/color/random"
    
        colour_response=requests.get(endpoint_colour)
        print(colour_response)
    
        created_colour=colour_response.json()
        print(created_colour)
        colour=created_colour["colors"][0]["tags"][0]["name"]
        print(colour)
    except IndexError:
        #print("rainbow")
        colour="rainbow"
        
    
    ##Animal API####
    try:
        pet_endpoint="http://api.petfinder.com/pet.getRandom?&"
        payload={"key": config.pet_api_key, "format": "json", "output": "basic"}
        
        pet_response=requests.get(pet_endpoint, params=payload)
        
        created_pet=pet_response.json()
        
        pet_name=created_pet['petfinder']['pet']['name']['$t']

        pet_breed=created_pet['petfinder']['pet']['breeds']['breed']['$t']
        
        pet_type=created_pet['petfinder']['pet']['animal']['$t']
        
    except TypeError:
        pet_breed="pitbull"
        
    except NameError:
        pet_type="dog"
    
    ####weather & location API###
    ###randomise postcode selection###
    postcodes = {'EH11BQ', 'CF102BU', 'BT15BA', 'CB39BB'}
    name=random.sample(postcodes, 1)
    strname=str(name)
    final_postcode=strname.strip("[]''")
    
    ###link it to postcode API###
    weather_endpoint="https://api.postcodes.io/postcodes/"
    postcode = final_postcode
    
    postcode_response = requests.get(weather_endpoint + postcode)
    
    data_postcode = postcode_response.json()
    town_name=data_postcode["result"]['country']
    
    
    ###link it to weather API###
    endpoint_weather="http://api.openweathermap.org/data/2.5/weather"
    payload={"appid": config.weather_api_key,  "q": town_name}
    
    response=requests.get(endpoint_weather, params=payload)
    data=response.json()
    #print(data)
    
    weather=data['weather'][0]['description']
    
    
    
    ####Insert into template#####
#    template = ("Once upon a time in the land far far away of {} there was an elf​ called ​{} who​ lived with a {} coloured {} {} named {}​.One morning {}​ woke up and saw that outside it showed signs of {}. {} was very bored so decided to {}. {} and {} did this all day long before the sun went down and {} finally decided to settle down and order a Chinese takeaway washed down with a {} cocktail. For dessert {} noticed they had been given a fortune cookie so they opened the cookie to find a message inside that said read ' {}'. The next day {} woke up inspired instead of bored and lived happily ever after.".format(town_name, final_name, colour, pet_breed, pet_type, pet_name, final_name, weather, final_name,  final_act, final_name, pet_name,final_name, cocktail, final_name, advice_slip, final_name))
    
    #print(template)  
   # return "<h1>Refresh for your fairytale!</h1>" + template
    return render_template("index.html", title="Fairytale Generator", **locals())
    
    
   



app.run(debug=True)#calling object and calling run on it


