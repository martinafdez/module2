# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 15:32:54 2019

@author: mluci

"""
###Doc Similarity Challenge###

import numpy as np

def readStopWords(stopword_file):
    stopword_file = open(stopword_file, 'r')
    slines=stopword_file.read()
    stopslines=slines.split()
#    print(stopslines)
    return stopslines
readStopWords('stopwords.txt')



def lexdiv1(text_file):
    cwfile=open(text_file, "r")
    new_file=cwfile.read().split()
    stops=readStopWords('stopwords.txt')
    g1={}
    for w in new_file:
        if w not in stops:
            if w in g1:
                g1[w] += 1
            else:
                g1[w] = 1
    return g1
lexdiv1('george01.txt')


def lexdiv2(text_file):
    cwfile=open(text_file, "r")
    new_file=cwfile.read().split()
    stops=readStopWords('stopwords.txt')
    g2={}
    for w in new_file:
        if w not in stops:
            if w in g2:
                g2[w] += 1
            else:
                g2[w] = 1
    return g2
lexdiv2('george02.txt')

def similarity(george, george2):
    g1=lexdiv1(george)
    g2=lexdiv2(george2)
    similarity=0
    
    for w in g1:
        if w in g2:
            similarity += 1
        else:
            pass
    georgeSim=similarity/(len(g1)+len(g2)-similarity)
    roundedGeorge=round(georgeSim, 3)
    print("compare: ({} <> {}) = {}".format(george, george2, roundedGeorge))

similarity('george01.txt','george02.txt')
similarity('george01.txt','george03.txt')
similarity('george01.txt','george04.txt' )
similarity('george02.txt','george03.txt' )
similarity('george02.txt','george04.txt' )
similarity('george03.txt','george04.txt' )


