'''
Created on Aug 21, 2018
@author: ishank
'''

def uniqueFruits(trees):
    
    tree_types = []
    cur_len, max_len = 0, 0
    
    prev_tree_type_index = 0
    
    for i in range(len(trees)):
        
        if(len(tree_types) < 2):
            tree_types.append(trees[i])
            cur_len += 1
        else:
            if(trees[i] in tree_types):
                cur_len += 1
            else:
                max_len = max(cur_len, max_len)
                tree_types = [trees[i], trees[prev_tree_type_index]]
                cur_len = i - prev_tree_type_index + 1
                
        if trees[prev_tree_type_index] != trees[i]:
            prev_tree_type_index = i       
        
    return max(max_len, cur_len)

print(uniqueFruits([1,2,1,2,1,2,1,1,1,1,2,3,3,2,3,2,3,2,2,4]))
