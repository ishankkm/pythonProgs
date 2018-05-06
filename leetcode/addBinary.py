'''
Created on May 5, 2018
@author: ishank

Given two binary strings, return their sum (also a binary string).
'''

def addBinary(a, b):
    
    carry = 0
    lenA, lenB = len(a), len(b)
    result = ""
    
    padding = ""
    for i in range(abs(lenA - lenB)):
        padding += "0"
    
    if lenA > lenB:
        b = padding + b
    elif lenB > lenA:
        a = padding + a
               
    for i in range(len(a)):
        res = int(a[-(i+1)]) + int(b[-(i+1)]) + carry
        
        if res == 3:
            result += "1"
            carry = 1
        elif res == 2:
            result += "0"
            carry = 1            
        else:
            result += str(res)
            carry = 0
            
    if carry == 1:
        result += "1"
    
    return result[::-1]

def addBinaryDirect(a, b):
    
    return "{0:b}".format(int(a, 2) + int(b, 2))
    return str(bin(int(a, 2) + int(b, 2)))[2:]

A = "11101101"
B = "10101010"

print(addBinaryDirect(A, B))
print(addBinary(A, B))

