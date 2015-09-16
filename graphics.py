#!/usr/bin/env python
import pygame, sys
from pygame import *

pygame.init()

window_w,window_h = (700,700)
DISPLAYSURF = pygame.display.set_mode((window_w,window_h))
pygame.display.set_caption('World War Chess!')

# COLORS ##################

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

##########################

BASICFONT = pygame.font.Font(None, 20)
BG = pygame.image.load("map.png")

while True: # main game loop
    DISPLAYSURF.blit(BG, (0,0))
    txtimg=BASICFONT.render(text,True,BLUE)
    DISPLAYSURF.blit(txtimg,(100,50))

    if clicked:
        pygame.draw.ellipse(DISPLAYSURF, GREEN, rect ,1)
    else:
        pygame.draw.ellipse(DISPLAYSURF, BLUE, big_rect ,1)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP:
            mousepos = event.pos
            if rect.collidepoint(mousepos[0],mousepos[1]):
                clicked = False if clicked else True
        elif clicked and event.type == KEYUP:
            if event.key == K_RETURN:
                clicked = False if clicked else True
                text=""
            else:
                text+=str(event.key)

    pygame.display.update()
