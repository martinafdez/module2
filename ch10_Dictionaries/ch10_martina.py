# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:59:33 2018

@author: mluci
"""
#--------Module 2: Lesson 10---------
#----"Dictionaries"----




###Task 1&2: Dictionary that you can assign, retrieve and update values###
salary={} #initialises empty dictionary
print(salary)

salary['al']=20000 # adding a value and key into the empty dictionary named salary
print(salary)

salary['bb', 'cc']=200, 300 #adds values and keys two tuples
print(salary)

#print(salary['bo']) #will get key error if key doesn't exist

print(salary['al']) #access value via key

salary['al'] += 2000 #operation of the value in key 
print(salary)




###Task 3: Looking up and deleting values###
phone_pers={'sarika': '156', 'maggie': '421', 'martina': '380'}
phone_pers['maggie'] = '0421'
phone_pers['martina'] = '5380'
phone_pers['sarika'] += '2156'#adds string to exising one at the end
print(phone_pers)




###Task 4: Retrieving keys and values from a dictionary###
del phone_pers['martina'] #way to delete an item(which is key and value)
print(phone_pers)

phone_pers.keys() #keys() method only applicable to dictionary object - nonstandard list
phone_pers.values() # returns the values of the dicionary. returns non standardised list





###Task 5: Convert keys and values to list data type###
counts={'a':3, 'c':1, 'b':5} #ditionary
labels=list(counts.keys()) #casting dictionary keys into a list and assigning it to the variable 'labels'
labels.sort(key=lambda k:counts[k]) #now that labels holds the dictionary as a list, can do a list operation like sort in it. argument of sort is lambda which returns the original key and value pair but sorted by the key
#print(sorted(counts.items(), key=lambda kv:kv[1]))




###Task 6: How to avoid key error types###

k = 'sarika'
if k in phone_pers:
    print(k, ':', phone_pers[k])
else:
    print(k, 'not found!')
    
    
    
    

###Task 7 & 8: Sorting a dictionary
    #-Version 1-#
counts={'a':3, 'c':1, 'b':5} #ditionary
labels=list(counts.keys()) #casting dictionary keys into a list and assigning it to the variable 'labels'
labels.sort(key=lambda k:counts[k]) #now that labels holds the dictionary as a list, can do a list operation like sort in it. argument of sort is lambda which returns the original key and value pair but sorted by the key
print(sorted(counts.items(), key=lambda kv:kv[1]))    




#-Version 2-#
numbs={'pers1': [5, 67], 'Pers2': [90, 43], 'pers3': [2, 100]} #can store multiple values for a key in a list, tuple or even another dictionary depending on what you need it for
labels=list(numbs.keys())
labels2=list(numbs.values())
labels.sort(key=lambda k:numbs[k])
print(sorted(numbs.items(), key=lambda kv:kv[0]))#getting into the values and choosing the second item
print(sorted(numbs.items(), key=lambda k:k[0])) #sorts by string pers key
print(sorted(numbs.items(), key=lambda kv:kv[1])) #sorts by the value
print(sorted(numbs, key=lambda k:numbs[k]))# as above, without.items() will return only the key not keyvalue pair. this is a naming convention
print(sorted(numbs.items(), key=lambda k:k[1][1])) #as below
print(sorted(numbs.items(), key=lambda kv:kv[1][1])) #will access and sort by second value in value list
print(sorted(numbs.items(), key=lambda kv:kv[2])) # error as no third item







###Putting all together (list conversion then sorting)###
#example of storing numeric values associated with keys
metals_info={'iron':[2.3, '£56,000', 3], 'aluminium': [30, '£10.90', 2], 'silver': [5.8, '£37.00', 2], 'tin':[1, '7.00', 700 ]}
metals=list(metals_info.keys()) #cast to list so can do list operations on it

print(metals)
#sort dictionary's 2nd value in descending order
print(sorted(metals_info.items(), key=lambda kv:kv[1][1], reverse=True)[:2] )#get the top two only



##In class example##
#abc = {
#       1: ("greg","january",7 ),
#       2: ("anna", "october",3),
#       3: ("mag", "november", 13)
#       }
##sort by key:
#sorted(abc.items(), key=lambda kv: kv[0]) #return k, v pair
#sorted(abc) #return only k
#
##sort by values:
#sorted(abc.items(), key=lambda kv: kv[1]) #return k, v pair 
#sorted(abc, key=lambda k: abc[k]) #return only k
#
##sort by (2nd position of the) values:
#sorted(abc.items(), key=lambda kv: kv[1][2]) #return k, v pair 
#sorted(abc, key=lambda k: abc[k][2]) #return only k







#####
#Independent research into value retrieval#
#Tuple
#
#The simplest option is a two-tuple of strings, which you can access by index:
#
#>>> d1 = {'key': ('owner', 'type')}
#>>> d1['key'][0]
#'owner'
#>>> d1['key'][1]
#'type'
#Dictionary
#
#Next up is a sub-dictionary, which allows you to access the values by key name:
#
#>>> d2 = {'key': {'owner': 'owner', 'type': 'type'}}
#>>> d2['key']['owner']
#'owner'
#>>> d2['key']['type']
#'type'
#Named tuple
#
#Finally the collections module provides namedtuple, which requires a little setup but then allows you to access the values by attribute name:
#
#>>> from collections import namedtuple
#>>> MyTuple = namedtuple('MyTuple', ('owner', 'type'))
#>>> d3 = {'key': MyTuple('owner', 'type')}
#>>> d3['key'].owner
#'owner'
#>>> d3['key'].type
#'type'
#####








    