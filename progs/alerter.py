'''
Created on Feb 28, 2018
@author: ishank



'''

def alert(inputs, windowSize, allowedIncrease):

    s, e = 0, windowSize - 1
    currentAvg = sum(inputs[:windowSize]) / windowSize + 1
        
    while e < len(inputs):
        win = inputs[s:e+1]
        winSum, winMax = sum(win), max(win)  
        winAvg = winSum / windowSize
        
        if currentAvg * allowedIncrease < winAvg: return True
        
        check = winAvg * allowedIncrease
        
        if winMax >= check: return True
        
        e, s = e + 1, s + 1
        
        currentAvg = min(winAvg, currentAvg)
        
    return False

print(alert([4,4,2,2,4,6,6], 4, 1.5))



