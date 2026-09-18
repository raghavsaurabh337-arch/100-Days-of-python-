
# Class Methods as Alternative Constructors in Python | Python Tutorial - Day #70
class emp:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def fromstr(self, string):
        name, age = string.split("-") # alternative constructor to create object from string    
        return emp(name, int(age))  

e1 = emp("John", 25)
print(e1.name) 
print(e1.age)  

string="John-25"
e2 = e1.fromstr(string) #fromstr is called using e1 object but it returns a new object e2
print(e2.name) 
print(e2.age)