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


A = [10, 0, 8, 2, -1, 12, 11, 3]

print(solution(A))