'''
Created on Aug 21, 2018
@author: ishank
'''


def lengthOfLongestSubstring(s):
    
    visited, cur_len, max_len = {}, 0, 0
    
    for i in range(len(s)):
        prev_index = visited.get(s[i], -1)
        
        if prev_index == -1 or (i - cur_len > prev_index):
            cur_len += 1
        else: 
            if cur_len > max_len:
                max_len = cur_len
            
            cur_len = i - prev_index
        
        visited[s[i]] = i
    
    return max_len if max_len > cur_len else cur_len

print(lengthOfLongestSubstring("b"))