# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 11:40:02 2018

@author: mluci
"""


#--------Module 2: Lesson 2---------
#--"Operations, Strings and Variables----
###Homework###
a = 1
a=a+1
print(a)
b="hello"
print(b)
c=b.title()
print(b)
print(c)    
d="hello"
e=d.title()
print(d)
print(e)
name="Dave"
f="Hello{0}!".format(name)
print(f)
name="Sarah"
print(f)
print(f*5)


###Homework 2###
###LPTHW Exercises 1-10###

#1#
print ("hello world!")
print("hello again")
print("i like typing like this")
print("this is fun")


#2#
print ("i could have code like this") #and the comment after is ignored

#3#
print("I will not count my chickens")
print("hens", 25+30/6)
print("roosters", 100-25*3%4)

#4#
cars=100
space_in_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_car


print("there are", cars, "cars available")
print("there are only", drivers, "drivers available")
print("there will be", cars_not_driven, "empty cars today.")
print("we can transport", carpool_capacity, "people today.")
print("we have", passengers, "to carpool today")

#5#
my_name="zed shaw"
my_age=35
my_height=74 #inches
my_weight=180 #lbs
my_eyes='Blue'
my_teeth='white'
my_hair='brown'


print("lets talk about %s." %my_name)
print("he's %d inches tall." % my_height)
print("he's %d pounds heavy." %my_weight)
print("hes got %s eyes and %s hair." % (my_eyes, my_hair))
print("if i add %d, %d, and %d I get %d." % (my_height, my_age, my_weight, my_age + my_height + my_weight))

#6#
x = "there are %d types of people." % 10
binary="binary"
do_not="don't"
y="those who know %s and those who %s." % (binary, do_not)

print (x)
print (y)

print("I said: %r." % x)
print("I also said: '%s'." % y)

#7#
print("." * 10)
end1="c"
end2="h"
end3="e"
end4="e"
end5="s"
end6="e"
end7="b"
end8="u"
end9="r"
end10="g"
end11="e"
end12="r"

print(end1 + end2+end3+end4+end5+end6, )
print(end7+end8+end9+end10+end11+end12)

print(end1 + end2+end3+end4+end5+end6 )
print(end7+end8+end9+end10+end11+end12)

print(end1 + end2+end3+end4+end5+end6 ),
print(end7+end8+end9+end10+end11+end12)

#8 & 9#
formatter = "%r %r %r %r"
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
        "I had this thing.",
        "That you could type up right.",
        "but it didn't sing.",
        "so i said goodnight.")
)

print ("""
Theres something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
""")


#10#
tabby_cat="\tI'm tabbed in."
persian_cat="I'm split\non a line."
backslash_cat="I'm \\ a \\ cat."

fat_cat="""
I'll do a list:
    \t* Cat food
    \t*Fishies
    \t*Catnip\n\* Grass
 """
   
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)




##while True:
  #  for i in ["/", "-", "|", "\\", "|"]:
   #     print ("%s\r" % i)
    #     break

