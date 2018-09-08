'''
Created on Sep 6, 2018
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
    while lst != None:
        print(lst.x + '->')
        lst = lst.next

def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    
    ptrA, ptrB = headA, headB
    
    while ptrA != ptrB:
        
        if not ptrA: ptrA = headB
        if not ptrB: ptrB = headA
        
        ptrA = ptrA.next
        ptrB = ptrB.next
    
    return ptrA

ll1 = createLL([3])
ll2 = createLL([2, 3])

print(getIntersectionNode(ll1, ll2))