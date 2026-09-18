
# Instance variables vs Class variables in Python | Python Tutorial - Day #66

class Employee:
    company = "APPly"  # Class variable
    def __init__(self, name):
        self.name = name  # Instance variable
        self.salary = 2324.90  # Instance variable
    def show(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {self.company}")

emp=Employee("John Doe")
print(emp.name)  # Accessing instance variable
emp.company="Google"  # Modifying class variable
emp.salary = 30345.00  # Modifying instance variable
emp.show()  # Calling the show method

emp2=Employee("Jane Smith")
print(emp2.name)  # Accessing instance variable         
emp2.show()  # Calling the show method
