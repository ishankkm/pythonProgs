'''
Created on May 11, 2018
@author: ishank

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
'''

def isPaindrome(s):

    new_str = ''.join(filter(str.isalnum, s)).lower()
#     new_str = ''.join([c if c.isalnum() else '' for c in s])
    return new_str == new_str[::-1]

print(isPaindrome("race a car"))
