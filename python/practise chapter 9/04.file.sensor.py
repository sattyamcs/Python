# ques. a file contains a word 'donkey' multiple times. you need to write a program which replaces the word,
# with ## by updating the same file

with open ('file.donkey.txt',) as f:
    content = f.read()

content = content.replace("donkey","they are good peoples")
with open('file.donkey.txt','w') as f:
    content = f.write(content)