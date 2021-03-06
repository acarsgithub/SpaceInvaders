import pygame
import random

#initialize pygame
pygame.init()

#set screen size height and width
screen = pygame.display.set_mode((600, 600))

#title of game
pygame.display.set_caption("Space Invaders")


#game icon
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

playerImage = pygame.image.load('rocket2.png')
playerX = 300
playerY = 400
playerX_change = 0

#enemy
enemyImage = pygame.image.load('ufo.png')
enemyX = random.randint(200, 500)
enemyY = random.randint(50, 150)
enemyX_change = 0.25
enemyY_change = 20

def enemy(x, y):
    screen.blit(enemyImage, (x, y))


#our player creation and positioning
def player(x, y):
    screen.blit(playerImage, (x, y))

# game loop 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # left or right movement handling
        if event.type == pygame.KEYDOWN:
            print("Keystroke has been pressed.")
            if event.key == pygame.K_LEFT:
                print("Left key pressed.")
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                print("Right key pressed.")
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been released.")
                playerX_change = 0
    
    screen.fill((0, 0, 0))

    playerX += playerX_change
    # border managing for player
    if playerX <= 0:
        playerX = 0
    if playerX >= 570:
        playerX = 570

    enemyX += enemyX_change
    # border managing for enemy
    if enemyX <= 0:
        enemyX_change = 0.25
        enemyY += enemyY_change
    if enemyX >= 570:
        enemyX_change = -0.25
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()