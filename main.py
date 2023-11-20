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
gun=[]
bg=pygame.image.load('assets/bg/bg.jpg')
targets=[]
level=1

#Getting the game to run
run=True

while run:
	timer.tick(fps)
	screen.fill('white')
	screen.blit(bg,(0,0))
	
	#This willl close the program when the x on window is presssed
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
			
	#This dislpay what the while asks		
	pygame.display.flip()
	
pygame.quit()#Will close the program
