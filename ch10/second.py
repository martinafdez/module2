


counts={'a':3, 'c':1, 'b':5} #ditionary
labels=list(counts.keys()) #casting dictionary keys into a list and assigning it to the variable 'labels'
labels.sort(key=lambda k:counts[k]) #now that labels holds the dictionary as a list, can do a list operation like sort in it. argument of sort is lambda which returns the original key and value pair but sorted by the key
#print(sorted(counts.items(), key=lambda kv:kv[1]))    

