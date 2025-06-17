import pygame
import random
pygame.init()

#music
pygame.mixer.init()
pygame.mixer.music.load("myst.mp3.mp3")
pygame.mixer.music.play(-1)

collisound=pygame.mixer.Sound("colsn.mp3")

running=True
gameover=False

hight=600
width=600

screen=pygame.display.set_mode((width,hight))
clock=pygame.time.Clock()

pygame.display.set_caption("fluffy bird")

score=0
scorefont=pygame.font.Font(None,32)
finishfont=pygame.font.Font(None,55)

birdx=100
birdy=300

#classes
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((50,50))
        pygame.draw.circle(self.image,("red"),(25,25),15)
        
        self.rect = self.image.get_rect()

        self.rect.x = birdx

        self.rect.y = birdy

    def update(self):
        self.rect.y+=2

class Rectengel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((100,random.randint(0,500)))
        self.image.fill("green")

        self.rect = self.image.get_rect()

        self.rect.x = width

        self.rect.y = 0

    def update(self):
        self.rect.x-=3

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
    textsurfece=scorefont.render(f"score={score}",True,(0,0,0))
    finish=finishfont.render(f"GAME-OVER SCORE:{score}",True,(50,50,100))
    screen.blit(textsurfece,(50,50))

    playergroup.draw(screen)
    playergroup.update()
    enemygroup.draw(screen)
    enemygroup.update()
    
    if fluffy.rect.y>=hight or fluffy.rect.y<=0:
        fluffy.kill()
        enemygroup.empty()
        gameover=True

    if not gameover:
        if pygame.sprite.spritecollideany(fluffy,enemygroup):
            fluffy.kill()
            enemygroup.empty()
            screen.blit(finish,(1,260))
            gameover=True

    if gameover:
        screen.blit(finish,(1,260))
        pygame.mixer.music.stop()
    

    if not gameover:
        count+=1
        if count%140==0: 
            ret=Rectengel()
            enemygroup.add(ret)


    for ret in enemygroup:
            if ret.rect.x<=0:
                ret.kill()
                score+=1
    
    


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                fluffy.rect.y-=60
            if event.key==pygame.K_r:
                score=0
                fluffy=Bird()
                playergroup.add(fluffy)
                gameover=False
                pygame.mixer.music.play(-1)


    clock.tick(60)
    pygame.display.update()
