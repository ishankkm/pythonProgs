'''
Created on May 14, 2018
@author: ishank


Given an array of size n, find the majority element. 
The majority element is the element that appears more than n/2 times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

def majorityElement(nums):
    
    majority = 0
    count = 0
    
    for num in nums:
        if count == 0: majority = num
        if num == majority: count += 1
        else: count -= 1
    
    return majority
    
    if len(nums) == 1: return nums[0] 
    
    num_count = {}
    nums_len = len(nums)
    
    for num in nums:
        if num in num_count.keys():
            num_count[num] += 1
            if num_count[num] > nums_len / 2:
                return num
        else:
            num_count[num] = 1

    return None


print(majorityElement([2]))