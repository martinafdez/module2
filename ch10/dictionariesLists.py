# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 14:02:45 2018

@author: mluci
"""
#example of storing numeric values associated with keys
metals_info={'iron':[2.3, '£56,000', 3], 'aluminium': [30, '£10.90', 2], 'silver': [5.8, '£37.00', 2], 'tin':[1, '7.00', 700 ]}
metals=list(metals_info.keys()) #cast to list so can do list operations on it

print(metals)
#sort dictionary's 2nd value in descending order
print(sorted(metals_info.items(), key=lambda kv:kv[1][1], reverse=True)[:2] )#get the top two only



##class example:
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