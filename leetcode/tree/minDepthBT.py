'''
Created on May 9, 2018
@author: ishank

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
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

def minDepthBT(root):
    
    if root == None:
        return 0
    
    queue = [(root, 1)]
    cur = 0
            
    while cur < len(queue):
        
        node, lvl = queue[cur]
        
        if node.left == None and node.right == None:
            return lvl
        
        if node.left != None:
            queue.append((node.left, lvl+ 1))
        
        if node.right != None:
            queue.append((node.right, lvl + 1))
        
        cur += 1
        

tree = arrayToBT([3,9,20,None,None,15,7])
print(minDepthBT(tree))