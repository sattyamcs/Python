'''ques2. Write a python program to fill in a letter template given below with name and date
Letter   =    dear <name>
              you are selected!
              <date>'''


letter = ''' Dear <|name|>,
Greeting from thakur group of companies. i am happy to tell you.
You are selected!
have a great day ahead
Thank You.
<|date|>'''

name = input("enter your name\n")
date = input("enter date\n")
letter= letter.replace("<|name|>",name)
letter= letter.replace("<|date|>",date)
print(letter)
