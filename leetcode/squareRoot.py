'''
Created on May 5, 2018
@author: ishank

Implement int sqrt(int x)
'''

def squareRoot(x):
    
    factor = x
    
    while factor * factor > x:
        factor = (factor + x / factor) / 2
    
    return factor

print(squareRoot(105))
print(105 ** 0.5)
