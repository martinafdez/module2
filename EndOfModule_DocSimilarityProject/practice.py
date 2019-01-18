# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:52:42 2019

@author: mluci
"""
#task3#
def readStopWords(stopword_file):
    stopword_file = open(stopword_file, 'r')
    slines=stopword_file.read()
    stopslines=slines.split()
#    print(stopslines)
    return stopslines
readStopWords('stopwords.txt')


#task 1#
def countWords(text_file, stops):
    cwfile=open(text_file, "r")
    new_file=cwfile.read().split()
    stops=readStopWords('stopwords.txt')
    count={}
    for w in new_file:
        if w not in stops:
            if w in count:
                count[w] += 1
            else:
                count[w] = 1
#    print(count)
    return count
                
#    for word, times in count.items():
#        print (word, times)
   
countWords('mobypara.txt', 'stopwords.txt')

#task 2#
def PrintTop20():
    counts=countWords('mobypara.txt', 'stopwords.txt')
    l=sorted(counts.items(), key=lambda kv:kv[1], reverse=True)[:20]
    for word, times in l:
        print ("{} = {}".format(word, times))
PrintTop20()



   
    

