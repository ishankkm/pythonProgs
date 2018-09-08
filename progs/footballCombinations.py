'''
Created on Sep 8, 2018
@author: ishank
'''


def footballCombinations(teamGoal):
    
    if len(teamGoal) < 2: return "0.00"
    avg_dict = {}
    
    for tavg in teamGoal:
        avg_dict[tavg] = avg_dict.get(tavg, 0) + 1
        
    largest_avg = max(avg_dict.keys())
    num_avg = avg_dict[largest_avg]
    
    if num_avg > 1:
        numr = num_avg * (num_avg-1) / 2
    else:
        numr = avg_dict[sorted(avg_dict.keys())[-2]]
    
    denr = len(teamGoal) * (len(teamGoal) - 1) / 2
    
    units = numr // denr
    
    result =  str("%.2f" % (numr * 100 / denr)).split('.')
    
    return str(units) + '.' + result[0][-2:]

print(footballCombinations([3,3,4]))
        
