
# Magic/Dunder Methods in Python

class person:
    name = "saurabh"
    def __len__(self):
        for i in self.name:
            return len(self.name)
e=person()
print(e.name)
print(len(e)) 