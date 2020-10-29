#-*- coding: utf-8 -*-
import time
import re
 
regex = re.compile('[a-z]+|[A-Z]+|[^0-9]')
 
f = open("smallbank.go",'r')
text=f.read()
 
wordss=text.split()
words=regex.findall(str(wordss))
word_counts=dict()
 
 
for word in words:
    word_counts[word]=word_counts.get(word,0)+1
 
for word,count in word_counts.items():
    print(word,count)
 
f.close()