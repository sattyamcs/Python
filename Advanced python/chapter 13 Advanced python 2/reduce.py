# syntax: val = reduce(function,list)
from functools import reduce

sum = lambda a,b:a+b

l = [1,2,3,4]
val = reduce(sum,l) #this will return the sequential computation, that adds the value like 1+2,3+3,6+4
print(val)