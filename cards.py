'''
Created on Sep 14, 2017

@author: ishan
'''

fo = open("input.txt")

line = fo.readline()
iterations = int(line)

group = 1

count = ["1","2","3"]
fill = ["E","F","S"]
color = ["G","P","R"]
shape = ["O","D","S"]

for i in range(iterations):
    
    setOfCards = fo.readline()    
    cards = setOfCards.split()
    
    card1 = cards[0]
    card2 = cards[1]
    
    card1array = list(card1)
    card2array = list(card2)
    
    outputCard = ""
    
    if card1array[0] == card2array[0]:
        outputCard = outputCard + card1array[0]
    else:
        for c in count:
            if card1array[0] != c and card2array[0] != c:
                 outputCard = outputCard + c
    
    if card1array[1] == card2array[1]:
        outputCard = outputCard + card1array[1]
    else:
        for f in fill:
            if card1array[1] != f and card2array[1] != f:
                 outputCard = outputCard + f
                
    if card1array[2] == card2array[2]:
        outputCard = outputCard + card1array[2]
    else:
        for c in color:
            if card1array[2] != c and card2array[2] != c:
                 outputCard = outputCard + c
    
    if card1array[3] == card2array[3]:
        outputCard = outputCard + card1array[3]
    else:
        for s in shape:
            if card1array[3] != s and card2array[3] != s:
                 outputCard = outputCard + s
    
    final = "Group "+str(group)+": "+outputCard
    print final
    group = group + 1
    

