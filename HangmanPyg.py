# Kaden Alibhai
# Create a Hangman version of the wordgame
# Useing images, lists, fonts, rendering

import pygame, math, random, sys, time, os

os.system('cls')
pygame.init()

#create our screen or window

WIDTH=800
HEIGHT=500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game!")
#Define colors
WHITE=[255,255,255]
BLACK=[0,0,0]
screen.fill(WHITE)
pygame.display.update()

#set up fonts
TitleFont = pygame.font.SysFont("comicsans", 70)
WordFont= pygame.font.SysFont("comicsane", 50)
def updateScreen(turns, displayWord):
    screen.fill
    screen.blit(images[turns], (80,100))
    pygame.display.update
    pygame.time.delay(500)
    
#Words list
gameWords= ['lebron james','kevin durant','giannis antetokounmpo','kawhi leonard',
'nikola jokic','damian lillard','james harden','jayson tatum','luka doncic',
'anthony davis','stephen curry','joel embiid']

#Load images
images= []
for i in range(7):
    image=pygame.image.load("HangmanImages\hangman"+str(i)+".png")
    images.append(image)
    screen.blit(images[i], (100,100))
    pygame.display.update()
    pygame.time.delay(500)

def updateWord(word, guesses, turns):  # function with a parameter to update word
    displayWord =" "
    screen.fill(WHITE)
    pygame.display.update
    for char in word:
        if char in guesses:
            print(char,end=' ')
            displayWord += char+" "
        else:
            displayWord += "_ "
            print('_', end =' ')
    textW=WordFont.render(displayWord,1, BLACK)
    screen.blit(textW,(350,150))
    text=TitleFont.render("HANGMAN", 1, BLACK)
    centerTitle=WIDTH/2-text.get_width()/2
    screen.blit(text,(centerTitle,20))
    screen.blit(images[turns], (80,100))
    pygame.display.update()

check= True
while check:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            check=False
    word=random.choice(gameWords)
    guesses=""
    counter=len(word)
    print(word)
    print("The player's name contains",counter,"letters")
    turns=0  #should we consider controlling this number when they miss
    displayWord= updateWord(word, guesses, turns)
    updateScreen(turns, displayWord)
    while turns<7 and counter >0:
        newGuess=input("\n\n Give me a letter ")
        if newGuess not in guesses:
            if newGuess not in word:
                turns +=1    #       turns = turns -1
                print("Wrong! You have  ", turns, "guesses left")
            else:
                counter -=word.count(newGuess) #deleten repeated letters
                print("nice guess!")
            guesses += newGuess 
        else:
            print("you used this one already")
        updateWord(word, guesses, turns)

        #end of whole loop with

pygame.quit()
sys.exit