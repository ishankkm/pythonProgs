


def melon_count(boxes, melons):
    
    numMelon = len(melons)
    maxCount = 0
    
    for i in range(numMelon):
        
        c = 0
        for j in range(len(boxes)):           
            
            if (c + i) >= numMelon:
                break
            
            if boxes[j] >= melons[c + i]:
                c += 1
                
        if c > maxCount:
            maxCount = c
   
    return maxCount


print melon_count([1,2,1,2], [3,2,1])
   
   

  