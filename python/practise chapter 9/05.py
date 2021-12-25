# ques. repeat program 4 for a list of such words to be censored?


words = ["donkey","kaala","chutua","mote"]
with open ('file.donkey.txt',) as f:
    content = f.read()

for word in words:
    content = content.replace(word,"they are good peoples")
with open('file.donkey.txt','w') as f:
    content = f.write(content)