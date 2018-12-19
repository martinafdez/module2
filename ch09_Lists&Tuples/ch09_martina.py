# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:29:29 2018

@author: mluci
"""
#--------Module 2: Lesson 9---------
#----"Lists and Tuples"----

###Task 1: Create a list###
my_favourite_fruits=['apple', 'orange', 'banana']
x = ['this', 55, 'that', my_favourite_fruits] #lists contain mix of data

###Task 2: Modify list###
#-Removing and Appending-#
print(x.remove(my_favourite_fruits))
x[1]='and'
x.append('again') #adds item to list as a sring
 
my_favourite_fruits=['apple', 'orange', 'banana',]
x = ['this', 55, 'that', 'that', 55, my_favourite_fruits] #lists contain mix of data

y = []
x.remove('this')
y = x.append('this') # y will still return a none type



#-Operating on list?-#
x = ['the', 'cat', 'sat']
y=['on' 'the', 'mat']
#z = x + y
#z = x - y
#z = x / y
#z = x * y

#-Set function on list-#
#print(set(x+y))
print(set(y+x))
#set function unordered items in a list, and removes duplicates.
a = set(x+y )



###Task 3: Slicing a list###
x = ['this', 'and', 'that', 'again']
print(x[1:4]) #includes item one but not 4
print(x[0:9]) #even if index number is out of range, will return up until the end.
print(x[0:0]) #0 is beginning and then up to but not including item 0 so returnes empty list because of sequential order 
print(x[-1:-1]) #as above
print(x[:])


###Task 4: Sorting a list###
x = [7,11,3,5,2]
print(sorted(x))

print(sorted(x, reverse=True))

x.sort()
x.sort(reverse=True)

x = ['aaa', 'zzz', 'fff',] #0] sorted and sort won't work on instances of integer and string
x.sort()
print(sorted(x))

###Task 5: Create tuple and compare tuple with list###
#-Cannot delete item inside a tuple=#
a =[1,2,3,4,5]
del a[-1]
a

b=(0,1,2,3,4,5,6,7,8,9)
del b[-1]

#-Cannot assign new value to a position in tuple-#
##list
a=[0,1,2,3,4,5,6,7,8,9]
a[0]=50
a
##tuple
b=(4,6,3,3,5,)
b[0]=50

#-Cannot append to tuple-#
##list
a=[4,6,3,3,5,]
a.append('z')

##tuple
b=(4,6,3,3,5,)
b.append('z')

#c=list(b)#this works, and makes tuple become a list. b as a tuple sill exists.


###Task 6: Using Lamda to sort a list###
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







##Extra independent task: testing what item in a list is sorted first. Answer is the first item, not integer vs string###

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


