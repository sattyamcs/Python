# store the multiplication table in ques 3 in a file name table.txt?


num = int(input("Enter your number"))
table = [num*i for i in range(1,11)]    #this is used for creating table
print(table)
with open('table.txt','a') as f:        #here we use append to print table to table.txt
    f.write(str(table))                 #txt file always accept str values
    f.write('\n')                     