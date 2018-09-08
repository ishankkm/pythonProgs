'''
Created on May 21, 2018
@author: ishank

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack) == 0:
            self.stack.append((x, x))
        else:
            if x < self.stack[-1][1]:
                self.stack.append((x, x))
            else:
                self.stack.append((x, self.stack[-1][1]))
        
    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) > 0:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1][0]
        else:
            return None
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1][1]
        else:
            return None