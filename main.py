#Creating an Arcade Shooting Game Gallery
from pickle import FALSE
import pygame
import math

#This prepares the windows will be using
pygame.init()
fps=60
timer= pygame.time.Clock()
font=pygame.font.Font('assets/Fonts/MelodyStories.otf',32)
WIDTH=900
HEIGHT =800
screen =pygame.display.set_mode([WIDTH,HEIGHT])

#Assets that will be used for the game
guns=pygame.transform.scale(pygame.image.load('assets/gun/gun.png'),(66, 200))
bg=pygame.transform.scale(pygame.image.load('assets/bg/bg.jpg'),(900,800))
targets=[]
level=1
 
def draw_gun():
	mouse_pos=pygame.mouse.get_pos()
	gun_point=(WIDTH/2, HEIGHT-200)
	lasers=['brown']
	clicks=pygame.mouse.get_pressed()
	if mouse_pos[0] != gun_point[0]:
		slope=(mouse_pos[1]-gun_point[1])/(mouse_pos[0]-gun_point[0])
	else:
		slope=-100000000000000
	angle = math.atan(slope)
	rotation=math.degrees(angle)
	if mouse_pos[0]	< WIDTH/2:
		gun= pygame.transform.flip(guns,True, False)
		if mouse_pos[1] < 600:
			screen.blit(pygame.transform.rotate(gun,90-rotation), ((WIDTH/2)-90,HEIGHT-250))
			if clicks[0]:
				pygame.draw.circle(screen,lasers[level-1], mouse_pos,5)
	else:
		gun=guns
		if mouse_pos[1] < 600:
			screen.blit(pygame.transform.rotate(gun,270-rotation), (WIDTH/2-30,HEIGHT-250))
			if clicks[0]:
				pygame.draw.circle(screen,lasers[level-1], mouse_pos,5)
			
#Getting the game to run
run=True

while run:
	timer.tick(fps)
	screen.fill('white')
	screen.blit(bg,(0,0))
	
	if level >0:
		draw_gun()
	
	#This willl close the program when the x on window is presssed
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
			
	#This dislpayss what the while asks		
	pygame.display.flip()
	
pygame.quit()#Will close the program
