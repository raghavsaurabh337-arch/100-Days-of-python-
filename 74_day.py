 # Method Overriding in Python 
class employee:
    def show(self, x , y  ):
        print("this is employee")
        return x+y
class programer(employee):
    def show(self, x, y):
        print("this is programer")
        return x+y  
c=employee()
print(c.show(5, 10))
c=programer()
print(c.show(5, 10))