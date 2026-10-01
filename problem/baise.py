def table(number):
    for i in range(1,11):
        print(f"{number} x {i} = {number*i}")


def fact(n):
    if n==0 or n==1:
        table(n)
        return 1
    else:
       return n * fact(n-1)
           
# obj=fact(5)
# print(obj)
# print(fact(3))


# // same number of square and cube of a number

class math:
    def squares_and_cubes(self, number):
        # self.number=number
        print(f"{number}^2 = {number**2}, {number}^3 = {number**3}")
        return fact(number)
# obj=math()
# obj1=int(input("Enter a number: "))
# print((obj.squares_and_cubes(obj1)))    
    
def add(a,b):
    return a+b
    str ="saurabh"
    str1="raghav"
    # for i in range(len(str)):
    #     print(str[i])   
    # print(len(str))
    print(type(str + str1))
# def str():
name = "saurabh"
list=list(name)
print(list[:-2])
print(list[:2])
print(type(list))

# class login():
#     name="saurabh"
#     email="raghav"
#     def auth(self):
#         if self.name=="saurabh" and self.email=="raghav":
#             print("login successful")
             
#         else:
#             print("login failed")
            
# login1=login()
# login1.auth()   


# class loginSystem():
    # def login():
    #     pass
    # def logout():
    #     pass
    # def register():
    #     pass
    # def website():
    #     pass
    # def cart():
    #     pass

# website=True






            
            
    




