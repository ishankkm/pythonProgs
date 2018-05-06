'''
Created on May 5, 2018
@author: ishank

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
'''

def merge(nums1, nums2):
    
    len1 = len(nums1)
    len2 = len(nums2)
    
    nums1 = nums1 + nums2
    lenf = len(nums1) - 1
    
    while len1 > 0 and len2 > 0:
        
        if nums1[len1 - 1] > nums2[len2 - 1]:
            nums1[lenf] = nums1[len1 - 1]
            len1 -= 1
        else:
            nums1[lenf] = nums2[len2 - 1]
            len2 -= 1
        lenf -= 1
        
    if len1 == 0:
        nums1[:lenf+1] = nums2[:len2]
    
    return nums1


print(merge([1,2,3,9], [2,3,4,5,7,11]))