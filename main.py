import pygame
import math

# Initialize Pygame
pygame.init()

# Game Window Setup
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('assets/Fonts/MelodyStories.otf', 60)
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode([WIDTH, HEIGHT])
target_images = []
menu = True
high_score = 0
level_coords = [[], [], [], []]

# Game Variables
lives = 3
level = 1
points = 0
shot = False
clicked = False
target = {1: [15, 12, 8, 3]}

# Load Assets
guns = pygame.transform.scale(pygame.image.load('assets/gun/Harpoon.png'), (150, 150))
bg = pygame.transform.scale(pygame.image.load('assets/bg/bg.jpg'), (900, 800))
banner = pygame.transform.scale(pygame.image.load(f'assets/banner/banner.png'), (900, 100))
heart_image = pygame.transform.scale(pygame.image.load('assets/life/heart.png'), (30, 30))
menu_image = pygame.image.load(f'assets/menu/menu.png')
for i in range(1, 5):
    target_images.append(pygame.transform.scale(pygame.image.load(f'assets/targets/{i}.png'), (100, 100)))

file = open('high_score.txt', 'r')
read_file = file.readlines()
file.close()
high_score = int(read_file[0])

pygame.mixer.init()
pygame.mixer.music.load('assets/sounds/Super Mario 64 - Water Theme  Dire Dire Docks - HD.mp3')
harpoon_sound = pygame.mixer.Sound('assets/sounds/Harpoon sound- sound effect..mp3')
harpoon_sound.set_volume(.2)
pygame.mixer.music.load('assets/sounds/Donkey Kong Country - Aquatic Ambience [Restored].mp3')

def draw_menu():
    global menu, level, clicked  
    screen.blit(menu_image, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    clicks = pygame.mouse.get_pressed()
    play_button = pygame.Rect((302, 330), (245, 75))
    exit_button = pygame.Rect((315, 490), (230, 75))
    screen.blit(font.render(f'{high_score}', True, 'black'), (510, 198))

    if play_button.collidepoint(mouse_pos) and clicks[0] and not clicked:
        level = 1
        menu = False
        clicked = True
    elif exit_button.collidepoint(mouse_pos) and clicks[0] and not clicked:
        level = 2
        menu = False
        clicked = True

def draw_gun():
    global shot  
    mouse_pos = pygame.mouse.get_pos()
    gun_point = (WIDTH / 2, HEIGHT - 100)
    lasers = ['brown']
    clicks = pygame.mouse.get_pressed()

    if mouse_pos[0] != gun_point[0]:
        slope = (mouse_pos[1] - gun_point[1]) / (mouse_pos[0] - gun_point[0])
    else:
        slope = -100000000000000

    angle = math.atan(slope)
    rotation = math.degrees(angle)

    if mouse_pos[0] < WIDTH / 2:
        gun = pygame.transform.flip(guns, True, False)
        if mouse_pos[1] < 600:
            screen.blit(pygame.transform.rotate(gun, 90 - rotation), ((WIDTH / 2) - 90, HEIGHT - 250))
            if clicks[0]:
                pygame.draw.circle(screen, lasers[level - 1], mouse_pos, 5)
                shot = True
    else:
        gun = guns
        if mouse_pos[1] < 600:
            screen.blit(pygame.transform.rotate(gun, 270 - rotation), (WIDTH / 2 - 30, HEIGHT - 250))
            if clicks[0]:
                pygame.draw.circle(screen, lasers[level - 1], mouse_pos, 5)
                shot = True

def draw_score():
    points_text = font.render(f'{points}', True, 'black')
    screen.blit(points_text, (280, 620))
def exit_level():
    mouse_pos = pygame.mouse.get_pos()
    clicks = pygame.mouse.get_pressed()
    exit_button=pygame.rect.Rect((720, 620), (100,75) )
    if exit_button.collidepoint(mouse_pos) and clicks[0] and not clicked:
        level=0       
        clicked = True

def move_level(coords):
    global level  
    max_val = 4
    for i in range(max_val):
        for j in range(len(coords[i])):
            my_coords = coords[i][j]
            if my_coords[0] < -150:
                coords[i][j] = (WIDTH, my_coords[1])
            else:
                coords[i][j] = (my_coords[0] - 2 ** i, my_coords[1])
    return coords

def draw_level(coords):
    global target_rects, level  
    if level == 1:
        target_rects = [[], [], [], []]

    for i in range(len(coords)):
        for j in range(len(coords[i])):
            target_rects[i].append(pygame.Rect((coords[i][j][0] + 20, coords[i][j][1]),
                                               (60 - i * 12, 60 - i * 12)))
            screen.blit(target_images[i], coords[i][j])
    return target_rects

for i in range(4):
    my_list = target[1]
    for j in range(my_list[i]):
        level_coords[i].append((WIDTH // (my_list[i]) * j, 300 - (i * 100) + 30 * (j % 2)))

def check_shot(targets, coords):
    global points 
    mouse_pos = pygame.mouse.get_pos()
    for i in range(len(targets)):
        for j in range(len(targets[i])):
            if targets[i][j].collidepoint(mouse_pos):
                coords[i].pop(j)
                points += 10 + 10 * (i ** 2)
                if level == 1:
                    harpoon_sound.play()
    return coords

# Main Game Loop
run = True
while run:
    timer.tick(fps)
    screen.fill('white')
    screen.blit(bg, (0, 0))
    screen.blit(banner, (0, HEIGHT - 100))

    if menu:
        level = 0  
        pygame.mixer.music.play()
        draw_menu()

    if level == 1:
        target_boxes = draw_level(level_coords)
        level_coords = move_level(level_coords)
        if shot:
            level_coords = check_shot(target_boxes, level_coords)
            shot = False
    if level > 0:
        draw_gun()
        draw_score()
        exit_level()
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_position = pygame.mouse.get_pos()
            if (0 < mouse_position[0] < WIDTH) and (0 < mouse_position[1] < HEIGHT - 200): 
                shot = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and clicked:
            clicked = False
        if level == 1:
            if points > high_score:  
                high_score = points

    file = open('high_score.txt', 'w')
    file.write(f'{high_score}')
    file.close()

    pygame.display.flip()

pygame.quit()