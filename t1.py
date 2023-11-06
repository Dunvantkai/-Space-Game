import pygame
import os
import random
pygame.init()
os.system('cls')
print("t1")
# render screen
screen = pygame.display.set_mode((800, 600))

#Titile
pygame.display.set_caption("T1")
icon = pygame.image.load('world.png')
pygame.display.set_icon(icon)

#background
background = pygame.image.load('night sky.png')

#player
playerIco = pygame.image.load('ship.png')
playerX = 370
playerY = 500
playerX_change = 0

#enmy
enmyIco = pygame.image.load('enmy.png')
enmyX = random.randint(0, 736)
enmyY = random.randint(20, 80)
enmyX_change = 0.1
enmyY_change = 30

#bullet
bulletIco = pygame.image.load('bullet.png')
bulletY = 500
bulletX_chnage = 0
bulletY_change = 0.2
bullet_state = "ready"

score = 0

def player(x, y):
    screen.blit(playerIco, (x, y))

def enmy(x, y):
    screen.blit(enmyIco, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIco,(x + 19.4, y))

def Hitbox_math():
    global hit_enmy
    bulletX = fix_bullet_location
    enmyXB = enmyX + 64
    bulletXB = bulletX + 64
    enmyYB = enmyY + 64
    bulletYB = bulletY + 64
    hit_enmy = False
    if bulletX >= enmyX and bulletX <= enmyXB or bulletXB <= enmyXB and bulletXB >= enmyX:
        if bulletY >= enmyY and bulletY <= enmyYB or bulletYB <= enmyYB and bulletYB >= enmyY:
            hit_enmy = True




# Tick game loop
isRunning = True
while isRunning:
    # screen.fill((160, 160, 160))
    screen.blit(background,(0 , 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("KeyReg(Space)")
                if bullet_state == "ready":
                    fix_bullet_location = playerX
                fire_bullet(fix_bullet_location, bulletY)
            elif event.key == pygame.K_LEFT:
                print("KeyReg(Left)")
                playerX_change = -0.2
            elif event.key == pygame.K_RIGHT:
                print("KeyReg(Right)")
                playerX_change = +0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print("KeyReg(Space Lifted)")
            elif event.key == pygame.K_LEFT:
                print("KeyReg(Left Lifted)")
                playerX_change = 0.0
            elif event.key == pygame.K_RIGHT:
                print("KeyReg(Right Lifted)")
                playerX_change = 0.0

    playerX += playerX_change
    if playerX > 738:
        playerX = 736
    if playerX < -0:
        playerX = 0

    enmyX += enmyX_change

    if enmyX > 738:
        enmyX_change = -0.1
        enmyY += enmyY_change
    if enmyX < 0:
        enmyX_change = 0.1
        enmyY += enmyY_change
        #BULLET MOVE
    if bulletY <= -40:
        bullet_state = "ready"
        bulletY = 500
        
    if bullet_state == "fire":
        fire_bullet(fix_bullet_location, bulletY)
        bulletY -= bulletY_change
        Hitbox_math()

        if hit_enmy == True:
            score = score + 1
            print(score)
            bullet_state = "ready"
            bulletY = -40
            enmyX = random.randint(0, 736)
            enmyY = random.randint(20, 80)
    player(playerX, playerY)
    enmy(enmyX, enmyY)
    pygame.display.update()