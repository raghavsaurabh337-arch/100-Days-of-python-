#  Hybrid and Hierarchical Inheritance in Python

#Hybrid inheritance is a combination of two or more types of inheritance. It allows a class to inherit from multiple classes, which can be a combination of single, multiple, and hierarchical inheritance.
class baiseclass:
    pass
class derivedclass1(baiseclass):
    pass
class derivedclass2(baiseclass):    
    pass
class derivedclass3(derivedclass1, derivedclass2):
    pass



# hierarchical inheritance is a type of inheritance where multiple classes inherit from a single base class. It allows for the creation of a hierarchy of classes, where each derived class can have its own unique attributes and methods, while still inheriting the properties of the base class.
class baseclass:
    pass
class derivedclass4(baseclass):
    pass
class derivedclass5(baseclass):
    pass