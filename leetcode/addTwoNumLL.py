'''
Created on Aug 5, 2018
@author: ishank
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x 
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
        print(lst.val, end='->')
        lst = lst.next
        
def addTwoNumbers(l1, l2):
    
    sumLL = ListNode(0)
    sumHead = sumLL
    carry = 0
    while(l1 != None or l2 != None):
        
        l1_val = l1.val if l1 != None else 0
        l2_val = l2.val if l2 != None else 0
        
        int_sum = l1_val + l2_val + carry
        carry = int_sum // 10
        sumLL.next = ListNode(int_sum % 10)
        sumLL = sumLL.next
        
        l1 = l1.next if l1 != None else None
        l2 = l2.next if l2 != None else None
    
    
    if carry == 1:
        sumLL.next = ListNode(1)
        
    return sumHead.next

L1 = createLL([5])
L2 = createLL([5])

print(toString(addTwoNumbers(L1, L2)))

