# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 11:21:43 2019

@author: mluci
"""
import requests 


####Chapter 15- API's####
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/DOMAIN_NAME/messages",
        auth=("api", "API_KEY"),
        data={"from": "Excited User <FROM_EMAIL>",
              "to": ["TO_EMAIL"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})
    
send_simple_message()