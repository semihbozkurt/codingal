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
            self.rect.y+=self.hiz_y
            self.rect.x+=self.hiz_x


            if self.rect.x>=width-50 or self.rect.x<=-50:
                self.hiz_x=-self.hiz_x
            if self.rect.y>=height-50 or self.rect.y<=-50:
                self.hiz_y=-self.hiz_y



ball=Ball()
group=pygame.sprite.Group()
group.add(ball)

for i in range (1,9):
         ball=Ball()
         group.add(ball)

while runing:
    screen.fill("red")
    
    
    group.draw(screen)
    
    group.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runing=False
            
   

    
    pygame.display.update()

pygame.quit()
