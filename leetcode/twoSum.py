'''
Created on May 3, 2018
@author: ishank

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """               
    num_dict = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in num_dict.keys() and i != num_dict.get(complement):
            return [num_dict.get(complement), i]
        num_dict[nums[i]] = i


print(twoSum([2,7,11,15], 9))
