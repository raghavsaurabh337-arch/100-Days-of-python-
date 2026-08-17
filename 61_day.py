#Inheritance in Python 
class employee:
     def __init__(self, id,name):
         self.id = id
         self.name = name  
     def show(self):
         print(f"The name of Employee: {self.id} is {self.name}")     


class programer(employee):
    def sho():

        print("this is employee")         


e=employee(232,"saurabh")     
e.show()           
e1=programer(234,"raghav")
e1.sho()