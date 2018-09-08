'''
Created on May 11, 2018
@author: ishank

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
'''

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        # remember the local minima
        min_price = min(price, min_price) 
        profit = price - min_price
        max_profit = max(max_profit, profit)
        
    return max_profit

print(maxProfit([7,1,5,3,6,4]))