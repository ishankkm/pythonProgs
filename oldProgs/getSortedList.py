'''
Created on Dec 28, 2017

@author: ishank
'''

def getSortedList(names):
    
    nameList = {}
    uniqueNames = []
    output = []
    
    for name in names:
        
        splitName = name.split()
        if nameList.has_key(splitName[0]):
            nameList[splitName[0]].append(splitName[1])
        else:
            nameList[splitName[0]] = [splitName[1]]
            uniqueNames.append(splitName[0])    
        
    newNameList = {}
    romConv = {}
    
    for key, val in nameList.items():
        
        if newNameList.has_key(key):
            newNameList[key].append(romToInt(v) for v in val)
        else:
            newNameList[key] = [romToInt(v) for v in val ]
            
        for v in val:
            romConv[romToInt(v)] = v
        newNameList[key] = sorted(newNameList[key])
        
    for un in uniqueNames:
        for it in newNameList[un]:
            output.append(un + ' ' + romConv[it])
    print newNameList
    for o in output:
        print o
    return output
    
def romToInt(number):
            
    letterIndex = {'C': 2, 'D': 1, 'I': 6, 'M': 0, 'L': 3, 'V': 5, 'X': 4}
    
    literal = [ 1000, 500, 100, 50, 10, 5, 1 ]   
    
    intNum = 0
    prev = None
    for letter in reversed(number):
        i = letterIndex[letter]
        val = literal[i]
        if (prev is None) or (prev <= val):
            intNum += val
        else:
            intNum -= val
        prev = val

    return intNum
    
arr = ['Louis IV', 'Louis V', 'Louis I', 'Louis II', 'Louis III', 'Louis IX', 'Louis VIII', 'Charlie II']
    
getSortedList(arr)







