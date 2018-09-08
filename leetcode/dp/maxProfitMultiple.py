'''
Created on May 11, 2018
@author: ishank

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Input: [7,1,5,3,6,4]
Output: 7
'''

def maxProfit(prices):
    
    min_price = float('inf')
    max_profit = 0
    prev = float('inf')
    total_profit = 0
    
    for price in prices:
        
        if (price - prev) < 0:
            min_price = float('inf')
            total_profit += max_profit
            max_profit = 0
        
        min_price = min(price, min_price)
        profit = price - min_price
        max_profit = max(profit, max_profit)
        
        prev = price
        
    total_profit += max_profit
    
    return total_profit

print(maxProfit([7,1,5,3,6,4]))
