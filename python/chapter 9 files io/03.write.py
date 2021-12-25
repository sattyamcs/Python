f = open('another.txt','w')               #this w is used to write the file
f.write('please write this to the file, i am appending')
f.close()

f = open('another.txt','a')               #this a is used to add the content to the file
f.write( 'i am appending. my name is sattyam chauhan')
f.close()


