'''
Created on Jun 1, 2018
@author: ishank
'''

class Singleton(object): 

    _singleton_object = None    
    
    def __init__(self, **kwargs):        
        self.props = [1,2,3] # Update the attribute dictionary by inserting a new key-value pair 

    @staticmethod
    def getInstance():
        if Singleton._singleton_object == None:
            Singleton._singleton_object = Singleton()
        return Singleton._singleton_object
        


obj = Singleton.getInstance()
obj.props.append(10)
print(obj.props)

obj = Singleton.getInstance()
obj.props.append(12)
print(obj.props)