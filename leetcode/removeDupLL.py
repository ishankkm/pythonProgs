'''
Created on May 5, 2018
@author: ishank

Given a sorted linked list, delete all duplicates such that each element appear only once.
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


def deleteDuplicates(root):
    
    prev = root
    cur = prev.next
    
    while cur != None:
        if prev.x == cur.x:
            cur = cur.next
            prev.next = cur
        else:
            prev = prev.next
            cur = cur.next

    return root

head = deleteDuplicates(createLL([2,2,2,3,4,5,5,5,6,6]))
toString(head)