# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 10:35:07 2019

@author: mluci
"""

####Task 14: Homework###


import sqlite3

#Import and connect a database#
conn = sqlite3.connect('PhoneBook1.db')

#Connect cursor#
c=conn.cursor()

#Create table# 
def create_p_table():
    c.execute('CREATE TABLE IF NOT EXISTS PhoneBook1(First Name TEXT, Last Name TEXT, Address Line One VARCHAR(255), City TEXT, Postcode VARCHAR(255), Telephone Number VARCHAR(255), Business Category TEXT, X Coordinate REAL, Y Coordinate REAL)')

create_p_table()
conn.commit()
c.close()
conn.close()