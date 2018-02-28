'''
Created on Dec 21, 2017

@author: ishank
'''

num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def num2roman(num):

    roman = ''
    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r                
                num -= i
    return roman

def rom2num(number):
            
    letterIndex = {'C': 2, 'D': 1, 'I': 6, 'M': 0, 'L': 3, 'V': 5, 'X': 4}
    
    literal = [ 1000, 500, 100, 50, 10, 5, 1 ]   
    
    intNum = 0
    prev = None
    for letter in reversed(number):
        i = letterIndex[letter]
        val = literal[i]
        if (prev is None) or (prev <= val):
            intNum += val
        else:
            intNum -= val
        prev = val

    return intNum

for i in range(100011):
    if rom2num(num2roman(i)) != i:
        print "Fail"

# print num2roman(23)