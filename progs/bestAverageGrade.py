'''
Created on Oct 31, 2017

@author: ishank
'''


def bestAverageGrade(scores):
    
    scoresDict = {}
    
    if len(scores) == 0:
        return 0
    
    for s in scores:
        
        if not scoresDict.has_key(s[0]):            
            scoresDict[s[0]] = [s[1]]
        else:            
            scoresDict[s[0]].append(s[1])
    
    max = -308915776
    
    for k,v in scoresDict.items():
        
        sum = 0        
        for num in v:
            sum += int(num)
        
        avg = sum / len(v)
        
        if avg > max:
            max = avg
            
    return max    
    
    
    

scores = [["Sarah", 99],
          ["Sarah", 89],
          ["Tony", 65]]

print bestAverageGrade(scores)