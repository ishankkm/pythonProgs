'''
Created on Nov 21, 2017

@author: ishank
'''

def solution(A, B):
    
    values = set(A)
    longestPathLen = 0
    for val in values:
        pathLen = findLongestPath(A, B, val)
        if pathLen > longestPathLen:
            longestPathLen = pathLen
    
    return longestPathLen


def dfs(adjMat, root, depth, visited, n, path):
    
    maxDepth = depth
    
    for i in range(n):
        if i not in visited and adjMat[i][root]:
            visited.append(i)
            newPath = path + "-" + str(i)
            newDepth = dfs(adjMat, i, depth + 1, visited, n, newPath)
            if newDepth > maxDepth:
                print newPath
                maxDepth = newDepth
    
    return maxDepth

def findLongestPath(A, B, val):
    
    maxDepth = 0
    
    adjMat = [[0 for _ in range(len(A))] for _ in range(len(A)) ]
    
    for i in range(len(A) - 1):
        nodeA = B[2 * i]
        nodeB = B[2 * i + 1]
        
        if A[nodeA - 1] == val and A[nodeB - 1] == val:
            adjMat[nodeA - 1][nodeB - 1] = 1 
            adjMat[nodeB - 1][nodeA - 1] = 1
              
    for i in range(len(A)):
        if A[i] == val:
            newDepth = dfs(adjMat, i, 0, [i], len(A), str(i))
            if newDepth > maxDepth:
                maxDepth = newDepth
            
#     print maxDepth
#               
#     for p in range(len(A)):
#         s = ""
#         for q in range(len(A)):
#             s = s + str(adjMat[p][q])
#         print s
#     print "\n"
    
    return maxDepth
    
    
# A = [1,1,1,2,2]
# B = [1,2,1,3,2,4,2,5]


A = [1,1,1,1,1,2,1,1]
B = [1,2,2,4,1,3,3,5,3,6,6,7,6,8]

print solution(A, B)