import pygame
pygame.init()

width=500
hight=500

screen=pygame.display.set_mode((width,hight))
clock=pygame.time.Clock()
running=True

batx=200
baty=450
bally=20
import random
ballx=random.randint(0,width)

class Bat(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.Surface((150,50))

        self.image.fill("blue")

        self.rect = self.image.get_rect()

        self.rect.x = 200

        self.rect.y = 450


class ball (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()



bat=Bat()
playergroup=pygame.sprite.Group()
playergroup.add(bat)



while running:
    screen.fill("white")
    pygame.draw.rect(screen,"blue",(bat.rect.x,bat.rect.y,150,50))
    pygame.draw.circle(screen,"red",(ballx,bally,),20)
    bally+=1
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and bat.rect.x>0:
                bat.rect.x-=30
            if event.key==pygame.K_RIGHT and bat.rect.x<width-150:
                bat.rect.x+=30
    clock.tick(60)
    pygame.display.update()


pygame.quit









"""


import pygame

pygame.init()

height = 500

width = 500

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

runningStatus = True

batX = 200

batY = 450

ballY = 20

import random

# currenlty bat and ball are not being taken as game Object

class Bat(pygame.sprite.Sprite):

def __init__(self):

super().__init__()

self.image = pygame.Surface((150,50))

self.image.fill("blue")

self.rect = self.image.get_rect()

self.rect.x = 200

self.rect.y = 450

class Ball(pygame.sprite.Sprite)

pass


bat = Bat()

ball = Ball()

player = pygame.sprite.Group()

enemygroup = pygame.sprite.Group()

enemygroup.add(ball)

player.add(bat)

ballX = random.randint(0,width)

while runningStatus:

screen.fill("white")

# pygame.draw.rect(screen, "blue",(batX, batY, 150, 50))

player.draw(screen)

pygame.draw.circle(screen, "red", (ballX, ballY), 20)

ballY += 1

for event in pygame.event.get():

if event.type == pygame.QUIT:

runningStatus = False

pygame.quit()

if event.type == pygame.KEYDOWN:

if event.key == pygame.K_LEFT and bat.rect.x > 0:

bat.rect.x -= 30

if event.key == pygame.K_RIGHT and bat.rect.x < width-150:

print("hello")

bat.rect.x += 30

clock.tick(60)

pygame.display.update()



"""