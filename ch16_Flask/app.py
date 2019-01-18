# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:27:55 2019

@author: mluci
"""

from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def hello():
    return render_template("page.html")

#@app.route("/<name>")
#def hello_someone(name):
#    return render_template("hello.html", name=name.title())
    

@app.route("/<name>") #variable in path
def hello_someone(name):
    return render_template("styledhello.html", name=name.title())
    
@app.route("/signup", methods=["POST"]) #getting information from the user
def sign_up():
    form_data = request.form
    print(form_data["email"])
    return "ALL OK"


@app.route("/age/<age>")
def hello_age(age):
    return render_template("age.html", age=age.title())

app.run(debug=True)





