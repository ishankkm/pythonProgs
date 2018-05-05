'''
Created on May 4, 2018
@author: ishank

Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
'''

def searchInsert(nums, target):
    
    start, end = 0, len(nums) - 1
    
    
    if target > nums[-1]:
        return end + 1
    
    while start < end:
        
        mid = start + (end - start) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid
        
    return start + (end - start) // 2


print(searchInsert([0,1,2,4,5,6,9], 3))