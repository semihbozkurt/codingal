import pygame
pygame.init()

width=800
height=600

screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("earth and moon")

runing=True

class Earth (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((220,220),pygame.SRCALPHA)
        pygame.draw.circle(self.image,"blue",(150,150),70)
        self.rect=self.image.get_rect()
        self.rect.x=200
        self.rect.y=100

earth=Earth()
earthgroup=pygame.sprite.Group()
earthgroup.add(earth)
while runing:
    screen.fill("red")
    earthgroup.draw(screen)
    
    
    pygame.display.update()


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runing=False

pygame.quit()
