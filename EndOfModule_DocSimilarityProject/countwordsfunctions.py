# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:01:01 2019

@author: mluci
"""




####Doc Similarity Project###

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
   
countWords('mobydick.txt', 'stopwords.txt')



#task 2#
def PrintTop20():
    counts=countWords('mobydick.txt', 'stopwords.txt')
    csorted=sorted(counts.items(), key=lambda kv:kv[1], reverse=True)[:20]
    for word, times in csorted:
        print ("{} = {}".format(word, times))
PrintTop20()





##task2##   
#version2#             
#def printTop20():
#    text_file = open('mobypara.txt', 'r')
#    lines = text_file.read() 
#    counts = Counter(lines.split())
#    top_20 = counts.most_common(20)
#    print(top_20)
#printTop20()


