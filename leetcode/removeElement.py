'''
Created on May 4, 2018
@author: ishank

Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''

def removeElement(nums, val):
    
    cur = 0
    
    for n in nums:
        if n != val:
            nums[cur] = n
            cur += 1 
    
    return nums[:cur]

print(removeElement([1,1,2,3,1,3,1,3], 3))


