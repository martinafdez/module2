# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:15:49 2018

@author: mluci
"""
phoneBook_dict={}
def phoneBook():
    QueensAge= 92
    counter = 1
    for i in range(4):
        pers_name=str(input("enter your name: "))
        pers_no=str(input("please enter last 3 digits of your phone number: "))
        pers_luckyNo=int(input("please enter your lucky number: "))
        pers_postC=str(input("please enter your post code: "))
        pers_city=str(input("please enter your town/city "))
        phoneBook_dict[pers_name]=pers_no, pers_luckyNo, pers_postC, pers_city
        UserAge=int(input("Now please enter your age: "))
        phonesList=list(phoneBook_dict.values())
        if UserAge == int :
            phoneBook_dict[pers_name]+=UserAge
        elif UserAge != int:
            print("Please enter a number")
        QueenAndYou=QueensAge-UserAge
        print("The age gap between you and the Queen is {}".format(QueenAndYou))
        counter += 1
        print(phoneBook_dict)
        #print(phoneBook_dict)
                
phoneBook()

def sortingPhoneBook(phoneBook):
    phonesList=list(phoneBook_dict.keys())
    print(sorted(phoneBook_dict)) # organise alphabetically
    print(sorted(phoneBook_dict.items(), key=lambda kv:kv[1][3])) #srt by town city
    print(sorted(phoneBook_dict.items(), key=lambda k:k[1][1])) #sort by lucky number   
sortingPhoneBook(phoneBook)





    