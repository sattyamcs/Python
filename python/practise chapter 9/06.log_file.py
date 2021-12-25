# write a program that having file with log file and the check whether the word python is present in it or not ?

with open ('logfile.txt') as f:  
    content = f.read()

if 'python' in content:                              #this is case sensetive.
    print("yes python is present")
else:
    print("python is not present")
