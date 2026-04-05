'''The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hi-
score whenever the game() function breaks the Hi-score.'''

'''f = open("Hi-Score.txt")
lines = f.readline()
while(lines!= ""):
    print(lines)
    lines = f.readline()'''

'''st = "Hey Yashpal you are amazing"
f = open("Hi.txt", "a")
f.write(st)
f.close'''

'''with open("Hi.txt") as f:

    print(f.read())'''

'''import random 

def game():
    print("You are playing a game..")
    score = random.randint(1, 62)
    with open("Hi-Score.txt") as f:
        highscore = f.read
        if(highscore!= ""):
         highscore = int(highscore)
        else:
            highscore = 0
    print(f"Your score: {score}")
    if(score > highscore): 
        with open("Hi-Score.txt", "w") as f:
            f.write(str(score))
    
    return score 

game()'''


import random

def game(): 
    print("You are playing the game..")
    score = random.randint(1, 62)
    # Fetch the hiscore
    with open("Hi-Score.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score: {score}")
    if(score>hiscore):
        # write this hiscore to the file
        with open("Hi-Score.txt", "w") as f:
            f.write(str(score))

    return score

game()