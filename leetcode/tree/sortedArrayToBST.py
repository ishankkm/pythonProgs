'''
Created on May 7, 2018
@author: ishank

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.    
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(nums):
    
    if len(nums) == 0:
        return
    elif len(nums) == 1:
        return TreeNode(nums[0])
    
    half = len(nums) // 2
    
    node = TreeNode(nums[half])
    
    node.left = sortedArrayToBST(nums[:half])
    node.right = sortedArrayToBST(nums[half + 1:])
    
    return node


tree = [-10,-3,0,5,9]

root = sortedArrayToBST(tree)

print(root.right.left.val)