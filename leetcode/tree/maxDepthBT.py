'''
Created on May 6, 2018
@author: ishank

Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
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

def maxDepthBT(root):
    
    if root == None: return 0    
    return 1 + max(maxDepthBT(root.left), maxDepthBT(root.right))

tree = arrayToBT([1,2,2,3,4,4,3])
print(maxDepthBT(tree))