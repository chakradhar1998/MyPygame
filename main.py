import pygame

#initialize the pygame
pygame.init()

#create a screen
screen = pygame.display.set_mode((800, 600))

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
HunterX = 370
HunterY = 200


def Player(x,y):
    screen.blit(PlayerImg,(x,y))


def Hunter(x,y):
    screen.blit(HunterImg,(x,y))

#game loop
running = True
while running:

    screen.fill((0,0,0))



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

    PlayerX += Player_change

    if PlayerX <=0:
        PlayerX = 0
    elif PlayerX >=736:
        PlayerX = 736


    Player(PlayerX,PlayerY)
    Hunter(HunterX,HunterY)
    pygame.display.update()