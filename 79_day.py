class parent1:
    def func1(self):
        print("This function is in parent class.")
class parent2:
    def func2(self):
        print("This function is in parent class.")
class child(parent1,parent2):
    def func3(self):
        print("This function is in child class.")

obj=child()
obj.func3()
obj.func1()
obj.func2()