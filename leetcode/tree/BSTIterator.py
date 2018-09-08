'''
Created on Sep 1, 2018
@author: ishank
'''

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.iterateLeft(root)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if len(self.stack) > 0 else False

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self.iterateLeft(node.right)
        return node.val
    
    def iterateLeft(self, node):
        while node != None:
            self.stack.append(node)
            node = node.left
        
