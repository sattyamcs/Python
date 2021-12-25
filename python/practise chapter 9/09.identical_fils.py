# ques.write a program to find out whether a file is identical and matches the content of another file?

file1 = "this.txt"
file2 = "copy.this.txt"

with open (file1,'r') as f:
    f1 = f.read()
with open (file2,'r') as f:
    f2 = f.read()

f1==f2
print("yes files are identical")
