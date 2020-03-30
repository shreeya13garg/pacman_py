#name-Shreeya Garg
#Roll no-2018415
#section-B
#group-8
import pygame
from pygame.locals import *
from numpy import loadtxt
import time

#Constants for the game
WIDTH, HEIGHT = (32, 32)
WALL_COLOR = pygame.Color(0, 0, 255, 255) # BLUE
PACMAN_COLOR = pygame.Color(255, 0, 0, 255) # RED
COIN_COLOR = pygame.Color(255, 255, 0, 255) # RED
DOWN = (0,1)
RIGHT = (1,0)
UP = (0,-1)
LEFT = (-1,0)
score=0


#Draws a rectangle for the wall
def draw_wall(screen, pos):
	pixels = pixels_from_points(pos)
	pygame.draw.rect(screen, WALL_COLOR, [pixels, (WIDTH, HEIGHT)])

#Draws a rectangle for the player
def draw_pacman(screen, pos): 
	pixels = pixels_from_points(pos)
	pygame.draw.rect(screen, PACMAN_COLOR, [pixels, (WIDTH, HEIGHT)])

#Draws a rectangle for the coin
def draw_coin(screen, pos):
	pixels = pixels_from_points(pos)
	pygame.draw.rect(screen, COIN_COLOR, [pixels, (WIDTH, HEIGHT)])
def move():
	coordinate=(0,0)
	key_used = pygame.key.get_pressed()
	if key_used[pygame.K_LEFT]:
		coordinate = LEFT
	if key_used[pygame.K_RIGHT]:
		coordinate = RIGHT
	if key_used[pygame.K_UP]:
		coordinate = UP
	if key_used[pygame.K_DOWN]:
		coordinate = DOWN
	return coordinate		
def points(points):
	font = pygame.font.SysFont('Times New Roman',30)
	sum = font.render('points:' +str(points),False,(255,0,0,255))
	screen.blit(sum,(20,25))


#Uitlity functions
def add_to_pos(pos, pos2):
	if pos[0] <  750 and pos[1] < 500:
		return (pos[0]+pos2[0], pos[1]+pos2[1])
	else:
		return(1,1)	

def pixels_from_points(pos):
	return (pos[0]*WIDTH, pos[1]*HEIGHT)


#Initializing pygame
pygame.init()
screen = pygame.display.set_mode((320,320), 0, 32)
background = pygame.surface.Surface((320,320)).convert()


#Initializing variables
layout = loadtxt('layout.txt', dtype=str)
rows, cols = layout.shape
pacman_position = (1,1)
background.fill((0,0,0))
get=[]


# Main game loop 
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		elif event.type==KEYDOWN and (event.key==K_w or event.key==K_UP):
			move_direction=UP
		elif event.type==KEYDOWN and (event.key==K_a or event.key==K_LEFT):
			move_direction=LEFT
		elif event.type==KEYDOWN and (event.key==K_s or event.key==K_DOWN):
			move_direction=DOWN
		elif event.type==KEYDOWN and (event.key==K_d or event.key==K_RIGHT):
			move_direction=RIGHT
							



	screen.blit(background, (0,0))

	#Draw board from the 2d layout array.
  #In the board, '.' denote the empty space, 'w' are the walls, 'c' are the coins
	for col in range(cols):
		for row in range(rows):
			value = layout[row][col]
			pos = (col, row)
			if value == 'w':
				draw_wall(screen, pos)
			elif value == 'c':
				if pos not in get:
					draw_coin(screen, pos)
				else:
					score+=2
				if value=="W" and pacman_position==pos:
					pacman_position=get[-2]
					get=get[0:-1]



	#Draw the player
	draw_pacman(screen, pacman_position)
	points(A)
	#TODO: Take input from the user and update pacman moving direction, Currently hardcoded to always move down
	move_direction = DOWN

	#Update player position based on movement.
	pacman_position = add_to_pos(pacman_position, move_direction)

	#TODO: Check if player ate any coin, or collided with the wall by using the layout array.
	# player should sUP when colliding with a wall
	# coin should dissapear when eating, i.e update the layout array

	#Update the display
	pygame.display.update()

	#Wait for a while, computers are very fast.
	time.sleep(1)