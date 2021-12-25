# write a class calculator that is capable of finding squares, cubes and the squareroot of a number?
# and add greeting with the help of staticmethod.

class Calculator:
    def __init__(self,num):
        self.number = num

    @staticmethod
    def greet():
        print("HI, bro.\n Are you looking for problem with solutions\n Here you go.")

    def square(self):
        print(f"the value of{self.number} square is {self.number **2}")

    def cube(self):
        print(f"the value of{self.number} cube is {self.number **3}")

    def squareroot(self):
        print(f"the value of{self.number} squareroot is {self.number **0.5}")

a = Calculator(10)
a.greet()
a.square()
a.cube()
a.squareroot()
    