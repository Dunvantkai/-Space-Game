import pygame
import os
import random
import time
pygame.init()
os.system('cls')
print("Kai's Space Shooter program")
# render screen
screen = pygame.display.set_mode((800, 600))

#Titile
pygame.display.set_caption("Kai's Space Shooters")
icon = pygame.image.load('backdrop.png')
pygame.display.set_icon(icon)

#sub debug
screen.fill((160, 160, 160))
pygame.display.update()
controlls = input("Press (i) to enable controlls debug:")
if controlls == ("i"):
    controlls = True
else:
    controlls = False
print("Game Starting")
time.sleep(2)

#background
background = pygame.image.load('night sky.png')

#player
playerIco = pygame.image.load('ship.png')
playerX = 370
playerY = 500
playerX_change = 0
# score = 0

score_value = 0
font = pygame.font.Font('celtic.ttf', 32)
textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
#enmy
enmyIco = []
enmyX = []
enmyY = []
enmyX_change = []
enmyY_change = []
enmyXB = []
enmyYB = []
numberOFenmy = 5

for e in range(numberOFenmy):
    enmyIco.append (pygame.image.load('enmy.png'))
    enmyX.append (random.randint(0, 736))
    enmyY.append (random.randint(20, 80))
    enmyX_change.append (0.2)
    enmyY_change.append (45)
    enmyXB.append (0)
    enmyYB.append (0)

#bullet
bulletIco = pygame.image.load('bullet.png')
bulletY = 500
bulletX_chnage = 0
bulletY_change = 0.1
bullet_state = "ready"
#player render
def player(x, y):
    screen.blit(playerIco, (x, y))
#enmy render
def enmy(x, y, e):
    screen.blit(enmyIco[e], (x, y))
#bullet render
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIco,(x + 19.4, y))
#hit box check
def Hitbox_math():
    global hit_enmy
    bulletX = fix_bullet_location
    enmyXB[e] = enmyX[e] + 60
    bulletXB = bulletX + 60
    enmyYB[e] = enmyY[e] + 60
    bulletYB = bulletY + 60
    hit_enmy = False
    if bulletX >= enmyX[e] and bulletX <= enmyXB[e] or bulletXB <= enmyXB[e] and bulletXB >= enmyX[e]:
        if bulletY >= enmyY[e] and bulletY <= enmyYB[e] or bulletYB <= enmyYB[e] and bulletYB >= enmyY[e]:
            hit_enmy = True
# Tick game loop
isRunning = True
while isRunning:
    screen.blit(background,(0 , 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if controlls == True:  print("KeyReg(Space)")
                if bullet_state == "ready":
                    fix_bullet_location = playerX
                fire_bullet(fix_bullet_location, bulletY)
            elif event.key == pygame.K_LEFT:
                if controlls == True:  print("KeyReg(Left)")
                playerX_change = -0.2
            elif event.key == pygame.K_RIGHT:
                if controlls == True:  print("KeyReg(Right)")
                playerX_change = +0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                if controlls == True:  print("KeyReg(Space Lifted)")
            elif event.key == pygame.K_LEFT:
                if controlls == True:  print("KeyReg(Left Lifted)")
                playerX_change = 0.0
            elif event.key == pygame.K_RIGHT:
                if controlls == True:  print("KeyReg(Right Lifted)")
                playerX_change = 0.0
    #player walls
    playerX += playerX_change
    if playerX > 738:
        playerX = 736
    if playerX < -0:
        playerX = 0

    #enmy edge of screen bons
    for e in range(numberOFenmy):
        negEnmy = random.uniform(-0.3, -0.1)
        posEnmy = random.uniform(0.3, 0.1)
        enmyX[e] += enmyX_change[e]
        if enmyX[e] > 738:
            enmyX_change[e] = negEnmy
            enmyY[e] += enmyY_change[e]
        if enmyX[e] < 0:
            enmyX_change[e] = posEnmy
            enmyY[e] += enmyY_change[e]
        if bullet_state == "fire":
            #bullet moves up  
            fire_bullet(fix_bullet_location, bulletY)
            bulletY -= bulletY_change
            Hitbox_math()
            # kill check
            if hit_enmy == True:
                score_value = score_value + 1
                # print("Your Score is:", score)
                bullet_state = "ready"
                bulletY = -40
                enmyX[e] = random.randint(0, 736)
                enmyY[e] = random.randint(20, 80)
        enmy(enmyX[e], enmyY[e], e)

        #BULLET MOVE
    if bulletY <= -40:
        bullet_state = "ready"
        bulletY = 500
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()