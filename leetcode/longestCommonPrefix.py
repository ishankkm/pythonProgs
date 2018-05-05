'''
Created on May 3, 2018
@author: ishank

find the longest common prefix strning amongst an array of strnings.
'''



def longestCommonPrefix(strns):
    
    prefix = ""
    
    for i, c in enumerate(strns[0]):
        for strn in strns:
            if i < len(strn):
                if strn[i] != c:
                    return prefix
            else:
                return prefix
        prefix += c
    
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))
