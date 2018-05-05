'''
Created on May 3, 2018
@author: ishank

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''

def removeDuplicates(nums):
    
    cur = 1
    
    for i in range(1, len(nums)):
        if nums[cur - 1] != nums[i]:
            nums[cur] = nums[i]
            cur += 1
            
    return nums[:cur]

print(removeDuplicates([1,1,2,3,4]))