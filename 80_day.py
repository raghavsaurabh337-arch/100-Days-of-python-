class grandparent:
    def func1(self):
        print("This function is in grandparent class.")
class parent(grandparent):        
    def func2(self):
        print("This function is in parent class.")
class child(parent):
    def func3(self):
        print("This function is in child class.")
cobj=child()
cobj.func3()
cobj.func2()
cobj.func1()
                    