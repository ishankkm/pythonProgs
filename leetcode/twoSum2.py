'''
Created on Sep 6, 2018
@author: ishank
'''

def twoSum( numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    visited = {}
    for i, num in enumerate(numbers):
        
        diff = target - num
        if num in visited.keys(): 
            return [visited[num], i + 1]
        else:             
            visited[diff] = i + 1
    
    return []

a = [212,221,227,230,277,282,306,314,316,321,325,997]
b = 542


print(twoSum(a, b))
