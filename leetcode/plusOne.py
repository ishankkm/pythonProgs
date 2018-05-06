'''
Created on May 5, 2018
@author: ishank

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
'''

def plusOne(nums):
    
    nums[-1] = nums[-1] + 1
    stack = []
    carry = 0
    
    while len(nums) != 0:
        nums[-1] = nums[-1] + carry
        carry = 0
            
        if nums[-1] == 10:
            nums[-1] = 0 
            carry = 1
        stack.append(nums.pop())
    
    if carry == 1:
        stack.append(1)
            
    return stack[::-1]


print(plusOne([9,9,9,9]))

