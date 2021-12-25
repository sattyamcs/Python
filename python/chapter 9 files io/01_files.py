# use open function to read the content of a file.
f = open('sample.txt','r') #the r is by default if you only want to read you can access normally
#  without printing r. 
data = f.read()  #reads the content
data = f.read(5)  #this is used to specify the characters to print
print(data)      #prints the content
f.close()        # close the file
