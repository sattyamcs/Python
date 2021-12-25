b = set()                            #empty set

b.add(4)                             #this is used to add values to set
b.add(2)
b.add(4)                              #repetative value could not be counted
b.add(1)
b.add((4,5,6))                        #tuple can be added
# b.add([2,3,4,5])                       #cannot add list
# b.add({4:5})                           #cannot add  dictionary to sets
print(b)

print(len(b))                             #prints the length of the set

#Removal of an item 
b.remove((4,5,6))                           # removes the value from the set b
# b.remove(54)                             #throws an error because 54 is not available to set
print(b)

print(b.pop())
print(b)

b.clear()                                # it clears the set
print(b)

b = {1,2,3,4,56,7,8,7}
print(b)