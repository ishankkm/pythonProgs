'''
Created on Oct 31, 2017

@author: ishank
'''

def dotProduct(x, y):
    
    if len(x) != len(y):
        return 0
    
    sum = 0   
    
    for i in range(len(x)):
        
        sum += x[i] * y[i]
        
    return sum


x = [1,2]
y = [1,2]

print dotProduct(x, y)
    