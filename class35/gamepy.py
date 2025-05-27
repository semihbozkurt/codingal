import pygame
pygame.init()

screen=pygame.display.set_mode((800,600))

clock=pygame.time.Clock()

running=True

circleX=400
circleY=300


while running:
    screen.fill("red")
    pygame.draw.circle(screen,"blue",(circleX,circleY),30)
    pygame.display.update()
    circleY+=1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                circleY-=50

    clock.tick(60)
    pygame.time.delay=18


pygame.quit()
