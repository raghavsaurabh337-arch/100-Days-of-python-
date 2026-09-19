#  super keyword in Python 
class Parent:
    def parent_method(self):
        
        print("This is parent method")

       
class Child(Parent):
    def parent_method(self):
        print("This is child method")
        super().parent_method()
   
    def child_method(self):
        print("This is child method")
        super().parent_method()

# p=Parent("Alice",30)   
p=Child()    
p.child_method()
p.parent_method()



class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class manager(employee):

        def __init__(self,name,age,department):
            super().__init__(name,age)
            self.department=department
            print("Name:",self.name)
            print("Age:",self.age)
            print("Department:",self.department)
saurab=manager("saurabh",30,"IT")            