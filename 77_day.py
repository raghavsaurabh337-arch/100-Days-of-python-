#  Operator Overloading in Python 
class vector:
    def __init__(self, i , j , k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self, other):
        return vector(self.i + other.i, self.j + other.j, self.k + other.k)

v1=vector(1, 2, 3)
print(v1)
v2=vector(4, 5, 6)    
print(v2)
print(v1+v2)
print(type(v1+v2))