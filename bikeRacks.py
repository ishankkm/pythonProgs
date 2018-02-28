'''
Created on Nov 8, 2017

@author: ishank
'''

def solution(A):
    
    maxDiff = 0    
    A.sort()
    
    for i in range(1, len(A)):
        
        diff = A[i] - A[i - 1]
        if diff > maxDiff: maxDiff = diff
    
    return maxDiff / 2


A = [5,5]

print solution(A)