'''
Created on Jun 2, 2018
@author: ishank
'''

def findAllDivisors(n):
    
    divList1 = []
    divList2 = []
    
    for i in range(1, int(n**0.5)):
        
        if n % i == 0:
            if (n / i) == i:
                divList1.append(i)
            else:
                divList1.append(i)
                divList2.append(n/i)
    
    return divList1 + divList2[::-1]

for i in range(1, 101):
    print(i, ": ", len(findAllDivisors(i)))
