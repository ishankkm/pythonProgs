'''
Created on May 3, 2018
@author: ishank

Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
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
        print(lst.x, end='->')
        lst = lst.next

def mergeTwoLists(l1, l2):
    
    head = l1 if l1.x < l2.x else l2
    current = ListNode(0)
    
    while l1 != None and l2 != None:
        if l1.x < l2.x:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    current.next = l1 if l1 != None else l2
    
    return head

def mergeTwoListsRec(l1, l2):
    
    if l1 == None: return l2
    elif l2 == None: return l1
    
    head = l1 if l1.x < l2.x else l2
    
    if l1.x < l2.x:
        l1.next = mergeTwoLists(l1.next, l2)
    else:
        l2.next = mergeTwoLists(l1, l2.next)
    
    return head


      
l1 = createLL([1,3,5])
l2 = createLL([2,4,5,6,7])
toString(mergeTwoListsRec(l1, l2))

