# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:10:47 2019

@author: mluci
"""

####Chapter 14: Databases####
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
