'''
Created on Feb 27, 2018

@author: ishank
'''

import time
def powerNumbers(index):
    
    def isPowerNumber(num):
        
        numSq = (int) (num ** 0.5) + 1           
        for i in range(2, numSq):  
            p = i
            while p <= num:
                p *= i
                if p == num:
                    return True
      
    c = 0
    num = 4    
    nums = []
      
    if index < 1: return 0
      
    while c < index:                
                  
        if isPowerNumber(num):
            nums.append(num)
            c += 1              
        num += 1
          
    return nums[-1]
      
  
    
            
    
      
start=time.time()
print(powerNumbers(120))
print(time.time()-start)
