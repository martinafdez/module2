# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:20:02 2018

@author: mluci
"""

#--------Module 2: Lesson 12---------#
#--------"Introducing For Loops"---------#


###Task 1: Loop through a list###
my_shopping_cart=["cake", "plates", "plastic forks", "juice", "cups"]
for item in my_shopping_cart:
    print(item)


###Task 2: Update List Values###
#-Version 1-#    
values=[875, 23, 45]
for val in values:
    print("--->"+str(val))     
#-Version 2-#
values=[875, 23, 45]
for val in values:
    print("--->"+str(val+50)) 
  
    


###Task 3: Create your own list and print###
values=["this", 55, "that"]
for item in values:
    print("***", item)
    
    
###Task 4: Loop through string data type###
for char in "Yes":
    print(char)
    
for char in "I like coding".split():
    print(char) #convert into a list
    
    
###Task 5: Loop through tuple###
values=(100, 101, 99, "little string")
for i in values:
    print(i)


###Task 6&7: Loop through dictionary###
#-6-#
salaries={"al":20000, "bo":50000, "ced":1500}   
salary=list(salaries.keys())
sorted(salaries.items(), key=lambda s:s[1])
for s in salaries:
    print("{} = {}".format(s,salaries[s]))
 
#-7-# Sorting and printing key value pairs #   
metals_info={'iron':[2.3, '£56,000', 3], 'aluminium': [30, '£10.90', 2], 'silver': [5.8, '£37.00', 2], 'tin':[1, '7.00', 700 ]}
metals=list(metals_info.keys()) 
metals.sort(key=lambda m:metals_info[m], reverse=True)#sort  dictionary by values in reverse order
keyValue=sorted(metals_info.items(), key=lambda kv:kv[1][1], reverse=True)
for metal, metalValue in keyValue:
    print(metal, metalValue[1]) #print second value
    
for metal in metals:
    print(metal, metals_info[metal][1]) #other way to do the same task
    
for k, v in sorted(metals_info.items(), key=lambda kv:kv[1][1]):
    print(k, v[1]) #othe way to do the same task 
    
for metal in metals:
    if metals_info[metal][0]>8:
        print("{0:>8}={1:5.1f}".format(metal,metals_info[metal][0]))


    
    
###Task 8: Combining counting loops and conditionals to filter out values###
testlist=[1,2,3,4,5]
for i in testlist:       
    if i > 4:
        print(i)
    else:
        print(i, "not in if conition")
        
for metal in metals:
    if metals_info[metal][0]>8:
        print(metal,metals_info[metal][0])
        
##Task 9: Design a sum function##
values=[3,12,9]
total=0
for val in values:
    total+=val #same as total = total + val
print("TOTAL: " + str(total))

#-Function Version-#
values=[3,12,9]
def SumValues(values):    
    total=0
    for val in values:
        total+=val 
        return total
    print(SumValues(values))
SumValues(values)
    
        
#-Classroom task: Xmas game-#
#presents={"candles": (2, "3.00"), "books": (70, "1.00"), "clothes": (3, "90.00")}
presents={"candles": 2, "books": 70, "clothes": 3}
counter=1
for pres, item in presents.items():
    print("open gift", counter, "the gift is", pres)
    if item < 4:
        print("i have received", item, "of", pres)
    else:
        print("i want more of", pres)
    counter+=1
    
    
###Task 10:  Loop with index values###
values=[3,12,9]
for i in range(len(values)): #for index in the range of values length whatever the length is
    values[i]=values[i]*2 #multiply the item by 2 and update the index of values
print(values) #print the new updated values


    
###Task 11: Loop with range function###

for i in range(3,10,2): #will go through range 3-10 skipping 2
    print(i)

values=[3,12,9,5,6]
for index in range(1, len(values),2):
    print(values[index], "with index", index) #len of values is 5 so range is 1-5, skipping 2. 
    #prints index 1, skips 2, then prints index 3 
    ##
    
###Task 12: Using break ###
scan_list=[2, 5, 30, 300, 202, 22]
for scan in scan_list:
    if scan < 100:
        print("ok")
        break

nums=[2, 5, 30, 300, 202, 22]
for index in range(len(nums)):
    if nums[index] > 100:
        print("break: ", nums[index], "with index", index)
        break
    
###Task 13: Creating nested loops in a for loop###
outer_vals=[1,2,3]
inner_vals=['A','B','C']
for val_o in outer_vals:
    for val_i in inner_vals:
        print(val_o, val_i)        

#-Version 2: dictionary-#    
outer_val_list=[1,2,3]
inner_vals_list=['A','B','C']
dict={}
for outer_val in outer_val_list:
    for inner_val in inner_vals_list:
        print(outer_val, inner_val)
        dict[outer_val]=inner_val
print(dict)    


#-Version 3: updating a dictionary-#
outer_val_list=[1,2,3]
inner_vals_list=['A','B','C']
dict={}
for outer_val in [1,2,3]:
    for inner_val in ['A','B','C']:
        dict[outer_val]=inner_val
        print(dict) 
    
###Task 14: Multiplication###
for i in range(1,11):
    for j in range(1,11):
        print("{0:>3}".format(i*j), end="")
    print("\n")