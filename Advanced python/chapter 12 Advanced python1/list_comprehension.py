a = [3,4,5,6,7,8,9,22,33,44,55,66]
b = []
# for item in a:          #this is used to write the items that we want
#     if item%2==0:       #for even numbers
#         b.append(item)

# print(b)


b = [i for i in a if i%2==0]  #this is list comprehension that is used same as the upper code
print(b)