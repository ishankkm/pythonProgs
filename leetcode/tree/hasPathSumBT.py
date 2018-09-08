'''
Created on May 10, 2018
@author: ishank

Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
such that adding up all the values along the path equals the given sum.
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

def hasPathSum(root, key):
    
    if root == None:
        return False
        
    stack = [(root, root.val)]
    
    while len(stack) > 0:
        
        node, val = stack.pop()
        
        if node.left == None and node.right == None:
            if val == key:
                return True
        
        if node.right != None:
            stack.append((node.right, val + node.right.val))
            
        if node.left != None:
            stack.append((node.left, val + node.left.val))
    
    return False

tree = arrayToBT([5,4,8,11,None,13,4,7,2,None,None,None,1])
print(hasPathSum(tree, 23))