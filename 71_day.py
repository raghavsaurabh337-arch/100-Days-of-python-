
# dir, __dict__ and help method in Python | Python Tutorial - Day #71
list=[1, 2, 3, 4, 5]
print(dir(list)) # dir method will give all the methods and attributes of the list object
print(list. __add__)
print(list.__len__)

 # __dict__ method will give all the attributes of the list object in dictionary format
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = person("Alice", 30)
print(p.__dict__)
print(help(person)) # help method will give all the methods and attributes of the person class