# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 13:46:26 2018

@author: mluci
"""

import sys
print(sys.argv)


#import sys
#
#if len(sys.argv) < 2:
#    print("what is your name")
#    sys.exit()
#    
#print("Hello, " + sys.argv[1])



from sys import argv

script, filename = argv

print ("We're going to erase {}.".format(filename))
print ("If you don't want that, hit CTRL- C (^C).")
print ("If you do want that, hit RETURN.")
raw_input("?")
print ("Opening the file...")
target = open(filename, 'w')
print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
print ("I'm going to write these to the file.")


target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("And finally, we close it.")
target.close()







