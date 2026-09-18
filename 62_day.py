# Access Modifiers in Python | Python Tutorial - Day #62
 # public, private, protected

#public: can be accessed from anywhere
class emo:
    def __init__(self):
        self.name="saurabh"

a=emo()
print(a.name)    


# private: can be accessed only within the class
class emo:
    def __init__(self):
        self.__name="saurabh raghav  "

a=emo()
# print(a.__name)  # This will raise an AttributeError
print(a._emo__name)  # This will print "saurabh"  
print(a.__dir__()) 