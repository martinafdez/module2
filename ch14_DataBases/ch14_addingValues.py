# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:51:15 2019

@author: mluci
"""
####Chapter 14: Databases####
#Task 2: Adding data to table with variables#

import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('ch14.db')
c=conn.cursor()

#Inserting data dynamically#
def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H/:%M:%S'))
    keyword='Python'
    value=random.randrange(0,10)
    
    c.execute('INSERT INTO stuffToBuild(unix, datestamp, keyword, value) VALUES (?,?,?,?)', (unix, date, keyword, value))
    conn.commit()
    
#Insert multiple rows with a for loop#
for i in range(10):
    dynamic_data_entry()
    time.sleep(1)
    
c.close()
conn.close()



###Task 3: Reading data from databases###
conn = sqlite3.connect('ch14.db')
c=conn.cursor()

def read_from_db_all():
    c.execute('SELECT * FROM stuffToBuild WHERE value=8 ')
    for row in c.fetchall():
        print(row)
read_from_db_all()
print('read from db all')

#Task 3 extension#
def read_from_db2():
    c.execute('SELECT unix FROM stuffToBuild WHERE value < 8')
    for row in c.fetchall():
        print(row[0])
read_from_db2()  
print('read from db all 2')    

c.close()
conn.close()  
        
