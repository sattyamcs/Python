# write a program to make copy of a file?

with open ('this.txt','r') as f:
    content = f.read()

with open ('copy.this.txt','w') as f:
    f.write(content)