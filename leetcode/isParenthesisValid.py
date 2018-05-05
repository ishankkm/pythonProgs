'''
Created on May 3, 2018
@author: ishank\

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
'''

def isParenthesesValid(s):
    
    openP = ['{', '[', '(']
    closeP = ['}', ']', ')'] 
    
    stack = []
    
    for c in s:
        if c in openP:
            stack.append(c)
        elif c in closeP:
            if c == closeP[openP.index(stack[-1])]:
                stack.pop()
            else:
                return False
        else:
            return False
    
    return True if len(stack) == 0 else False

print(isParenthesesValid("()[]{}{"))