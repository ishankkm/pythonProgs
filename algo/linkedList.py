'''
Created on May 6, 2018
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
        print(lst.x, end='->')
        lst = lst.next
