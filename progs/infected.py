'''
Created on Sep 14, 2017

@author: ishan

'''

from __future__ import print_function

fo = open("input.txt")

line = fo.readline()
l1 = list(line.rstrip())
l = len(l1)

arr = []

for i in l1:
    z = int(i)
    arr.append(z)

for i in range(l -1):
    line = fo.readline()
    if line == "": break
    l1 = list(line.rstrip())  
    
    for j in l1:
        arr.append(int(j))


i = 0
while i < len(arr):
    count = 0
    
    if i == 12:
        fwe = 0
    
    if i != 0 and (i % l) != 0:
        if arr[i-1] == 1 and arr[i] != 1:
            count += 1
    
    if i != (l*l - 1) and i % l != (l - 1):
        
        if arr[i + 1] == 1 and arr[i] != 1:
            count += 1      

    if (i / l) != 0:
        if arr[i - l] == 1 and arr[i] != 1:
            count += 1
            
    if i < (l*(l-1) - 1):
        if arr[i + l] == 1 and arr[i] != 1:
            count += 1
    
    if count > 1:
        arr[i] = 1
        i = -1
        for j in range(len(arr)):
            print(arr[j],end=" ")
            if (j % l) == (l-1):
                print("")
        print("")
        
    i = i + 1  
    

for i in range(len(arr)):
    print(arr[i],end=" ")
    if (i % l) == (l-1):
        print("")
    
    
    