'''
Created on May 3, 2018
@author: ishank

Given a 32-bit signed integer, reverse digits of an integer.
'''

def reverse(x):
    
    sign = False if x < 0 else True
    if sign == False: x = -x 
    rev = 0
    
    while x != 0:
        rev = rev * 10 + x % 10
        x = x // 10
    
    return rev if sign else -rev

print(reverse(-10001))