# single inheritance 
# that simply owns a class that is iherited with the parent to the child class
class Employee:                                      #base class or parent class
    company = "google"

    def showDetails(self):
        print("this is a developer")

class Programmer(Employee):                          #child class or derived class
    language = "python"
    company = "youtube"

    def getlanguage(self):
        print(f"the language is {self.python}")

    def showDetails(self):
        print("this is a programmer")

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()      #this will inherit the parent class attribute if it is not found in child class.
print (e.company)    #here if it has its own then it prints its own otherwise it will print the parent class attributes