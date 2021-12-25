# ques. write a program to find out the line number present in which python is present as from the logfile.txt?
content = True
i = 1
with open ('logfile.txt') as f:
    while content:
        content = f.readline()
        if 'python' in content:
            print(content)
            print(f"yes,python is  present in line number {i}")
            i+=1
    
