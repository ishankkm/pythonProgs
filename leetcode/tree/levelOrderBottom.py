'''
Created on May 7, 2018
@author: ishank

Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root).
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

def levelOrderBottom(root):
    
    queue = [(root, 0)]
    cur = 0
    
    while cur < len(queue):
        
        node, lvl = queue[cur]
        
        if node.left != None:
            queue.append((node.left, lvl + 1))
            
        if node.right != None:
            queue.append((node.right, lvl + 1))
        
        cur += 1
        
    result = []
        
    for node, lvl in queue:
        
        if len(result) == lvl:
            result.append([node.val])
        else:
            result[lvl].append(node.val)
    
    return result[::-1]

A = [3,9,20,None,None,15,7]
tree = arrayToBT(A, 0)

print(levelOrderBottom(tree))