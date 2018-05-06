'''
Created on May 5, 2018
@author: ishank

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

def climbStairs(n):
    
    first, second = 1, 2
    
    for _ in range(2, n):
        
        second = first + second
        first = second - first
    
    return second   

print(climbStairs(10))
