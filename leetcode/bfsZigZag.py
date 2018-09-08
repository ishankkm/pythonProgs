'''
Created on Aug 30, 2018
@author: ishank
'''

class TreeNode():
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

def zigzagLevelOrder(root):
    
    if root == None:
        return []
    
    output, queue = {}, [(root, 0)]
    current = 0
    
    while current < len(queue):
        node = queue[current]
        output[node[1]] = output.get(node[1], []) + [node[0].val]
        
        if node[0].left:
            queue.append(tuple(( node[0].left, node[1] + 1 )))
            
        if node[0].right:
            queue.append(tuple(( node[0].right, node[1] + 1 )))
            
        current += 1
    
    
    rev = False
    zigzag = []
    
    for lvl in sorted(output.keys()):
        if rev:
            zigzag.append(output[lvl][::-1])
        else:
            zigzag.append(output[lvl])
        rev = not rev
            
    return zigzag
    
tree = arrayToBT([3,9,20,None,None,15,7])

print(zigzagLevelOrder(tree))