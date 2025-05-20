import pygame
pygame.init()

width=800
height=600
screen=pygame.display.set_mode((800,600))

pygame.display.set_caption("First game")

red=(250,2,2)
green=(0,250,0)   #rpg numbers
blue=(0,0,250)

runing=True
#loop
while runing:
    screen.fill(red)
    pygame.display.update()

pygame.quit()

