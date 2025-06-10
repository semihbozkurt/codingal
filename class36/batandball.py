import pygame
pygame.init()

width=500
hight=500

screen=pygame.display.set_mode((width,hight))
clock=pygame.time.Clock()
running=True

background=pygame.image.load(r"Cayir.png")
background=pygame.transform.scale(background,(width,hight))


score=0
numlives=5

scorefont=pygame.font.Font(None,32)
finishfont=pygame.font.Font(None,55)






batx=200
baty=450
bally=20
import random
ballx=random.randint(0,width)

colorlist=["green","red","blue","orange","purple","black","yellow","pink","brown","gray","cyan"]

class Bat(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.Surface((150,50))

        self.image.fill("blue")

        self.rect = self.image.get_rect()

        self.rect.x = 200

        self.rect.y = 450


class Ball (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((100,100),pygame.SRCALPHA)
        pygame.draw.circle(self.image,random.choice(colorlist),(50,50),20)
        self.rect=self.image.get_rect()
        self.rect.x=random.randint(0,width)

    def update(self):
        self.rect.y+=1






bat=Bat()
playergroup=pygame.sprite.Group()
playergroup.add(bat)
ball=Ball()
enemygroup=pygame.sprite.Group()
enemygroup.add(ball)

count=0




while running:

    textsurfece=scorefont.render(f"score={score}",True,(255,255,255))
    livestext=scorefont.render(f"lives={numlives}",True,(255,255,255))
    finish=finishfont.render(f"GAME-OVER SCORE:{score}",True,(50,50,100))

    screen.blit(background,(0,0))
    screen.blit(textsurfece,(50,50))
    screen.blit(livestext,(50,100))
    

    playergroup.draw(screen)
    enemygroup.draw(screen)
    enemygroup.update()
    

    
    count+=1
    if count%100==0: 
        ball=Ball()
        enemygroup.add(ball)


    for ball in enemygroup:
            if ball.rect.y>=hight:
                ball.kill()
                numlives-=1


    if numlives==0:
            bat.kill()
            enemygroup.empty()
            screen.blit(finish,(1,250))



    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and bat.rect.x>0:
                bat.rect.x-=30
            if event.key==pygame.K_RIGHT and bat.rect.x<width-150:
                bat.rect.x+=30
    if pygame.sprite.spritecollideany(bat,enemygroup):
        pygame.sprite.spritecollide(bat,enemygroup,True)
        score+=1
        
        
        
        

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

ballY = 10

import random

ballX = random.randint(0,width)

colorList = ["red","green","blue","yellow","purple","orange","pink","brown","black","white","gray","cyan","magenta","lime","teal","maroon","navy","olive","silver","gold","beige","turquoise","lavender","indigo","violet","plum"]

# currenlty bat and ball are not being taken as game Object

class Bat(pygame.sprite.Sprite):

def __init__(self):

super().__init__()

self.image = pygame.Surface((150,50),pygame.SRCALPHA)

self.image.fill("blue")

self.rect = self.image.get_rect()

self.rect.x = 200

self.rect.y = 450

class Ball(pygame.sprite.Sprite):

def __init__(self):

super().__init__()

self.image = pygame.Surface((100,100),pygame.SRCALPHA)

pygame.draw.circle(self.image,random.choice(colorList),(50,50),20)

self.rect = self.image.get_rect() #i want to get the container of the circle

self.rect.x = random.randint(0,width)

# sprite class: overriding

def update(self):

self.rect.y += 1

bat = Bat()

ball = Ball()

player = pygame.sprite.Group()

enemygroup = pygame.sprite.Group()

enemygroup.add(ball)

player.add(bat)

count = 0

while runningStatus:

screen.fill("white")

# pygame.draw.rect(screen, "blue",(batX, batY, 150, 50))

player.draw(screen)

enemygroup.draw(screen)

enemygroup.update()


count += 1


if count % 100 == 0:


ball = Ball()

enemygroup.add(ball)

# pygame.draw.circle(screen, "red", (ballX, ballY), 20)

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

if pygame.sprite.spritecollideany(bat, enemygroup):

pygame.sprite.spritecollide(bat, enemygroup,False)

clock.tick(60)

pygame.display.update()



"""