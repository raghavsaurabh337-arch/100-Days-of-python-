age=int(input("enter the age:"))
match age:
     case 18:
          print("The age is 18 and allow")
     case 17:
          print("The age is not 18")
     case 60:
          print("The age is 60 and over age") 
     case _:
          print("The age is not specified") 
