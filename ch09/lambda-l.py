# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:48:17 2018

@author: mluci
"""

a = [50, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_favourite_fruits=['apple', 'orange', 'banana']
x = ['aa', 'zs', 'cs', 'hd', 'ab']
z = ['zs', 'yw', 'hd', 'cs', 'ab']
y = ['ab', 'cs', 'hd', 'yw', 'zs']

x2 = [('a', 3, z), ('c', 1, y), ('b', 5, x)]
#print(sorted(x2, key=lambda s:s[1]))
#print(sorted(x2, key=lambda s:s[2][1]))
print(sorted(x2, key=lambda s:s[2][-3]))