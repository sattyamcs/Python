def func (a):
    return a+5

print (func(10))

func = lambda a: a+5 #this we used lambda function this is as same as the upper function
sum = lambda a,b: a+b
square = lambda a: a*a

a=5
print(func(a))
print(sum(a,5))
print(square(a))