list1 = ["sattyam", 11,False,11.2]

# index = 0
# for item in list1:        #this is also a method to print list with index number
#     print(item,index)
#     index += 1

for index,item in enumerate(list1):   #this function prints the index with items of a list.
    print(index,item)