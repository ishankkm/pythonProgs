'''
Created on Jun 3, 2018
@author: ishank
'''
from __future__ import print_function

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        
class TreeTraversal:
    def __init__(self):
        pass    
        
    # covert array format to tree format  
    @staticmethod    
    def arrayToBST(arr, i=0):
        
        if (i > len(arr) - 1) or (arr[i] == None):
            return None
        
        root = Node(arr[i])
        root.left = TreeTraversal.arrayToBST(arr, 2 * i + 1)
        root.right = TreeTraversal.arrayToBST(arr, 2 * i + 2)
            
        return root
    
    @staticmethod
    def levelOrderTraversal(root):
        
        queue = [root]
        cur, arr = 0, []
        
        while cur < len(queue):
            arr.append(queue[cur].value)
            
            if queue[cur].left != None:
                queue.append(queue[cur].left)
            
            if queue[cur].right != None:
                queue.append(queue[cur].right)
            
            cur += 1
                
        return arr
    
    @staticmethod
    def depthOrderTraversal(root):
        
        stack = [root]
        arr = []
        
        while len(stack) > 0:
            
            node = stack.pop()
            arr.append(node.value)
            
            if node.right != None:
                stack.append(node.right)
            
            if node.left != None:
                stack.append(node.left)
                
        return arr
    
    @staticmethod
    def depthOrderTraversal_rec(root):
        
        if root == None:
            return []
        
        arr = [root.value]
        arr += TreeTraversal.depthOrderTraversal_rec(root.left)
        arr += TreeTraversal.depthOrderTraversal_rec(root.right)
        
        return arr

class BST:
    def __init__(self):
        pass
    
    @staticmethod
    def insert(root, key):
        
        if root is None:
            root = Node(key)
            return root
                    
        elif root.value < key:
            if root.right != None:
                BST.insert(root.right, key)
            else:
                root.right = Node(key)
        
        elif root.value > key:
            if root.left != None:
                BST.insert(root.left, key)
            else:
                root.left = Node(key)
                
        return root
    
    @staticmethod
    def balancedBST(arr):
        
        if len(arr) == 1:
            return Node(arr[0])
        elif len(arr) == 0:
            return None
        
        arr = sorted(arr)
        
        mid = len(arr) // 2
        
        root = Node(arr[mid])
        root.left = BST.balancedBST(arr[:mid])
        root.right = BST.balancedBST(arr[mid+1:])
        
        return root
        
    @staticmethod
    def dfs(root, key):
        
        if root == None:
            return False
        
        if root.value == key:
            return True
        elif root.value < key:
            return BST.dfs(root.right, key)
        else:
            return BST.dfs(root.left, key)
    
    @staticmethod
    def inorderSuccessor(root):
        node = root         
        while node.left != None:
            node = node.left
            
        return node
           
    @staticmethod
    def delete(root, key):
        
        if root == None:
            return
        
        if root.value < key:
            root.right = BST.delete(root.right, key)
        elif root.value > key:
            root.left = BST.delete(root.left, key)
        else:
            if root.left == None:
                node = root.right
                root = None
                return node
            elif root.right == None:
                node = root.left
                root = None
                return node
            else:
                root.value = BST.inorderSuccessor(root.right).value 
                root.right = BST.delete(root.right, root.value)
                return root 
    
        return root

# tree = [2,1,3,4]
# print(TreeTraversal.levelOrderTraversal(BST.balancedBST(tree)))    



# tree = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, None, None, 13, None]
# bst = TreeTraversal.arrayToBST(tree)
# print(TreeTraversal.levelOrderTraversal(bst))
# print(BST.delete(bst, 13).value)
# print(TreeTraversal.levelOrderTraversal(bst))









