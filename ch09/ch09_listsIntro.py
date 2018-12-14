# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:29:29 2018

@author: mluci
"""
#introducing compound type list and practicing functions on them


#my_favourite_fruits=['apple', 'orange', 'banana']
#x = ['this', 55, 'that', my_favourite_fruits] #lists contain mix of data
#print(x.remove(my_favourite_fruits))
#x[1]='and'
#x.append('again') #adds item to list as a sring
 
#my_favourite_fruits=['apple', 'orange', 'banana',]
#x = ['this', 55, 'that', 'that', 55, my_favourite_fruits] #lists contain mix of data
#
#y = []
#x.remove('this')
#y = x.append('this') # y will still return a none type

#x = ['the', 'cat', 'sat']
#y=['on' 'the', 'mat']
##z = x + y
##z = x - y
##z = x / y
##z = x * y
##
##print(set(x+y))
#print(set(y+x))
##set function unordered items in a list, and removes duplicates.
#a = set(x+y )


#x = ['this', 'and', 'that', 'again']
#print(x[1:4]) #includes item one but not 4
#print(x[0:9]) #even if index number is out of range, will return up until the end.
#print(x[0:0]) #0 is beginning and then up to but not including item 0 so returnes empty list because of sequential order 
#print(x[-1:-1]) #as above
#print(x[:])



#x = [7,11,3,5,2]
#
#print(sorted(x))
#
#print(sorted(x, reverse=True))
#
#
#x.sort()
#x.sort(reverse=True)
#
#
#x = ['aaa', 'zzz', 'fff',] #0] sorted and sort won't work on instances of integer and string
#
#x.sort()
#print(sorted(x))

#a =[1,2,3,4,5]
#del a[-1]
#a[0]=50
#
#
#
#b=(4,6,3,3,5,)
#b[0]=50

#a=[4,6,3,3,5,]
#a.append('z')
#b=(4,6,3,3,5,)
#b.append('z')
#c=list(b)#this works, and makes tuple become a list. b as a tuple sill exists.













#testing what item in a list is sorted first. Am=nswer is the first item, not integer vs string

ages =[('Person A', 16), ('Person Z', 40), ('Person B', 1)]
##person_id = [(1, 'Person B'), (34, 'Person A'), (20, 'Person Z')]
##ages.sort()
##print(ages)
#print(sorted(ages))
#person_id.sort()
#print(person_id)

#A = ages
#B = person_id

#person_id2=[('Person A', 23), ('Person Z', 50), ('Person B', 1)]
#
#A = sorted(ages)
#B = sorted(person_id2)
#
#if A == B:
#    print('same')
#else:
#    print("Different!") #tesing if string and integers will be considered by this or if only string since that is the first item and the one that undergoes the sorted function.


