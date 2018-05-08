'''
Created on May 6, 2018
@author: ishank

Given two binary trees, write a function to check if they are the same or not.
'''
from algo import binaryTree as bt

def isSameTree(p, q):
    
    if p == None and q == None:
        return True 
    
    if p == None or q == None:
        return False
    
    if p.val != q.val:
        return False
    
    if isSameTree(p.left, q.left) == False:
        return False
    
    if isSameTree(p.right, q.right) == False:
        return False
    
    return True


P = bt.arrayToBT([1,2,3])
Q = bt.arrayToBT([1,2,3])

print(isSameTree(P, Q))