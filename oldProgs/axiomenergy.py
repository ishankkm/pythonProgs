'''
Created on Apr 16, 2018
@author: ishank mishra
'''


# Question 1: Write three functions that compute the sum of the numbers in a given list  
#             using a for-loop, a while-loop, and recursion.

def computeSum(numbers, method='for_loop'):
    
    if len(numbers) == 0: return 0
    
    sum_numbers = 0
    
    if method == 'for_loop':        
        for number in numbers:
            sum_numbers += number
        return sum_numbers
    elif method == 'while':
        n = 0
        while n < len(numbers):
            sum_numbers += numbers[n]
            n += 1
        return sum_numbers
    elif method == 'recursion':
        if len(numbers) == 1:
            return numbers[0]
        else:
            return numbers[-1] + computeSum(numbers[:-1], 'recursion')
    else:
        raise Exception("Invalid Method")
    
# print(computeSum([1,2,3,4,5,6]))
    
# Question 2: Write a function that combines two lists by alternatingly taking elements.
# For example: given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3].
def combineLists(listA, listB):
    
    len_listA, len_listB = len(listA), len(listB)
    
    if len_listA == 0 and len_listB == 0: return None
    
    minLength = min(len_listA, len_listB)
    
    combined = []
    for i in range(minLength):
        combined.append(listA[i])
        combined.append(listB[i])
   
    if len_listA > len_listB: 
        return combined.append(listA[minLength:])
    elif len_listB > len_listA: 
        return combined.append(listB[minLength:])
    else:
        return combined

#print(combineLists([1,2,3], ['a','b','c']))

# Question 3: Write a function that computes the list of the first 100 Fibonacci numbers. 
#             By definition, the first two numbers in the Fibonacci sequence are 0 and 1, 
#             and each subsequent number is the sum of the previous two. 
#             As an example, here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.
def fibonnaciList(size=100):
    
    if size == 1: return [0]
    elif size < 1: return None
    
    fibList = [0, 1]
    
    for _ in range(size-2):
        fibList.append(fibList[-1] + fibList[-2])
        
    return fibList

#print(fibonnaciList())


























    

