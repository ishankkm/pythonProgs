'''
Created on May 3, 2018
@author: ishank

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
'''

def romanToInteger(s):
    
    intVal = 0
    
    order = {'M': 1, 'D': 2, 'C': 3, 'L': 4, 'X': 5, 'V': 6, 'I': 7}
    value = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10,'V': 5, 'I': 1}

    for i in range(len(s)):
        if i < len(s) - 1:
            if order[s[i]] > order[s[i+1]]:
                intVal -= value[s[i]]
                continue
        intVal += value[s[i]]
    
    return intVal

print(romanToInteger("MCMXCIV"))