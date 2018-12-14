# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:55:28 2018

@author: 612383263
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:04:54 2018

@author: 612383263
"""
def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
        transtype=TransactionType()
        if transtype == 1:
            if checkBalance(balance):
                return ('Your balance is {}'.format(balance))
                exit()
            else:
                return ('Your balance is not sufficient: {}'.format(balance))
                exit()
        elif transtype == 2:
            return ('This service is unavailable at the moment')
            exit()
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
    balanceAvailable = checkBalance(balance)
    Numb1 = int(input('Please enter your phone number: '))
    Numb2 = int(input('Please confirm your phone number: '))
    if Numb1 == Numb2:
        amountbuy = int(input('How much data would you like to buy? Please select up to 100GB. '))
        if amountbuy > maxtopup:
            print('Sorry maximum is 100.')
        elif amountbuy > balanceAvailable:
            print('Sorry, you do not have enough in your account for this purchase.')
        else:
            multipleFive(amountbuy)
    else:
        print('Sorry, your numbers do not match. Try again')

def multipleFive(amountbuy):
    if amountbuy %5==0:
        print('Success. Your account has been updated.')
    else:
        print('This amount is unavailable. Try again please.')
     
        


    
        
        
        
 
    
    
    
    