'''
Created on Oct 3, 2017

@author: ishan
'''


def dijkstras(graph, source):
           
    unvisitedNodes = []
    
    vertex = [graph[0][i] for i in range(len(graph))]
    dist = []
    prev = []    
    
    for i in range(len(vertex)):
        dist.append(None)
        prev.append(None)
        unvisitedNodes.append(i)
        
    dist[source] = 0
    
    while unvisitedNodes != []:
        dist.sort()
        
        
    
    
    
    
    
    