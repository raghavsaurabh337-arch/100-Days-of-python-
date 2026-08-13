#constructors
class person:
     # name="saurabh"
     # work="Developer"
     def __init__(self,name,work):
          self.name=name
          self.work=work
          print("Hey ")
     def info(self):
          print(f"{self.name} is a {self.work}")
a=person("saurabh","AI") 
b=person("sandeep","Aix") 
a.info() 
b.info()

    