'''
Created on May 4, 2018
@author: ishank

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

def strStr(haystack, needle):
    
    h, n = len(haystack), len(needle)
        
    for i in range(h-n+1):
        if haystack[i:i+n] == needle:
            return i
    
    return -1
