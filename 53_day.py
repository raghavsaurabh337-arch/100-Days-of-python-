# Map, Filter and Reduce in Python

def cube(x):
   return x*x*x
l=[2,3,4,8,5]

newl=list(map(cube,l))
print(newl)


# Filter

def filter_function(a):
   return a>4

newl=list(filter(filter_function,l))
print(newl)    
