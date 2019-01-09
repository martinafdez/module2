# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 11:35:14 2019

@author: mluci
"""

####Coding Bat####
#Return number of even ints in given array#
#count_evens=([2,1,2,3,4])
#count_evens=([2,2,0])
#count_evens=([1,3,5])
#
#def count_evens(nums):
#    counter=0
#    for num in nums: 
#        if num % 2 == 0:
#            counter += 1
#    return counter

#Return True if array contains a 2 next to a 2 somewhere#

def has22(nums):
 for num in nums:
   if nums[1:] == 2:
     return True
   if nums[:-1] == 2:
     return True
   else:
     return False
 
has22([1,2,2])



    