'''
Created on Sep 5, 2018
@author: ishank
'''

def find_offset(nums, i, j):
        
    if j == i: return j
    if j == i+1:
        if nums[j] > nums[i]:
            return j
        else:
            return i
        
    mid = (j + i) // 2
    
    if nums[i] > nums[mid]:
        return find_offset(nums, i, mid)
    else:
        return find_offset(nums, mid, j)
    
def binary_search(nums, i, j, key):
        
    mid = (i+j) // 2
    if key == nums[mid]: return mid
    if j == i: return -1
    
    if nums[j] >= nums[mid]:
        if key >= nums[mid] and key <= nums[j]:
            return binary_search(nums, mid+1, j, key)
        else:
            return binary_search(nums, i, mid, key)
    
    if nums[i] <= nums[mid]:
        if key <= nums[mid] and key >= nums[i]:
            return binary_search(nums, i, mid, key)
        else:
            return binary_search(nums, mid+1, j, key)
    

print(binary_search([1,3], 0, 1, 4))