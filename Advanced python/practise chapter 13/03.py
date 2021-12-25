'''a list contains the multiplication of 7. write a program to convert it to a vertical string of same number {7,14...}'''

l = [str(i*7) for i in range(1,11)]
print(l)
table = "\n".join(l)    #it always works with strings
print(table)
