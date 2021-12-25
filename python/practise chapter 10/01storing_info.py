# create a class programmer for storing information of few programmers working at microsoft?

class Programmer:
    company = "microsoft"

    def __init__(self,name,product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"the name of the programmer is {self.name} and the product is {self.product}")


sattyam = Programmer("sattyam","skpe")
pawan = Programmer("pawan","github")
sattyam.getInfo()
pawan.getInfo()