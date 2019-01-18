# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:17:22 2019

@author: mluci
"""

####Chapter 16: Flask and using Python and HTML together####

from flask import Flask, render_template



app = Flask("MyApp")#creating Flask object and passing one MyApp parameter to it
@app.route("/")#creates route to standard index page. / means top of the server.
def hello():
    return "<h1>HTML</h1> \n <h2>New line?</h2>"

@app.route("/center")
def middle():
    return "<p style='text-align: center;'> This text will be centered.So will this paragraph.</p>"

@app.route("/bio")
def paragraph():
    return "<p> This is a test paragraph.</p>"

app.run(debug=True)#calling object and calling run on it


