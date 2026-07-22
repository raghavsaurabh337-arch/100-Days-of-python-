'''Write a C program to input length and width of a rectangle and calculate perimeter of the rectangle. How to find perimeter of a rectangle in C programming. Logic to find the perimeter of a rectangle if length and width are given in C programming.
'''
def cal_para(length,width):
    print(2 * (length + width))

def cal_area(length,width):
    print(length * width)

def multi(number):
    for  i in range(1,11):
        print(number,"*",i,"=",number*i)

def marks_greater(marks):
     if marks > 80:
        print("A++")
     elif(marks>70):
            print("A+")
     elif marks > 60:
        print("A")
     elif(marks>50):
            print("second")
     elif marks > 40:
        print("pass third")
     elif(marks>33):
            print("only")
     else:
          print("fail")

def pattren(num):
     for i in range(1,num+1):
          for j in range(i):          
               print("*",end="  ")
          print()          
# cal_para(5, 10)
# cal_area(5, 10)
# multi(3)
# marks_greater(25)
pattren(5)