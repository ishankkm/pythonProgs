'''
Created on Nov 7, 2017

@author: ishank
'''

def solution(A):
 
    t = list(set(A))     
    cnt = len(t)
     
    require = [0] * (max(A) + 1)
    
    for i in range(cnt):
        require[t[i]] += 1
    i = -1
    j = 0
    minLength = max(A) + 1
    minidx = 0     
     
    while i < len(A) and j < len(A):
        if cnt > 0:
            i += 1
            if i == len(A): 
                idx = 0 
            else: 
                idx = A[i]
            require[idx] -= 1
            if require[idx] >=0: 
                cnt -= 1
        else:
            if minLength > i - j + 1:
                minLength = i - j + 1
                minidx = j
                
            require[A[j]] += 1
            if require[A[j]] > 0: 
                cnt += 1
            j += 1
            
            
    if minLength == max(A) + 1: 
        return ""
    
    return A[minidx:minidx+minLength]
 
 
A = [7,3,7,4,3]    
print solution(A)     