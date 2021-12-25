# multilevel inheritance occurs when child class inhertit from more than one parent class

class Person:                        #class1 parent class
    country = "INDIA"

    def takeBreathe(self):
        print("i am breathing")

class Employee:                      #class2 parent class
    company = "Honda"

    def getSalary(self):
        print(f"salary is {self.salary}")

    def takeBreathe(self):
        print("i am luckly breathing")

class Programmer(Employee):          #class3 child class
    company = "fiber"

def getSalary(self):
    print(f"no salary to programmer because you are on learning mode")

p = Person()
# print(p.company)      #person object has no attribute like company
e = Employee()
print(e.company)
pr = Programmer()
p.takeBreathe()
e.takeBreathe()
pr.takeBreathe()     #this inherits attributes from clss employee, they can access the nearest parents.
