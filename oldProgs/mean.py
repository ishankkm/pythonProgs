'''
Created on Sep 14, 2017

@author: ishan
'''


fo = open("input.txt")

line = fo.readline()

a = line.split(",")

sum = float(0)

for c in a:
    sum = sum + float(int(c))

print int(round(sum/len(a)))

