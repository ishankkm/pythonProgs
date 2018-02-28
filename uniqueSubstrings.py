'''
Created on Nov 5, 2017

@author: ishank
'''

def uniqueSubstrings(string, length):
    
    return sorted(list(set(string[i : i + length] for i in range(len(string) - length + 1))))

print uniqueSubstrings("aaabbc", 2)
    
    
