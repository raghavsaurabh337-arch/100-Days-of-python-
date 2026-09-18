
# Class Methods in Python | Python Tutorial - Day #69
class emp:
    company = "Google"
    def show(self):
        print(f"Employee name is: {self.name} and company is: {self.company}")
    @classmethod
    def companychange(cls, newcompany):
        cls.company = newcompany

a=emp()
a.name="saurabh"
a.show()

a2=emp()
a2.name="John"
emp.companychange("Microsoft")
a2.show()
print(emp.company)