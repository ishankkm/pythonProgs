'''
Created on Sep 7, 2018
@author: ishank
'''


prices = [0,1,5,8,9,10,17,17,20]

def rod_cutting(n):
    
    optimal_cut = [0]*(n+1)
    
    for i in range(n+1):
        max_price = 0
        for j in range(i+1):
            max_price = max(max_price, prices[j]+optimal_cut[i-j])
            
        optimal_cut[i] = max_price
        
    print(optimal_cut)
    

    
print(rod_cutting(8))
