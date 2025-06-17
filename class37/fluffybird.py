import pygame
import random
pygame.init()

#music
pygame.mixer.init()
backsound=pygame.mixer.music.load("myst.mp3.mp3")
pygame.mixer.music.play(-1)

collisound=pygame.mixer.Sound("colsn.mp3")

running=True

hight=600
width=600

screen=pygame.display.set_mode((width,hight))
clock=pygame.time.Clock()

pygame.display.set_caption("fluffy bird")

score=0
scorefont=pygame.font.Font(None,32)

birdx=1
birdy=300

#classes
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((50,50))
        pygame.draw.circle(self.image,("red"),(50,50),20)
        
        self.rect = self.image.get_rect()

        self.rect.x = birdx

        self.rect.y = birdy

    def update(self):
        self.rect.y+=1

class Rectengel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((100,random.randint(0,500)),pygame.SRCALPHA)
        self.image.fill("green")

        self.rect = self.image.get_rect()

        self.rect.x = width

        self.rect.y = 0

    def update(self):
        self.rect.x+=1

#adding the classes
fluffy=Bird()
playergroup=pygame.sprite.Group()
playergroup.add(fluffy)
ret=Rectengel()
enemygroup=pygame.sprite.Group()
enemygroup.add(ret)

count=0

while running:
    #screen
    screen.fill("white")
    textsurfece=scorefont.render(f"score={score}",True,(255,255,255))
    screen.blit(textsurfece,(50,50))

    playergroup.draw(screen)
    enemygroup.draw(screen)
    enemygroup.update()
    
    count+=1
    if count%100==0: 
        ret=Rectengel()
        enemygroup.add(ret)

    
    clock.tick(60)
    pygame.display.update