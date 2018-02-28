'''
Created on Nov 12, 2017

@author: ishank
'''
from __future__ import print_function
from audioop import reverse

def dataAggregation():
    
    ipFile = open("input.txt")
    
    timeWindow = str(ipFile.readline()).split(", ")
        
    startDate = (int(timeWindow[0][:4]), int(timeWindow[0][5:7]))
    endDate = (int(timeWindow[1][:4]), int(timeWindow[1][5:7]))
    
    data = {}
    
    for _ in range(10):
    
        dataPoint = str(ipFile.readline()) 
        dataPointSplit = dataPoint.split(", ")
        
        if int(dataPointSplit[0][:4]) < startDate[0]:
            continue            
        elif int(dataPointSplit[0][:4]) > endDate[0]:
            continue        
        elif int(dataPointSplit[0][:4]) == startDate[0]:
            if int(dataPointSplit[0][5:7]) < startDate[1]:
                continue        
        elif int(dataPointSplit[0][:4]) == endDate[0]:
            if int(dataPointSplit[0][5:7]) > endDate[1]:
                continue
        
        if data.has_key(dataPointSplit[0][:7]):
                        
            d = data[dataPointSplit[0][:7]] 
            if d.has_key(dataPointSplit[1]):
                d[dataPointSplit[1]] += int(dataPointSplit[2])
            else:
                data[dataPointSplit[0][:7]][dataPointSplit[1]] = int(dataPointSplit[2])
        else:
            data[dataPointSplit[0][:7]] = {dataPointSplit[1]: int(dataPointSplit[2]) }
    
    timeRange = []
    
    year = startDate[0]
    month = startDate[1]
    
    while year < endDate[0]:
        for m in range(month, 13):
            s = str(year) + "-" + str(m).zfill(2)
            timeRange.append(s)
        month = 1
        year += 1
        
    for m in range(1, endDate[1] + 1):
        s = str(endDate[0]) + "-" + str(m).zfill(2)
        timeRange.append(s)
    
    timeRange.sort(reverse = True)
        
    for t in timeRange:
        s = ""
        if data.has_key(t):
            s = t + " "
            for key in sorted(data[t], reverse = True):
                s = s + key + ", " + str(data[t][key]) + ", "
            print(s[:-2])
    

dataAggregation()   