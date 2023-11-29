import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Game Window Setup
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('assets/Fonts/MelodyStories.otf', 60)
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode([WIDTH, HEIGHT])
target_images=[]
menu=True
high_score=0

# Load Assets
guns = pygame.transform.scale(pygame.image.load('assets/gun/Harpoon.png'), (150, 150))
bg = pygame.transform.scale(pygame.image.load('assets/bg/bg.jpg'), (900, 800))
banner= pygame.transform.scale(pygame.image.load(f'assets/banner/banner.png'), (900,100))
heart_image = pygame.transform.scale(pygame.image.load('assets/life/heart.png'), (30, 30))
menu_image= pygame.image.load(f'assets/menu/menu.png')
for i in range(1,5):
     target_images.append(pygame.image.load(f'assets/targets/{i}.png'))

def draw_menu():
    screen.blit(menu_image,(0,0))
    mouse_pos=pygame.mouse.get_pos()
    clicks=pygame.mouse.get_pressed()
    play_button=pygame.rect.Rect((302, 330),(245,75))
    screen.blit(font.render(f'{high_score}',True,'black'),(510, 198))

    if play_button.collidepoint(mouse_pos) and clicks[0]and not clicked: 
        level=1
        menu=False
                                                      
    
# Game Variables
lives = 3  # Starting lives
level = 1
score = 0
targets = []

# Function to draw the gun
def draw_gun():
    mouse_pos = pygame.mouse.get_pos()
    gun_point = (WIDTH/2, HEIGHT-100)
    lasers = ['brown']
    clicks = pygame.mouse.get_pressed()

    if mouse_pos[0] != gun_point[0]:
        slope = (mouse_pos[1] - gun_point[1]) / (mouse_pos[0] - gun_point[0])
    else:
        slope = -100000000000000

    angle = math.atan(slope)
    rotation = math.degrees(angle)

    if mouse_pos[0] < WIDTH/2:
        gun = pygame.transform.flip(guns, True, False)
        if mouse_pos[1] < 600:
            screen.blit(pygame.transform.rotate(gun, 90 - rotation), ((WIDTH/2) - 90, HEIGHT - 250))
            if clicks[0]:
                pygame.draw.circle(screen, lasers[level-1], mouse_pos, 5)
    else:
        gun = guns
        if mouse_pos[1] < 600:
            screen.blit(pygame.transform.rotate(gun, 270 - rotation), (WIDTH/2 - 30, HEIGHT - 250))
            if clicks[0]:
                pygame.draw.circle(screen, lasers[level-1], mouse_pos, 5)
# Function to draw lives
def draw_lives():
    for i in range(lives):
        screen.blit(heart_image, (10 + i * 40, 10))


# Main Game Loop
run = True
while run:
    timer.tick(fps)
    screen.fill('white')
    screen.blit(bg, (0, 0))
    screen.blit(banner,(0,HEIGHT-100))

    if menu:
        level==0
        draw_menu()

    draw_gun()
    draw_lives()

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()