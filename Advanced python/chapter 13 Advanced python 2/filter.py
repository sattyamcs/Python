# syantax of filter : list(filter(function,list))
def greater_than_5(num):
    if num>5:
        return True
    else:
        return False

l = [1,2,22,33,44,55]
g10 = lambda l:l>10
print(list(filter(greater_than_5,l))) #so this method prints the value that is greater than 5 as we defined in function
print(list(filter(g10,l))) #wecan use lambda function also to filter