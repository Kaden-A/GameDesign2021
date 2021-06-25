#Kaden Alibhai
#Final project
#6/22/21
#I am making a Flappy Bird game with 3 levels, a highscores feature, a restart button, and exit button
from io import UnsupportedOperation
import os, sys, time, pygame, random, math,datetime
import button
from pygame.constants import K_1  
os.system('cls')  
pygame.init() 
dt=datetime.datetime.now()
file= "FinalProject\Flappy_Bird_HighScores.txt"
score=0
name=input("What is your name? ")
#button module from https://github.com/russs123/pygame_tutorials/tree/main/Button
# I added my own images and actions for the buttons
#game mechanics from https://github.com/russs123/flappy_bird/blob/main/flappy.py
# I used my own images and sprotes, created my own functions, added levels, and added a highscores option using files


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
bg=pygame.image.load("FinalProject\FinalProjectImages\MenuBG.jpg")

def printSCORES():
    FileRead=open(file,'r')
    print(FileRead.read())
    FileRead.close

def updateSCORES(score):
    FileWrite=open(file,'a')
    line=name+"\t"+"SCORED"+"\t"+str(score)+"\t"+"POINTS"+"\t"+str(dt.strftime("%A"))+" "+str(dt.month)+"/"+str(dt.day)+ "/"+ str(dt.year)
    FileWrite.write("\n"+line)
    FileWrite.close

def QUIT():
	pygame.quit()

def Level1UNDERWATER():
	clock = pygame.time.Clock()
	fps = 60
	font = pygame.font.SysFont('Bauhaus 93', 60)
	ground_scroll = 0
	scroll_speed = 4
	flying = False
	game_over = False
	pipe_gap = 150
	pipe_frequency = 1500 #milliseconds
	last_pipe = pygame.time.get_ticks() - pipe_frequency
	score = 0
	pass_pipe = False


	#load images
	bg = pygame.image.load('img/bg2.jpg')
	ground_img = pygame.image.load('img/ground.png')
	button_img = pygame.image.load('img/restart.png')


	#function for outputting text onto the screen
	def draw_text(text, font, text_col, x, y):
		img = font.render(text, True, text_col)
		screen.blit(img, (x, y))

	def reset_game():
		pipe_group.empty()
		flappy.rect.x = 100
		flappy.rect.y = int(HEIGHT / 2)
		score = 0
		return score


	class Bird(pygame.sprite.Sprite):

		def __init__(self, x, y):
			pygame.sprite.Sprite.__init__(self)
			self.images = []
			self.index = 0
			self.counter = 0
			for num in range (1, 4):
				img = pygame.image.load(f"img/bird{num}.png")
				self.images.append(img)
			self.image = self.images[self.index]
			self.rect = self.image.get_rect()
			self.rect.center = [x, y]
			self.vel = 0
			self.clicked = False

		def update(self):

			if flying == True:
				#apply gravity
				self.vel += 0.5
				if self.vel > 8:
					self.vel = 8
				if self.rect.bottom < 768:
					self.rect.y += int(self.vel)

			if game_over == False:
				#jump
				if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
					self.clicked = True
					self.vel = -10
				if pygame.mouse.get_pressed()[0] == 0:
					self.clicked = False

				#handle the animation
				flap_cooldown = 5
				self.counter += 1
				
				if self.counter > flap_cooldown:
					self.counter = 0
					self.index += 1
					if self.index >= len(self.images):
						self.index = 0
					self.image = self.images[self.index]


				#rotate the bird
				self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
			else:
				#point the bird at the ground
				self.image = pygame.transform.rotate(self.images[self.index], -90)



	class Pipe(pygame.sprite.Sprite):

		def __init__(self, x, y, position):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.image.load("img/pipe2.png")
			self.rect = self.image.get_rect()
			#position variable determines if the pipe is coming from the bottom or top
			#position 1 is from the top, -1 is from the bottom
			if position == 1:
				self.image = pygame.transform.flip(self.image, False, True)
				self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
			elif position == -1:
				self.rect.topleft = [x, y + int(pipe_gap / 2)]


		def update(self):
			self.rect.x -= scroll_speed
			if self.rect.right < 0:
				self.kill()



	class Button():
		def __init__(self, x, y, image):
			self.image = image
			self.rect = self.image.get_rect()
			self.rect.topleft = (x, y)

		def draw(self):
			action = False

			#get mouse position
			pos = pygame.mouse.get_pos()

			#check mouseover and clicked conditions
			if self.rect.collidepoint(pos):
				if pygame.mouse.get_pressed()[0] == 1:
					action = True

			#draw button
			screen.blit(self.image, (self.rect.x, self.rect.y))

			return action



	pipe_group = pygame.sprite.Group()
	bird_group = pygame.sprite.Group()

	flappy = Bird(100, int(HEIGHT / 2))

	bird_group.add(flappy)

	#create restart button instance
	button = Button(WIDTH // 2 - 50, HEIGHT // 2 - 100, button_img)


	run = True
	while run:

		clock.tick(fps)

		#draw background
		screen.blit(bg, (0,0))

		pipe_group.draw(screen)
		bird_group.draw(screen)
		bird_group.update()

		#draw and scroll the ground
		screen.blit(ground_img, (ground_scroll, 768))

		#check the score
		if len(pipe_group) > 0:
			if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
				and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
				and pass_pipe == False:
				pass_pipe = True
			if pass_pipe == True:
				if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
					score += 1
					pass_pipe = False
		draw_text(str(score), font, WHITE, int(WIDTH / 2), 20)


		#look for collision
		if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
			game_over = True
		#once the bird has hit the ground it's game over and no longer flying
		if flappy.rect.bottom >= 768:
			game_over = True
			flying = False


		if flying == True and game_over == False:
			#generate new pipes
			time_now = pygame.time.get_ticks()
			if time_now - last_pipe > pipe_frequency:
				pipe_height = random.randint(-100, 100)
				btm_pipe = Pipe(WIDTH, int(HEIGHT / 2) + pipe_height, -1)
				top_pipe = Pipe(WIDTH, int(HEIGHT / 2) + pipe_height, 1)
				pipe_group.add(btm_pipe)
				pipe_group.add(top_pipe)
				last_pipe = time_now

			pipe_group.update()

			ground_scroll -= scroll_speed
			if abs(ground_scroll) > 35:
				ground_scroll = 0

		#check for game over and reset
		if game_over == True:
			if button.draw():
				game_over = False
				updateSCORES(score)
				score = reset_game()


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
				flying = True

		pygame.display.update()

def Level2NIGHTMODE(): 
	clock = pygame.time.Clock()
	fps = 60
	font = pygame.font.SysFont('Bauhaus 93', 60)
	ground_scroll = 0
	scroll_speed = 4
	flying = False
	game_over = False
	pipe_gap = 150
	pipe_frequency = 1500 #milliseconds
	last_pipe = pygame.time.get_ticks() - pipe_frequency
	score = 0
	pass_pipe = False


	#load images
	bg = pygame.image.load('img/bg.png')
	ground_img = pygame.image.load('img/ground.png')
	button_img = pygame.image.load('img/restart.png')


	#function for outputting text onto the screen
	def draw_text(text, font, text_col, x, y):
		img = font.render(text, True, text_col)
		screen.blit(img, (x, y))

	def reset_game():
		pipe_group.empty()
		flappy.rect.x = 100
		flappy.rect.y = int(HEIGHT / 2)
		score = 0
		return score


	class Bird(pygame.sprite.Sprite):

		def __init__(self, x, y):
			pygame.sprite.Sprite.__init__(self)
			self.images = []
			self.index = 0
			self.counter = 0
			for num in range (1, 4):
				img = pygame.image.load(f"img/bird{num}.png")
				self.images.append(img)
			self.image = self.images[self.index]
			self.rect = self.image.get_rect()
			self.rect.center = [x, y]
			self.vel = 0
			self.clicked = False

		def update(self):

			if flying == True:
				#apply gravity
				self.vel += 0.5
				if self.vel > 8:
					self.vel = 8
				if self.rect.bottom < 768:
					self.rect.y += int(self.vel)

			if game_over == False:
				#jump
				if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
					self.clicked = True
					self.vel = -10
				if pygame.mouse.get_pressed()[0] == 0:
					self.clicked = False

				#handle the animation
				flap_cooldown = 5
				self.counter += 1
				
				if self.counter > flap_cooldown:
					self.counter = 0
					self.index += 1
					if self.index >= len(self.images):
						self.index = 0
					self.image = self.images[self.index]


				#rotate the bird
				self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
			else:
				#point the bird at the ground
				self.image = pygame.transform.rotate(self.images[self.index], -90)



	class Pipe(pygame.sprite.Sprite):

		def __init__(self, x, y, position):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.image.load("img/pipe.png")
			self.rect = self.image.get_rect()
			#position variable determines if the pipe is coming from the bottom or top
			#position 1 is from the top, -1 is from the bottom
			if position == 1:
				self.image = pygame.transform.flip(self.image, False, True)
				self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
			elif position == -1:
				self.rect.topleft = [x, y + int(pipe_gap / 2)]


		def update(self):
			self.rect.x -= scroll_speed
			if self.rect.right < 0:
				self.kill()



	class Button():
		def __init__(self, x, y, image):
			self.image = image
			self.rect = self.image.get_rect()
			self.rect.topleft = (x, y)

		def draw(self):
			action = False

			#get mouse position
			pos = pygame.mouse.get_pos()

			#check mouseover and clicked conditions
			if self.rect.collidepoint(pos):
				if pygame.mouse.get_pressed()[0] == 1:
					action = True

			#draw button
			screen.blit(self.image, (self.rect.x, self.rect.y))

			return action



	pipe_group = pygame.sprite.Group()
	bird_group = pygame.sprite.Group()

	flappy = Bird(100, int(HEIGHT / 2))

	bird_group.add(flappy)

	#create restart button instance
	button = Button(WIDTH // 2 - 50, HEIGHT // 2 - 100, button_img)


	run = True
	while run:

		clock.tick(fps)

		#draw background
		screen.blit(bg, (0,0))

		pipe_group.draw(screen)
		bird_group.draw(screen)
		bird_group.update()

		#draw and scroll the ground
		screen.blit(ground_img, (ground_scroll, 768))

		#check the score
		if len(pipe_group) > 0:
			if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
				and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
				and pass_pipe == False:
				pass_pipe = True
			if pass_pipe == True:
				if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
					score += 1
					pass_pipe = False
		draw_text(str(score), font, WHITE, int(WIDTH / 2), 20)


		#look for collision
		if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
			game_over = True
		#once the bird has hit the ground it's game over and no longer flying
		if flappy.rect.bottom >= 768:
			game_over = True
			flying = False


		if flying == True and game_over == False:
			#generate new pipes
			time_now = pygame.time.get_ticks()
			if time_now - last_pipe > pipe_frequency:
				pipe_height = random.randint(-100, 100)
				btm_pipe = Pipe(WIDTH, int(HEIGHT / 2) + pipe_height, -1)
				top_pipe = Pipe(WIDTH, int(HEIGHT / 2) + pipe_height, 1)
				pipe_group.add(btm_pipe)
				pipe_group.add(top_pipe)
				last_pipe = time_now

			pipe_group.update()

			ground_scroll -= scroll_speed
			if abs(ground_scroll) > 35:
				ground_scroll = 0

		#check for game over and reset
		if game_over == True:
			if button.draw():
				game_over = False
				score = reset_game()


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
				flying = True

		pygame.display.update()

def Level3HARD():
	clock = pygame.time.Clock()
	fps = 60
	font = pygame.font.SysFont('Bauhaus 93', 60)
	ground_scroll = 0
	scroll_speed = 4
	flying = False
	game_over = False
	pipe_gap = 125
	pipe_frequency = 1500 #milliseconds
	last_pipe = pygame.time.get_ticks() - pipe_frequency
	score = 0
	pass_pipe = False


	#load images
	bg = pygame.image.load('img/bg1.png')
	ground_img = pygame.image.load('img/ground.png')
	button_img = pygame.image.load('img/restart.png')


	#function for outputting text onto the screen
	def draw_text(text, font, text_col, x, y):
		img = font.render(text, True, text_col)
		screen.blit(img, (x, y))

	def reset_game():
		pipe_group.empty()
		flappy.rect.x = 100
		flappy.rect.y = int(HEIGHT / 2)
		score = 0
		return score


	class Bird(pygame.sprite.Sprite):

		def __init__(self, x, y):
			pygame.sprite.Sprite.__init__(self)
			self.images = []
			self.index = 0
			self.counter = 0
			for num in range (1, 4):
				img = pygame.image.load(f"img/bird{num}.png")
				self.images.append(img)
			self.image = self.images[self.index]
			self.rect = self.image.get_rect()
			self.rect.center = [x, y]
			self.vel = 0
			self.clicked = False

		def update(self):

			if flying == True:
				#apply gravity
				self.vel += 0.5
				if self.vel > 8:
					self.vel = 8
				if self.rect.bottom < 768:
					self.rect.y += int(self.vel)

			if game_over == False:
				#jump
				if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
					self.clicked = True
					self.vel = -10
				if pygame.mouse.get_pressed()[0] == 0:
					self.clicked = False

				#handle the animation
				flap_cooldown = 5
				self.counter += 1
				
				if self.counter > flap_cooldown:
					self.counter = 0
					self.index += 1
					if self.index >= len(self.images):
						self.index = 0
					self.image = self.images[self.index]


				#rotate the bird
				self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
			else:
				#point the bird at the ground
				self.image = pygame.transform.rotate(self.images[self.index], -90)



	class Pipe(pygame.sprite.Sprite):

		def __init__(self, x, y, position):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.image.load("img/pipe1.png")
			self.rect = self.image.get_rect()
			#position variable determines if the pipe is coming from the bottom or top
			#position 1 is from the top, -1 is from the bottom
			if position == 1:
				self.image = pygame.transform.flip(self.image, False, True)
				self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
			elif position == -1:
				self.rect.topleft = [x, y + int(pipe_gap / 2)]


		def update(self):
			self.rect.x -= scroll_speed
			if self.rect.right < 0:
				self.kill()



	class Button():
		def __init__(self, x, y, image):
			self.image = image
			self.rect = self.image.get_rect()
			self.rect.topleft = (x, y)

		def draw(self):
			action = False

			#get mouse position
			pos = pygame.mouse.get_pos()

			#check mouseover and clicked conditions
			if self.rect.collidepoint(pos):
				if pygame.mouse.get_pressed()[0] == 1:
					action = True

			#draw button
			screen.blit(self.image, (self.rect.x, self.rect.y))

			return action



	pipe_group = pygame.sprite.Group()
	bird_group = pygame.sprite.Group()

	flappy = Bird(100, int(HEIGHT / 2))

	bird_group.add(flappy)

	#create restart button instance
	button = Button(WIDTH // 2 - 50, HEIGHT // 2 - 100, button_img)


	run = True
	while run:

		clock.tick(fps)

		#draw background
		screen.blit(bg, (0,0))

		pipe_group.draw(screen)
		bird_group.draw(screen)
		bird_group.update()

		#draw and scroll the ground
		screen.blit(ground_img, (ground_scroll, 768))

		#check the score
		if len(pipe_group) > 0:
			if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
				and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
				and pass_pipe == False:
				pass_pipe = True
			if pass_pipe == True:
				if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
					score += 1
					pass_pipe = False
		draw_text(str(score), font, RED, int(WIDTH / 2), 20)


		#look for collision
		if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
			game_over = True
		#once the bird has hit the ground it's game over and no longer flying
		if flappy.rect.bottom >= 768:
			game_over = True
			flying = False


		if flying == True and game_over == False:
			#generate new pipes
			time_now = pygame.time.get_ticks()
			if time_now - last_pipe > pipe_frequency:
				pipe_height = random.randint(-100, 100)
				btm_pipe = Pipe(WIDTH, int(HEIGHT / 2) + pipe_height, -1)
				top_pipe = Pipe(WIDTH, int(HEIGHT / 2) + pipe_height, 1)
				pipe_group.add(btm_pipe)
				pipe_group.add(top_pipe)
				last_pipe = time_now

			pipe_group.update()

			ground_scroll -= scroll_speed
			if abs(ground_scroll) > 35:
				ground_scroll = 0

		#check for game over and reset
		if game_over == True:
			if button.draw():
				game_over = False
				updateSCORES(score)
				score = reset_game()


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
				flying = True

		pygame.display.update()


def Main_Menu():
#load button images
	level1_img= pygame.image.load("FinalProject\FinalProjectImages\Level1.png").convert_alpha()
	level2_img= pygame.image.load("FinalProject\FinalProjectImages\Level2.png").convert_alpha()
	level3_img= pygame.image.load("FinalProject\FinalProjectImages\Level3.png").convert_alpha()
	exit_img = pygame.image.load('FinalProject\FinalProjectImages\Quit.png').convert_alpha()
	scores_img = pygame.image.load('FinalProject\FinalProjectImages\HighSCORES.png').convert_alpha()

	#create button instances
	level1_button = button.Button(250, 15, level1_img, 0.6)
	level2_button= button.Button(205,150, level2_img, 0.6)
	level3_button= button.Button(250,325, level3_img, 0.6)
	exit_button = button.Button(275, 500, exit_img,0.8)
	scores_button= button.Button(175,650, scores_img,0.8)

	#game loop
	run = True
	while run:
		screen.blit(bg,(0,0))

		if level1_button.draw(screen):
			Level1UNDERWATER()
		if level2_button.draw(screen):
			Level2NIGHTMODE()
		if level3_button.draw(screen):
			Level3HARD()
		if exit_button.draw(screen):
			QUIT()
		if scores_button.draw(screen):
		    printSCORES()
		    updateSCORES(score)

		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False

		pygame.display.update()

Main_Menu()

pygame.quit()