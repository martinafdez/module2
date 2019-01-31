# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:04:40 2019

@author: mluci
"""

###testingCountwords###
from countwordsfunctions import *
from challenge import *



#Task 1#
countWords('mobydick.txt', 'stopwords.txt')

#Task 2#
PrintTop20()

#Task 3#
readStopWords('stopwords.txt')

#challenge#
readStopWords('stopwords.txt')

lexdiv1('george01.txt')

lexdiv2('george02.txt')

similarity('george01.txt','george02.txt')
similarity('george01.txt','george03.txt')
similarity('george01.txt','george04.txt' )
similarity('george02.txt','george03.txt' )
similarity('george02.txt','george04.txt' )
similarity('george03.txt','george04.txt' )