# the game() function in a program list , let a user play a game and returns the score as an integer.
# you need to read a file 'hiscore.txt' which is either blank or contains the previous hi score
# you need to write a program to update the hiscore whenever game breaks the hiscore.

def game ():
    return 64333

score = game()
with open ('hiscore.txt') as f:
    hiscore = f.read()

if hiscore == '':
    with open ('hiscore.txt', 'w') as f:
        f.write(str(score))
        
elif int (hiscore)< score:
    with open ('hiscore.txt', 'w') as f:
        f.write(str(score))

#this program will update the value to the hiscore.txt file


