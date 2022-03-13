import pygame
import random
from sys import exit

#initialize the pygame
pygame.init()
clock = pygame.time.Clock()

#create a screen
screen = pygame.display.set_mode((800, 600))

#background
bg= pygame.image.load('test.png')

#title and icon
pygame.display.set_caption('Bunny chesina game')
icon = pygame.image.load('project.png')
pygame.display.set_icon(icon)

#Player
PlayerImg = pygame.image.load('monkey.png')
PlayerX = 370
PlayerY = 480
Player_change = 0

#Hunter
HunterImg = pygame.image.load('man.png')
HunterX = random.randint(0,736)
HunterY = random.randint(50,150)
HunterX_change = 1
HunterY_change = 0


#banana
bananaImg=pygame.image.load('banana.png')
bananaX = PlayerX
bananaY = PlayerY
bananaY_change = 0


def Player(x,y):
    screen.blit(PlayerImg,(x,y))


def Hunter(x,y):
    screen.blit(HunterImg,(x,y))

#game loop
running = True
while running:

    screen.fill((0,0,0))
    # bg image
    screen.blit(bg,(0,0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False


    # If keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Player_change = -1
                print("left")


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Player_change = 1
                print("right")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Player_change = 0
                print("released")

    #check boundaries for player
    PlayerX += Player_change

    if PlayerX <=0:
        PlayerX = 0
    elif PlayerX >=736:
        PlayerX = 736


    HunterX += HunterX_change

    if HunterX <=0:
        HunterX = 0
        HunterX_change = abs(HunterX_change)
        HunterY += 64 
    elif HunterX >=736:
        HunterX = 736
        HunterX_change = HunterX_change* -1
        HunterY +=64

    Player(PlayerX,PlayerY)
    Hunter(HunterX,HunterY)
    pygame.display.update()
    clock.tick(600)