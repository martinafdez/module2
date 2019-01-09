# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:33:29 2019

@author: mluci
"""

#-7-# Sorting and printing key value pairs #   
metals_info={'iron':[2.3, '£56,000', 3], 'aluminium': [30, '£10.90', 2], 'silver': [5.8, '£37.00', 2], 'tin':[1, '7.00', 700 ]}
metals=list(metals_info.keys()) 
#metals.sort(key=lambda m:metals_info[m], reverse=True)#sort  dictionary by values in reverse order
#keyValue=sorted(metals_info.items(), key=lambda kv:kv[1][1], reverse=True)

    
for metal in metals:
    if metals_info[metal][0]>8:
        print("{0:>8}={1:5.1f}".format(metal,metals_info[metal][0]))