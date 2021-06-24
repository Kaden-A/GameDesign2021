import os, sys, time, pygame, random, math
import button
from pygame.constants import K_1  
os.system('cls')  
pygame.init() 
 

#button module from https://github.com/russs123/pygame_tutorials/tree/main/Button
# I added my own images and actions for the buttons

#create display window
HEIGHT = 800
WIDTH = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
WHITE= [255,255,255]
BLACK= [0,0,0]
CYAN=[0,255,255]
RED=[255,0,0]
GREEN=[50,25,255]
BLUE=[0,0,255]
PURPLE=[200,0,190]
bg=pygame.image.load("FinalProject\FinalProjectImages\BG.jpg")

def QUIT():
	pygame.quit()

def playGAME(): 
	pygame.display.set_caption("Flappy Bird")

#load button images
start_img = pygame.image.load('FinalProject\FinalProjectImages\Start.png').convert_alpha()
exit_img = pygame.image.load('FinalProject\FinalProjectImages\Quit.png').convert_alpha()
scores_img = pygame.image.load('FinalProject\FinalProjectImages\HighSCORES.png').convert_alpha()

#create button instances
start_button = button.Button(200, 75, start_img, 0.8)
exit_button = button.Button(275, 350, exit_img,0.8)
scores_button= button.Button(175,575, scores_img,0.8)

#game loop
run = True
while run:
	screen.blit(bg,(0,0))

	if start_button.draw(screen):
		screen.fill(CYAN)
		pygame.display.flip()
		pygame.time.delay(300)
		level1_img= pygame.image.load("FinalProject\FinalProjectImages\Level1.png").convert_alpha()
		level1_button= button.Button(200,75, level1_img, 0.8)

		
	if exit_button.draw(screen):
		QUIT()
	if scores_button.draw(screen):
		print("")
    #     # printSCORES()
    #     # updateSCORES()

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()