'''
Created on Jan 24, 2018

@author: ishank
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        nodeStack = [root]
        result = [[root.val]]
        
        while len(nodeStack) > 0:
            nodes = nodeStack.pop()
            tempRes = []
            tempNS = []
            
            for node in nodes:            
                if node.left != None:
                    tempNS.append(node.left)
                    tempRes.append(node.left.val)
                
                if node.right != None:
                    tempNS.append(node.right)
                    tempRes.append(node.right.val)
                
            if len(tempNS) > 0:
                result.append(tempRes)
                nodeStack.append(tempNS)
        
        
        return result[::-1]