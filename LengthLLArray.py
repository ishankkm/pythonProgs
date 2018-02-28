'''
Created on Nov 8, 2017

@author: ishank
'''


def solution(A):
    
    if A[0] == -1: return 1
    lenLL = 1
    current = A[0]
    
    for _ in xrange(1, len(A)):        
        if A[current] == -1: return lenLL + 1
        else: 
            lenLL += 1
            current = A[current]
    
    return lenLL

A = [1,4,-1,2,3]

print solution(A)