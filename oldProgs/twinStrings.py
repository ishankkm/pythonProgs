'''
Created on Mar 25, 2018
@author: ishank
'''

def twins(a, b):
    
    results = []
    for i in range(len(a)):
        
        a_list, b_list = list(a[i]), list(b[i])
        
        if len(a_list) == len(b_list):
            a_set_odd, a_set_even = set(a_list[1::2]), set(a_list[0::2])
            b_set_odd, b_set_even = set(b_list[1::2]), set(b_list[0::2])
            
            if a_set_odd == b_set_odd and a_set_even == b_set_even:
                results.append('Yes')
            else:
                results.append('No')
    return results

print(twins(['cdab', 'dcba', 'abcd'], ['abcd', 'abcd', '']))
