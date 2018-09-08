'''
Created on May 10, 2018
@author: ishank

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
eg. 
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

def generate(numRows):
    
    if numRows == 0:
        return []
    
    result = [[1]]
    
    for _ in range(1,numRows):
        val = [1]
        for j in range(len(result[-1]) - 1):
            val.append(result[-1][j] + result[-1][j+1])
        val.append(1)
        result.append(val)
        print(val)
    return result

        
print(generate(3))
