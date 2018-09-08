'''
Created on Jun 1, 2018
@author: ishank

An object-oriented way of providing global variables is Singleton. 
Singleton is the pattern you need when you'd like to allow only one object to be instantiated from a class. 
Why would you need such a pattern? 
Let's say that there is a need for keeping a cache of information to be shared by various elements of your software system. 
By keeping this information in the single object, there's no need to retrieve the information from its original source every time.

So in this case, Singleton acts as a cache of the information. 
Modules in Python act as Singletons. 
There are also a number of ways of implementing Singleton, but we'll be using the Borg design pattern to implement our Singleton.
'''

class Borg:
    """Borg pattern making the class attributes global"""
    _shared_data = {} # Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data # Make it an attribute dictionary

        
class Borg_Singleton(Borg): #Inherits from the Borg class
    """This class now shares all its attributes among its various instances"""
    #This essenstially makes the singleton objects an object-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs) # Update the attribute dictionary by inserting a new key-value pair 

    def __str__(self):
        return str(self._shared_data) # Returns the attribute dictionary for printing

x = Borg_Singleton(HTTP="Hyper Text Transfer Protocol")
print(x) 

y = Borg_Singleton(SNMP="Simple Network Management Protocol")
print(Borg._shared_data)

b = Borg()
b._shared_data.update(HTTP="Hyper Text Transfer Protocol 2")
print(b._shared_data)
print(x)

'''
Traditional Singleton
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


