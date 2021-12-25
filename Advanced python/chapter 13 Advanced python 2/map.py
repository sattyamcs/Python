def square(num):
    return num*num

l = [1,2,3,4]

#method 1 
l2 =[]
for items in l:
    l2.append(square(items))
print(l2)

#method 2
print (list(map(square,l)))   #this is map method
# having syntax: map(function,input_lists)