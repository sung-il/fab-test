#-*- coding: utf-8 -*-
import time
import re
 
regex = re.compile('[A-z]+|[^0-9]')
 
f = open("smallbank.go",'r')
text=f.read()
 
wordss=text.split()
words=regex.findall(str(wordss))
word_counts=dict()
 
 
for word in words:
    word_counts[word]=word_counts.get(word,0)+1
 
for word,count in word_counts.items():
    for check in ["GetState", "PutState", "Marshal", "Unmarshal", "return"]:
        if word == check:
            print(word,count)
 
f.close()