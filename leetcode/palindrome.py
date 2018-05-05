'''
Created on May 3, 2018
@author: ishank

Determine whether an integer is a palindrome.
'''

def isPalindrome(x):
    
    num, rev = x, 0 
    
    while x!= 0:
        rev = rev * 10 + x % 10
        x = x // 10
    
    return rev == num

print(isPalindrome(10001))