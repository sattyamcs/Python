'''write a programm to open three files 1.txt, 2.txt, 3.txt. if any of these files are not present,
a message without exiting the program must be printed prompting the same''' 

def readFile(filename):
    try:
        with open(filename,'r') as f:
            print(f.read())
    except FileNotFoundError:         #this exception is used where file not found 
        print(f"file not found{filename}") #used to print this filename

readFile('1.txt')
readFile('2.txt')  #file 2.txt is deleted
readFile('3.txt')
