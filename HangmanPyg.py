#Kaden Alibhai
# Create a Hanggman version of the game:  
# Use images in a list, Use Fonts, render them  

import os, sys, time, pygame, random, math

from pygame.constants import K_1  
os.system('cls')  
pygame.init()  

#Create my display screen  
WIDTH = 800  # uppercase because it behaves as constant  
HEIGHT = 500   
screen = pygame.display.set_mode((WIDTH,HEIGHT))  
pygame.display.set_caption("Hangman GAME!")   

# Define Colors  
WHITE = [255,255,255]  
BLACK = [0,0,0]  

# Word lists  
gameWords= ['lebron','kd','giannis','kawhi', 'jokic','dame','harden','tatum','luka', 'ad','steph','embiid']
# load images to list  
images = []  
for i in range(7):  
    image=pygame.image.load("HangmanImages\\hangman"+ str(i)+".png")  
    images.append(image)  
    # screen.blit(images[i], (100,100))  
    # pygame.display.update()  
    # pygame.time.delay(300)  
  
# Define Font objects  
TitleFont= pygame.font.SysFont("comicsans", 70)  #set the type of font and the size   
WordFont=pygame.font.SysFont("comicsans", 50)  
LetterFont=pygame.font.SysFont("comicsans", 40) 
 
#Define letters for rectangular buttons 
A=65 
Wbox=30 
dist=10 
letters=[]#an array of arrays  [[x,y, ltr, boolean]] 
#DEfine where to start our drawing 26 letter, 13 letter in each line 
startx= round((WIDTH - (Wbox + dist)*13) /2) #int function round 
starty= 350 
#load the letters into our double array 
for i in range(26): 
    x=startx +dist*2+((Wbox +dist)*(i%13)) 
    y=starty+((i//13)*(dist + Wbox *2)) 
    letters.append([x,y,chr(A+i), True]) 

#Function to update the screen 
def updateScreen(turns,displayWord):  
    screen.fill(WHITE)  
    title=TitleFont.render("Hangman",1, BLACK)  
    centerTitle= WIDTH/2-title.get_width()/2  
    screen.blit(title, (centerTitle,20))  
    screen.blit(images[turns], (100,100))  
    textW=WordFont.render(displayWord,1, BLACK)  
    screen.blit(textW, (300,150))  
    for letter in letters: 
        x,y,ltr, see= letter 
        if see: 
            rect=pygame.Rect(x-Wbox/2,y-Wbox/2,Wbox,Wbox) 
            pygame.draw.rect(screen, BLACK, rect, width=1)  
            text=LetterFont.render(ltr,1,BLACK) 
            screen.blit(text,(x -text.get_width()/2,y -text.get_height()/2)) 
    pygame.display.update()  
 
def updateWord(word, guesses):  # function with a parameter to update word  
    displayWord=""  
    for char in word:  
        if char in guesses:  
            displayWord += char+" "  
        else:  
            displayWord += "_ "  
    return displayWord  
 
def dis_message(message): 
    screen.fill(WHITE) 
    text =TitleFont.render(message,1,BLACK) 
    screen.blit(text, (200,200)) 
    pygame.display.update() 
    pygame.time.delay(2000)

# def cont():
#     screen.fill(WHITE)
#     msg="Would you like to play again?"
#     msg2="Press 1 to play again, press 2 to exit"
#     text1=TitleFont.render(msg,1,BLACK)
#     text2= TitleFont.render(msg2,1,BLACK)
#     screen.blit(text1, (200,100))
#     screen.blit(text2, (200,200))
#     pygame.display.update
#     keyBoardKey=pygame.key.get_pressed()
#     if keyBoardKey[pygame.K_1]:
#         updateWord
#         updateScreen
#     if keyBoardKey[pygame.K_2]:
#         pygame.quit

#always have a way to close your screen  

word=random.choice(gameWords).upper() 
print(word) 
turns= 0   #should we conider controlling this number when he/she misses      
guesses=[] 
check = True  
while check:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            check = False     
        if event.type == pygame.MOUSEBUTTONDOWN: 
            mx, my =pygame.mouse.get_pos() 
            for letter in letters: 
                x,y,ltr,see=letter 
                if see: 
                    rect=pygame.Rect(x-Wbox/2, y-Wbox/2,Wbox, Wbox) 
                    if rect.collidepoint(mx,my):  #if letter has been click 
                        letter[3]=False 
                        guesses.append(ltr) 
                        if ltr not in word: 
                            turns +=1 
    displayWord=updateWord(word, guesses)  
    updateScreen(turns, displayWord)  
    #check if we won or lost the game 
    
    won=True 
    for letter in word: 
        if letter not in guesses: 
            won=False 
            break 
    if won: 
        dis_message("You Won!!!") 
        break

    if turns == 6: 
        dis_message("You lost") 
        break

pygame.quit()  
sys.exit()  

 