# write a program to find the maximum  number in a list using the reduce function.?

from functools import reduce
l = [3,4,53,2,6]
sum= lambda a,b:a+b      #lambda function

a = reduce(sum,l)     #returns the largest value
print(a)

# here sum function return the sum that is defined by lambda