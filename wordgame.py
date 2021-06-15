#Kaden Alibhai
#6/11/21
#Word Game
#We are creating a list of words
#Randomly select a word from the list for the user to guess
#give the user some turns
#show the word to the user with the characters guesses
#play the game as long as the user has turns or has guessed the word

import random
import os
import sys
import time
import datetime

gameWords= ['lebron james','kevin durant','giannis antetokounmpo','kawhi leaonard',
'nikola jokic','damian lillard','james harden','jayson tatum','luka doncic',
'anthony davis','stephen curry','joel embiid']

l1= "**************************************"
l2= "*           WordGame                 *"
l3= "*                                    *"
l4= "*         1 - Play Game              *"
l5= "*         2 - High Scores            *"
l6= "*         3 - Exit                   *"
l7="***************************************"
x=1
score=0
name=input("What is your name? ")
def menu():
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print("Please enter your selection from 1 to 3")
    inputNumber = input()
    x = int(inputNumber)
    return x

def pause():
    print("Do you want to return to the menu?")
    var=input()
    var=var.upper()
    if "Y" not in var:
        return True
    else:
        return False

def getSCORES():
    fileNAME= "Word_Game_1_HighScores.txt"
    dt=datetime.datetime.now()
    FILE= open(fileNAME, 'w')
    line= name + " had a score of " + str(score)
    FILE.write(str(dt))
    FILE.write(line)
    FILE.write("\n")
    FILE.close
    time.sleep(0.5)
    FILE= open(fileNAME, 'r')
    print(FILE.read())
    input("press enter when you no longer want to see scores")
    FILE.close()


def playGAME():
    if x==1:
        score=0
        answer=input("Do you want to guess a word? ")
        answer=answer.upper()
        while "Y" in answer:
            print("Good luck", name, "!")
            word=random.choice(gameWords)
            counter=len(word)
            print(word)
            print("The player's name contains",counter,"letters")
            turns=10  #should we consider controlling this number when they miss
            guesses=""
            while turns>0 and counter >0:
                for char in word: 
                    if char in guesses:
                        print(char,end=" ")
                    else:
                        print("_", end=" ")
                newGuess=input("\n\nGive me a letter ")
                if newGuess not in word:
                    turns -=1        #turns=turns-1
                    print("Incorrect, you have", turns, "guesses left")
                else:
                    amt=word.count(newGuess)
                    counter-=amt
                    print("Nice guess!")    
                    guesses += newGuess
            if(counter==0):
                print("You guessed the player!")
                print("The player was",word)
                score += 1
                print("Your current score is", score)
            else:
                print("You ran out of guesses, better luck next time.")
                print("The player was",word)
            answer=input("\nWould you like to play again? ").upper()
        return score


while x !=3:
    x=menu()
    if (x==1):
        convert=True
        while convert:
            score=playGAME()
            convert=pause()
    
    if (x==2):
        convert=True
        while convert:
            getSCORES()
            convert=pause()
    
    if (x==3):
        print(name, "thank you for playing")
