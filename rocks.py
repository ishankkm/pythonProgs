'''
Created on Oct 2, 2017

@author: ishan
'''
import math

def wrapRibbon(ribLen, rocks):
        
    r = len(rocks)
    
    distMatrix = [[0 for i in range(r)] for j in range(r)]
    
    for i in range(len(rocks)):
        
        for j in range(len(rocks)):
            
            diffX = rocks[i][0] - rocks[j][0]
            diffY = rocks[i][1] - rocks[j][1]
                        
            lenRock = math.sqrt( diffX*diffX + diffY*diffY )
                        
            distMatrix[i][j] = lenRock            
            
    lst = []
    
    for i in range(r):
        for j in range(i+1, r):
            if distMatrix[i][j] != 0:
                lst.append(distMatrix[i][j])
                
    lst.sort()
    
    cnt = 0.0
    tot = 0
    
    
    for i in range(r):
        cnt += lst[i]
        if cnt < ribLen:
            tot += 1
    
    return tot

rocks = [[0.0,0.0],[0.0,3.0],[3.0,3.0]]

print wrapRibbon(10.0, rocks)


    
     
    