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
Player_rect= PlayerImg.get_rect(topleft= (PlayerX,PlayerY))

#Hunter
HunterImg = pygame.image.load('man.png')
HunterX = random.randint(0,736)
HunterY = random.randint(50,150)
HunterX_change = 1
HunterY_change = 0
Hunter_rect= HunterImg.get_rect(midtop=(HunterX,HunterY))


#banana
bananaImg=pygame.image.load('banana.png')
bananaX = PlayerX +32
bananaY = PlayerY
bananaY_change = 0
banana_rect= bananaImg.get_rect(center=(bananaX,bananaY))




def Player(x,y):
    screen.blit(PlayerImg,Player_rect)


def Hunter(x,y):
    screen.blit(HunterImg,Hunter_rect)

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
                Player_change = -2
                print("left")



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Player_change = 2
                print("right")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Player_change = 0
                print("released")


        if event.type == pygame.MOUSEBUTTONDOWN:
            bananaY_change = -3
            



    #check boundaries for player
    Player_rect.left += Player_change

    if Player_rect.left <=0:
        Player_rect.left = 0
    elif Player_rect.left >=736:
        Player_rect.left = 736


    Hunter_rect.left += HunterX_change

    if Hunter_rect.left <=0:
        Hunter_rect.left = 0
        HunterX_change = abs(HunterX_change)
        Hunter_rect.top += 64 
    elif Hunter_rect.left >=736:
        Hunter_rect.left = 736
        HunterX_change = HunterX_change* -1
        Hunter_rect.top +=64



    banana_rect.top += bananaY_change
    if banana_rect.top == 0:
        bananaY_change = 0
        banana_rect.top = PlayerY

    if bananaY_change == 0:
        banana_rect.left = Player_rect.left

    banana(bananaX,bananaY)
    Player(PlayerX,PlayerY)
    Hunter(HunterX,HunterY)


    if banana_rect.colliderect(Hunter_rect):
        banana_rect.top= PlayerY
        print(banana_rect.top)
        bananaY_change = 0
        Hunter_rect.top = random.randint(50,150)

    pygame.display.update()
    clock.tick(600)