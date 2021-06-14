#Kaden Alibhai
#6/11/21
#Word Game
#We are creating a list of words
#Randomly select a word from the list for the user to guess
#give the user some turns
#show the word to the user with the characters guesses
#play the game as long as the user has turns or has guessed the word

import random

gameWords= ['lebron james','kevin durant','giannis antetokounmpo','kawhi leaonard',
'nikola jokic','damian lillard','james harden','jayson tatum','luka doncic',
'anthony davis','stephen curry','joel embiid']

answer=input("Do you want to guess a word? ")
name=input("What is your name? ")
answer=answer.upper()
while "Y" in answer:
    print("Good luck", name, "!")
    word=random.choice(gameWords)
    counter=len(word)
    print("The player's name contains",counter,"letters")
    turns=10  #should we consider controlling this number when they miss
    guesses=""
    for char in word: 
        if char in guesses:
            print(char,end=" ")
        else:
            print("_", end=" ")
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
    else:
        print("You ran out of guesses, better luck next time.")
        print("The player was",word)
    answer=input("\nWould you like to play again? ").upper()

print(name,"thank you for playing")
