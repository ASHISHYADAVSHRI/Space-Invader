import pygame
import random
import math
from pygame import mixer
import wave
# initializing library
pygame.init()

# creating window
screen = pygame.display.set_mode((800, 500))

background = pygame.image.load("background.jpg")

mixer.music.load("background.wav.mp3")
mixer.music.play(-1)
# set caption
pygame.display.set_caption("Space Invader")

# set icon
icon = pygame.image.load("ufo.png.png")
pygame.display.set_icon(icon)

# creating images of space ship
image = pygame.image.load("spaceship.png")
image_x = 250
image_y = 430
image_change = 0
imagey_change = 0

# creating enemy image
enemy = []
enemy_x = []
enemy_y = []
enemyx_change = []
enemyy_change =  []
enemies_num = 9


for i in range(enemies_num):
    enemy.append(pygame.image.load("alien.png"))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 150))
    enemyx_change.append(0.2)
    enemyy_change.append(20)

# creating bullet image
bullet = pygame.image.load("bullet.png")
bullet_x = 500
bullet_y = 800
bulletx_change = 0.9
bullety_change = 0.9
bullet_state = 'ready'



scoring = 0
font = pygame.font.Font('Helloo Kidos.ttf', 30)
text_x = 5
text_y = 10

font_over = pygame.font.Font('Helloo Kidos.ttf', 100)

def score_showing(x, y):
    scoring_x = font.render("Score : " + str(scoring), True, (50, 255, 200))
    screen.blit(scoring_x, (x, y))

def game_over():
    font_1 = font.render(" GAME OVER ", True, (255, 0, 0))
    screen.blit(font_1,(320, 200))

# creating a function to show a image of our space ship
def show_image(x, y):
    screen.blit(image, (x, y))


# creatinf function for enemy
def enemy_image(x, y, i):
    screen.blit(enemy[i], (x, y))


def bullet_image(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet, (x + 17, y + 0))


def collision(enemy_x, enemy_y, bullet_x, bullet_y):
    dist = math.sqrt(math.pow(enemy_x - bullet_x, 2) + (math.pow(enemy_y - bullet_y, 2)))
    if dist < 27:
        return True
    else:
        return False


running = True
while running:
    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # for key down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                image_change = -0.3
            if event.key == pygame.K_RIGHT:
                image_change = +0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_sound = mixer.Sound('gunshot.wav.mp3')
                    bullet_sound.play()
                    bullet_x = image_x
                    bullet_image(image_x, image_y)

            # key for up and down
            if event.key == pygame.K_UP:
                imagey_change = -0.3
            if event.key == pygame.K_DOWN:
                imagey_change = +0.3
        # for key up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                image_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                imagey_change = 0

    # moving shooting space image
    image_x += image_change
    if image_x <= 0:
        image_x = 0
    if image_x >= 736:
        image_x = 736

    # moving up and down
    image_y += imagey_change
    if image_y <= 0:
        image_y = 0
    if image_y >= 436:
        image_y = 436

    # moving enemy image
    for i in range(enemies_num):
        if enemy_y[i] > 350:
            for k in range(enemies_num):
                enemy_y[k] = 4000
            game_over()
            break
        enemy_x[i] += enemyx_change[i]
        if enemy_x[i] <= 0:
            enemyx_change[i] = +0.3
            if scoring > 20:
                enemyx_change[i] = 0.4

                enemyy_change[i] = 20
            enemy_y[i] += enemyy_change[i]
        if enemy_x[i] >= 736:
            enemyx_change[i] = -0.3
            if scoring > 20:
                enemyx_change[i] = -0.4

            enemy_y[i] += enemyy_change[i]

            # for collision
        coll = collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if coll:
            collision_sound = mixer.Sound("laser.mp3")
            collision_sound.play()
            bullet_y = image_y
            bullet_state = 'ready'
            scoring += 1



            enemy_x[i] = random.randint(0, 736)
            enemy_y[i] = random.randint(50, 150)
        enemy_image(enemy_x[i], enemy_y[i], i)


    # for moving bullet
    if bullet_y <= 0:
        bullet_y = image_y
        bullet_state = 'ready'
    if bullet_state == 'fire':
        bullet_image(bullet_x, bullet_y)
        bullet_y -= bullety_change



    # calling the functions

    show_image(image_x, image_y)
    score_showing(text_x, text_y)

    pygame.display.update()
