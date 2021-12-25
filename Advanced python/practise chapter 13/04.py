# write a program to filter a list of numbers which are divisible by 5?
l = [22,15,50,44,55,35,75,65,80]
l10 = lambda l : l%5==0        #divisible formula
print(list(filter(l10,l)))