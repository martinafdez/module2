# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:04:54 2018

@author: 612383263
"""

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
        return 'Password OK'
    else:
        return 'Wrong password'
    #return "Not yet created"

def passwordCheck(truePasscode):
    attempt = input('Please enter your password')
    if attempt == truePasscode:
        return True
    else:
        return False 