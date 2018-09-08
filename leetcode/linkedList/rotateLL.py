'''
Created on Sep 4, 2018
@author: ishank
'''

class ListNode(object):
    def __init__(self, x):
        self.x = x 
        self.next = None
    
def createLL(lst):    
    ll = ListNode(lst[0])
    head = ll
    
    for item in lst[1:]:
        newll = ListNode(item) 
        ll.next = newll
        ll = ll.next
    return head

def toString(lst):
    op = ""
    while lst != None:        
        op += str(lst.x) + '->'
        lst = lst.next
    print (op)
    
def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if not head:
        return None
    
    if not head.next:
        return head
    
    size = 0
    tail = head
    while tail.next != None:
        tail = tail.next 
        size += 1
    
    k = size - (k % size) + 1
    
    while k > 0:
        toString(head)
        node = head
        head = head.next
        node.next = None
        
        tail.next = node
        tail = tail.next
        k -= 1
        
    return head

ll = createLL([0,1,2])
toString(rotateRight(ll, 4) )
