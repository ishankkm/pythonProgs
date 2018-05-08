'''
Created on May 6, 2018
@author: ishank
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

def preorderTraversal(root):
    
    print(root.val, end=" ")
    
    if root.left != None:
        preorderTraversal(root.left)
        
    if root.right != None:
        preorderTraversal(root.right)


def postorderTraversal(root):
    
    if root.left != None:
        postorderTraversal(root.left)
    
    if root.right != None:
        postorderTraversal(root.right)
        
    print(root.val, end=" ") 
    
def inorderTraversal(root):
    
    if root.left != None:
        inorderTraversal(root.left)
    
    print(root.val, end=" ")
    
    if root.right != None:
        inorderTraversal(root.right)

def levelOrderTraversal(root):
    
    queue = [root]
    cur = 0
    
    while cur < len(queue):
        
        print(queue[cur].val, end=" ")
        
        if queue[cur].left != None:
            queue.append(queue[cur].left)
        
        if queue[cur].right != None:
            queue.append(queue[cur].right)
            
        cur += 1    

def BFS(root, key):
    
    queue = [root]
    cur = 0
    
    while cur < len(queue):
        
        if queue[cur].val == key:
            return True
        
        if queue[cur].left != None:
            queue.append(queue[cur].left)
        
        if queue[cur].right != None:
            queue.append(queue[cur].right)
            
        cur += 1   
    
    return False

def depthOrderTraversal(root):
    
    stack = [root]
    
    while len(stack) > 0:
        
        node = stack.pop()
        print(node.val, end=" ")
        
        if node.right != None:
            stack.append(node.right)
        
        if node.left != None:
            stack.append(node.left)
    
    return

def depthOrderTraversal_rec(root):
    
    if root == None:
        return
    
    print(root.val, end=" ")
    
    depthOrderTraversal(root.left)
    depthOrderTraversal(root.right)
    
def DFS(root, key):
    
    stack = [root]
    
    while len(stack) > 0:
        node = stack.pop()
        
        if node.val == key:
            return True
        
        if node.left != None:
            stack.append(node.left)
        
        if node.right != None:
            stack.append(node.right)
                
    return False


# A = [1, 2, 3, 4, 5, 6, 6]
# tree = arrayToBT(A, 0)
# print(DFS(tree, 7))

    

