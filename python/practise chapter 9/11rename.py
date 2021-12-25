# write a pyhton program to rename a file to "removed by python.txt"?
import os
file = "this.txt"
renamed = "removed by python.txt"

with open (file) as f:
    content =f.read()

with open(renamed,'w')as f:
    f.write(content)

os.remove(file)
