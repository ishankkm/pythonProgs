'''
Created on May 5, 2018
@author: ishank

Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum
'''

def maxSubArray(nums):
    
    maxSum, sumAll = nums[0], 0
    
    for n in nums:
        maxSum = max(maxSum, sumAll + n)
        # sum(1..i) for i in 1..N (non negative)
        sumAll = max(0, sumAll + n)         
        
    return maxSum

a = [-2, -3, 4, -1, -2, 1, 5, -3, -4]
print("Maximum contiguous sum is" , maxSubArray(a))

