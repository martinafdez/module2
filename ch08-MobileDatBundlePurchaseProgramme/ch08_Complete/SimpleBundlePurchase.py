# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:04:54 2018

@author: 612383263
"""
#--------Module 2: Lesson 8---------
#----"Data Bundle Exercise"----


###Functions###
def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode) == True:
        transtype=TransactionType()
        if transtype == 1:
                return ('Your balance is {}'.format(balance))
             
        elif transtype == 2:
            return TelNumber(balance) 
    else: 
        return 'Wrong Password'


def passwordCheck(truePasscode):
    attempt = input('Please enter your password: ')
    if attempt == truePasscode:
        return True
    else:
        return False 
    
def checkBalance(balance):
    if balance > 0:
        return True
    else:
        return False
    
def TransactionType():
    transtype = int(input('Please select what you would like to do: \n 1: Request credit balance \n 2: Purchase Data Bundle: '))
    return transtype
    
def TelNumber(balance):
    maxtopup = 100
 #   balanceAvailable = checkBalance(balance)
    Numb1 = int(input('Please enter your phone number: '))
    Numb2 = int(input('Please confirm your phone number: '))
    if Numb1 == Numb2:
        amountbuy = int(input('How much data would you like to buy? Please select up to 100GB. '))
        if amountbuy > maxtopup:
            return('Sorry maximum is 100.')
        elif amountbuy > balance:
            return('Sorry, you do not have enough in your account for this purchase.')
        else:
            multipleFive(amountbuy)
    else:
        return('Sorry, your numbers do not match. Try again')

def multipleFive(amountbuy):
    if amountbuy %5==0:
        return('Success. Your account has been updated.')
    else:
        return('This amount is unavailable. Try again please.')




















#
#def DataBundlePurchase(truePasscode, balance):
#    if passwordCheck(truePasscode):
#        if checkBalance(balance):
#            transtype=checkBalance(balance)
#            return transtype
#        else:
#            return ('Your balance is not sufficient: {}'.format(balance))
#    else: 
#        return 'Wrong Password'
#
#
#def passwordCheck(truePasscode):
#    attempt = input('Please enter your password: ')
#    if attempt == truePasscode:
#        return True
#    else:
#        return False 
#    
#def checkBalance(balance):
#    transtype=int(input('Please select what you would like to do: \n 1: Request credit balance \n 2: Purchase Data Bundle: '))
#    if transtype == "1":
#        return ('Your balance is {}'.format(balance))
#    elif transtype == "2":
#        return ('This service is unavailable at the moment')
#    if balance > 0:
#        return True
#    else:
#        return False







#    
#    
#    