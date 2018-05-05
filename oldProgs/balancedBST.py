'''
Created on Feb 27, 2018
@author: ishank

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of 
the two subtrees of every node never differ by more than 1.

'''
from math import floor

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        
        t = TreeNode(nums[floor(len(nums)/2)])
        
        t.left = self.sortedArrayToBST(nums[:floor(len(nums)/2)])
        t.right = self.sortedArrayToBST(nums[floor(len(nums)/2)+1:])
        
        return t

a = Solution()
a.sortedArrayToBST([-10, -3, 0, 5, 9])