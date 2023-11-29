import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Game Window Setup
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('assets/Fonts/MelodyStories.otf', 32)
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode([WIDTH, HEIGHT])
target_images=[]

# Load Assets
guns = pygame.transform.scale(pygame.image.load('assets/gun/Harpoon.png'), (150, 150))
bg = pygame.transform.scale(pygame.image.load('assets/bg/bg.jpg'), (900, 800))
heart_image = pygame.transform.scale(pygame.image.load('assets/life/heart.png'), (30, 30))
for i in range(1,5):
     target_images.append(pygame.image.load(f'assets/targets/{i}.png'))

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

class Enemy:
    def __init__(self, x, y, type, speed):
        self.x = x
        self.y = y
        self.type = type
        self.speed = speed

        # Add other attributes like image, health, etc.

    def draw(self):
        # Placeholder for drawing the enemy
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 20)

    def update(self):
        # Placeholder for updating enemy position
        self.y += self.speed
        if self.y > HEIGHT:
            global lives
            lives -= 1  # Lose a life if enemy passes the bottom
            targets.remove(self)

# Function to spawn enemies
def spawn_enemy():
    # Placeholder enemy spawning logic
    if random.randint(0, 60) == 1:  # Random chance to spawn an enemy
        new_enemy = Enemy(random.randint(0, WIDTH), 0, 1, 5)
        targets.append(new_enemy)

# Main Game Loop
run = True
while run:
    timer.tick(fps)
    screen.fill('white')
    screen.blit(bg, (0, 0))

    # Spawn and update enemies
    spawn_enemy()
    for enemy in targets[:]:
        enemy.update()
        enemy.draw()

    draw_gun()
    draw_lives()

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()