class math:
    def __init__(self,num):
        self.num=num
    def addtonum(self,n):
        return self.num+n
    @staticmethod
    def add(a,b,c):
        return a+b+c
obj=math(3)
print(obj.num)  
print(obj.addtonum(5))   
    