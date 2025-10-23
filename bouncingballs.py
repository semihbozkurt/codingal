import pygame
import random
pygame.init()

width=800
height=600

screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("bouncing balls")

colorlist=["green","red","blue","orange","purple","black","yellow","pink","brown","gray","cyan"]

runing=True

class Ball (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((100,100),pygame.SRCALPHA)
        pygame.draw.circle(self.image,random.choice(colorlist),(50,50),20)
        self.rect=self.image.get_rect()
        self.rect.x=random.randint(0,width-100)
        self.rect.y=random.randint(0,height-100)
        self.hiz_x=1
        self.hiz_y=2



    def update(self):
            self.rect.y+=hiz_y
            self.rect.x+=hiz_x



ball=Ball()
group=pygame.sprite.Group()
group.add(ball)

while runing:
    screen.fill("red")
    
    group.draw(screen)
    group.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runing=False
            
    if ball.rect.x>=width:
        hiz_x=-hiz_x
    if ball.rect.y>=height:
         hiz_y=-hiz_y


    pygame.display.update()

pygame.quit()
