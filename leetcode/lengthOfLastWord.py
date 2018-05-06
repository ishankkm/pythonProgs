'''
Created on May 5, 2018
@author: ishank

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word in the string. If the last word does not exist, return 0.
'''

def lengthOfLastWord(s):
    
    arr = s.strip().split(sep=" ", maxsplit=-1)

    return len(arr[-1])

print(lengthOfLastWord("Hello WorldI"))