'''
Created on May 12, 2018
@author: ishank

Given a linked list, determine if it has a cycle in it.
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

def hasCycle(head):
    
    slow, fast = head, head.next
    
    try:
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False
    
#     while head != None:
#         if hasattr(head, 'visited'):
#             return True
#         else:
#             head.visited = True
#     
#         head = head.next
#         
#     return False

ll = createLL([1,2,3,4,5,6,7,8,9])

ll.next.next.next.next.next.next.next.next = ll

print(hasCycle(ll))
