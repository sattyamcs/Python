# a = 12 
# b = 24
# print ('the sum of a and b is', a + b)

#this is called procedural oriented programming

class Number:
    def sum(self):
        return self.a + self.b

num = Number()
num.a =12
num.b =24
s = num.sum()
print(s)