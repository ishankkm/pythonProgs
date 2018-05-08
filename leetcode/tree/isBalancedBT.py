'''
Created on May 7, 2018
@author: ishank

Given a binary tree, determine if it is height-balanced.
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    
def arrayToBT(arr, i=0):
    
    if i > len(arr) - 1:
        return None
    
    if arr[i] == None:
        return None
    
    head = TreeNode(arr[i])
    head.left = arrayToBT(arr, 2 * i + 1)
    head.right = arrayToBT(arr, 2 * i + 2)
    
    return head

def treeHeight(node):
        
    if node == None: return 0
            
    left = treeHeight(node.left)
    right = treeHeight(node.right)
    
    if left == -1 or right == -1:
        return -1
    
    if abs(left - right) > 1: 
        return -1
    
    return 1 + max(left, right)

def isBalanced(root):
       
    if root == None: return True
    
    if treeHeight(root) == -1:
        return False
    
    return True



tree = arrayToBT([1,2,2,3,None,None,3,4,None,None,4])

print(isBalanced(tree))