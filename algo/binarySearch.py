'''
Created on May 4, 2018
@author: ishank
'''

def binary_search(nums, target):
    
    start, end = 0, len(nums) - 1
    
    while start <= end:
        
        mid = start + (end - start) // 2
        
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return -1

def binary_search_rec(nums, target):
    # TODO    
    return

# print(binary_search([1,2,3,5,7,7,9], 10))
