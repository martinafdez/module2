# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:10:47 2019

@author: mluci
"""

####Chapter 14: Databases####

#Task 1: Create table and insert data#
import sqlite3

#Import and connect a database#
conn = sqlite3.connect('ch14.db')

#Connect cursor#
c=conn.cursor()

#Create table#
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL, datestamp TEXT,  keyword TEXT, value REAL)')

#Inserting data into tables#

def data_entry():
    c.execute("INSERT INTO stuffToBuild VALUES(14223222, '2018-01-01', 'python', 5)")
    conn.commit()
    c.close()
    conn.close()
    
#Call the function to create table#
create_table()
data_entry()

import sqlite3
import time
import datetime
import random

#Inserting data dynamically#
def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.frmtimestamp(unix).strftime('%Y-%m-%d %H/:%M:%S'))
    keyword='Python'
    value=random.randrange(0,10)
    
    c.execute('INSERT INTO stuffToBuild(unix, datestamp, keyword, value) VALUES (?,?,?,?)', (unix, date, keyword, value))
    conn.commit()
    
#Insert multiple rows with a for loop#
    for i in range(10):
        dynamic_data_entry()
        time.sleep(1)
    
#c.close()
conn.close()
        



