import pygame
#print('test')
import random

#initialize the pygame
pygame.init()
#create the screen
screen = pygame.display.set_mode((800,600))


#just dem sexy title and icon
pygame.display.set_caption("Space Invaders")
icon= pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


running = True
#player
playerImg = pygame.image.load('player.png')
playerX = 380
playerY = 480
playerX_change = 0
#enemy
enemyImg = pygame.image.load('alien.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,200)
enemyX_change = 0

#playerY_change = 0

def player(x=playerX,y=playerY):
    #print(x,y)
    screen.blit(playerImg,(x,y))

def enemy(x=enemyX,y=enemyY):
    screen.blit(enemyImg,(x,y))

while running:
    screen.fill((255,0,0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False  
        #playerX+=0.1
        #keystroke
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                #print("LEFT BOI")
                playerX_change=-0.1
            elif e.key == pygame.K_RIGHT:
                #print("RIGHT BOI")
                playerX_change=0.1
            '''elif e.key == pygame.K_UP:
                #print("TOP KEY")
                playerY_change=-0.1
            elif e.key == pygame.K_DOWN:
                #print("DOWN KEY")
                playerY_change=0.1 -> optional'''
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                print("KeyStroke has been released")
                playerX_change = 0
                #playerY_change = 0 -> optional

    playerX += playerX_change
    #playerY += playerY_change -> optional for more movements ya kno
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 735:
        playerX = 735

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()

    