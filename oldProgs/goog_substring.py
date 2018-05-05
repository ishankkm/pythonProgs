'''
Created on Nov 21, 2017

@author: ishank
'''


def solution(A, B):
    
    if len(B) == 0: return 1
    elif len(A) == 0: return -1
    
    startIndexA = -1
    for i, c in enumerate(A):
        if B[0] == c:
            startIndexA = i
            break
    if startIndexA == -1:
        return -1
    
    indexA = startIndexA
    for c in B:
        if A[indexA] != c:
            return -1
        else:
            indexA = (indexA + 1) % len(A)
            
    if len(A) - startIndexA > len(B):
        return 1
    
    if startIndexA == 0 and (len(B) % len(A) == 0):
        return len(B) / len(A)
    else:
        return (len(B) / len(A)) + 1
    

A = "abcdabcd"
B = "abcdabcdabcdabcda"

print solution(A, B)