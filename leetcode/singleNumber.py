'''
Created on May 11, 2018
@author: ishank

Given a non-empty array of integers, every element appears twice except for one. Find that single one.
without using extra memory
'''

def singleNumber(nums):
    
    a = 0    
    for i in nums:
        a = a ^ i    
    return a

    return 2 * sum(set(nums)) - sum(nums)


print(singleNumber([1,2,3,4,5,4,3,2,1]))