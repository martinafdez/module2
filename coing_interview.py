# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:53:38 2019

@author: mluci
"""

####Coding interview practice####

##Write letters A-Z in upper case to console placing each letter on a new line#
#version 1#
#alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#for letter in alphabet:
#    print(letter, )
    
#import string
#string.ascii_uppercase
#alphabet=list(string.ascii_uppercase)
#for letter in alphabet:
#    print(letter, )

##For every 3rd letter write it to onsole lowercase##
#import string
#alphabetstring=string.ascii_uppercase
#alphabet=list(string.ascii_uppercase)
#
#alphabet[2: :3] = [x.lower() for x in alphabet[2: :3]]
# 
#alphabetstring=' '.join(alphabet)
#for i in alphabetstring:
#    print (i)




##For every 4th letter, write its numeric position## 
import string
alphabetstring=string.ascii_uppercase
alphabet=list(string.ascii_uppercase)
i = (alphabetstring[3: :4])
alphabetstring.replace(i, i.lower())
print(alphabetstring)


for index, l in enumerate(alphabet):
    print(index, l)
    if index == alphabet[3: :4]:
        l.replace(l, l.lower)
    
    

 


#for i in range(len(alphabetstring)):
#    
#    for selectedLetter in alphabetstring[0,26,4]:
#        print(alphabetstring[i], selectedLetter)
#        if alphabetstring[i] == selectedLetter:
#        
#            alphabetstring.replace(alphabetstring[i], alphabetstring[i].lower())
##        
#alphabetstring=' '.join(alphabet)
#print(alphabetstring)


        

#for i in (i for i,x in enumerate(alphabetstring) if x == alphabetstring[3: :4]):
#    alphabet[3: :4] = [x.replace(x, i) for x in alphabet[3: :4]]
#    
#alphabetstring=' '.join(alphabet)
#print(alphabetstring)

#for position, item in enumerate(alphabetstring):
#    if item ==alphabet[3: :4]:
#        alphabet.replace(item, position)
#alphabetstring=' '.join(alphabet)
#print(alphabetstring)
        
#[x for x in range(len(alphabetstring)) if alphabetstring[3: :4]]
 


