import math
import time

import pygame

import random

# Initializing the Screen
pygame.init()

# Creating The Display
W = 400
H = 600
screen = pygame.display.set_mode((W, H))
delay = 0.1

# Background Image
backgroundImg = pygame.image.load('road100.png').convert()
backgroundY = 0
backgroundY_change = 0
image_Height = 600

# Player Image
playerImg = pygame.image.load('car12.png')
playerX = 230
playerY = 440
playerX_change = 0
playerY_change = 0

# Traffic Image
trafficImg = pygame.image.load('traffic.png')
trafficX = 300
trafficY = -300
trafficY_change = random.randint(30, 40)

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font("freesansbold.ttf", 64)
over_font_xcord = 400
over_font_ycord = 300


# Functions
def game_over():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (10, 300))


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (textX, textY))


def player(x, y):
    screen.blit(playerImg, (x, y))


def traffic(x, y):
    screen.blit(trafficImg, (x, y))


running = True
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Keyboard Bindings
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                backgroundY_change = 70
                playerY += playerY_change
                playerY_change = -10

            elif event.key == pygame.K_LEFT:
                playerX_change = -14
            elif event.key == pygame.K_RIGHT:
                playerX_change = 14
            elif event.key == pygame.K_DOWN:
                backgroundY_change = 0
                playerY_change = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                playerY_change = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_DOWN:
                playerY_change = 0

    # Player Movement
    playerX += playerX_change

    playerY += playerY_change
    backgroundY += backgroundY_change

    # Background Movement
    relative_y = backgroundY % image_Height
    screen.blit(backgroundImg, (0, relative_y - 600))
    if relative_y < H:
        screen.blit(backgroundImg, (0, relative_y))

    # Border Collision
    if playerX <= 20:
        playerX = 20
    if playerX >= 300:
        playerX = 300
    if playerY >= 440:
        playerY = 440

    # For car not crossing the full of the display window
    if playerY <= 370:
        playerY = 370
        # For increasing the car speed
        backgroundY_change = 140

    time.sleep(delay)

    # Traffic Cars Movement
    trafficY += trafficY_change
    if trafficY > 600:
        trafficY = -100
        trafficX = random.randint(40, 280)

    # Scoring
    if trafficY == -100:
        score_value += 10


    # Collision
    playerCar = pygame.Rect(playerX, playerY, 60, 130)
    trafficCar = pygame.Rect(trafficX, trafficY, 60, 130)
    if playerCar.colliderect(trafficCar):
        game_over()
        playerX = 1000
        backgroundY_change = 0
        backgroundY = 0
        trafficY_change = 0


    traffic(trafficX, trafficY)

    player(playerX, playerY)

    show_score(textX, textY)


    pygame.display.update()
