'''
Created on Sep 3, 2018
@author: ishank
'''

def toLowerCase(str):


    output =""
    for c in str:
        if ord(c) < 97:
            output += chr(ord(c) + 32)
        else:
            output += c
    
    return output

print (toLowerCase("Hello"))