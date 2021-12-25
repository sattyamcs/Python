# write a program to wipe out the content of a file using python?

filename = "this.txt"
with open('this.txt','w')as f:
    f.write("")       
    
#this will empty or wioe the file using "".