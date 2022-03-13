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
banana_rect= bananaImg.get_rect(midtop=(bananaX,bananaY))


#learn rect using bull
bull_img = pygame.image.load('bulls.png')
bullx=370
bully=480
bull_rect = bull_img.get_rect(midbottom = (bullx,bully))

def Player(x,y):
    screen.blit(PlayerImg,(x,y))


def Hunter(x,y):
    screen.blit(HunterImg,(x,y))

def banana(x,y):
    screen.blit(bananaImg,banana_rect)

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


        if event.type == pygame.MOUSEBUTTONDOWN:
            print("yay")
            bananaY_change = -3
            



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



    banana_rect.top += bananaY_change
    if banana_rect.top == 0:
        bananaY_change = 0
        banana_rect.top = PlayerY

    if bananaY_change == 0:
        banana_rect.left = PlayerX

    banana(bananaX,bananaY)
    Player(PlayerX,PlayerY)
    Hunter(HunterX,HunterY)

    screen.blit(bull_img,bull_rect)
   # bull_rect.top += -4
    pygame.display.update()
    clock.tick(600)