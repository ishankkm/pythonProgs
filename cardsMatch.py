'''
Created on Nov 7, 2017

@author: ishank
'''

def solution(A, B):
    
    scoreA = 0
    
    cardOrder = { "A" : 14, 
                  "K" : 13, 
                  "Q" : 12, 
                  "J" : 11, 
                  "T" : 10, 
                  "9" : 9, 
                  "8" : 8, 
                  "7" : 7, 
                  "6" : 6, 
                  "5" : 5, 
                  "4" : 4, 
                  "3" : 3, 
                  "2" : 2}
    
    for i in xrange(len(A)):               
        if cardOrder[A[i]] > cardOrder[B[i]]:
            scoreA += 1  
    
    return scoreA  
            
A = "23A84Q"
B = "K2Q25J"

print solution(A, B)