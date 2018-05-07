'''
Created on May 6, 2018
@author: ishank

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    
def arrayToBT(arr, i=0):
    
    if i > len(arr) - 1:
        return None
    
    head = TreeNode(arr[i])
    head.left = arrayToBT(arr, 2 * i + 1)
    head.right = arrayToBT(arr, 2 * i + 2)
    
    return head

def isSymmetricTree(root):
    
    def isTreeSame(p, q):
        
        if p == None and q == None:
            return True
        
        if p == None or q == None:
            return False
        
        if p.val != q.val:
            return False
        
        if not isTreeSame(p.left, q.right):
            return False
        
        if not isTreeSame(p.right, q.left):
            return False
    
        return True
    
    
    if isTreeSame(root.left, root.right):
        return True
    
    return False

def isSymmetricTree_itr(root):
    
    queue_p = [root]
    queue_q = [root]
    cur = 0
    
    while cur < len(queue_p):
        if len(queue_p) != len(queue_q):
            return False
        
        if queue_p[cur].val != queue_q[cur].val:
            return False
        
        if queue_p[cur].left != None or queue_q[cur].right != None:
            if queue_p[cur].left != None and queue_q[cur].right != None:
                queue_p.append(queue_p[cur].left)
                queue_q.append(queue_q[cur].right)
            else:
                return False
    
        if queue_p[cur].right != None or queue_q[cur].left != None:
            if queue_p[cur].right != None and queue_q[cur].left != None:
                queue_p.append(queue_p[cur].right)
                queue_q.append(queue_q[cur].left)
            else:
                return False
        cur += 1
    
    return True
    
    

tree = arrayToBT([1,2,2,3,4,4,3])
print(isSymmetricTree_itr(tree))


    
    
