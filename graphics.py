#!/usr/bin/env python
import pygame, sys
from pygame import *
from Logic import *
import math

pygame.init()

# SIZES ##################

WINDOW_W,WINDOW_H= (750,700)
NODE_R = [15,20,30,40]


##########################

DISPLAYSURF = pygame.display.set_mode((WINDOW_W,WINDOW_H))
pygame.display.set_caption('World War!')

# COLORS #################

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

##########################

BASICFONT = pygame.font.Font(None, 20)
NODE_IMG = [pygame.image.load("img/node1.png"),
    pygame.image.load("img/node2.png"),
    pygame.image.load("img/node3.png"),
    pygame.image.load("img/node4.png")]


BG = pygame.image.load("img/map.png")

###########################

def get_hovered_node(pos):
    for n in network:
        lvl = 4-n.level if n.occupant>0 else n.level-5
        if math.sqrt((n.x-pos[0])**2 + (n.y-pos[1])**2)<NODE_R[lvl]:
            return n

# STATE DATA ##############

hovered=None
selected_1=None
selected_2=None

###########################

while True: # main game loop

    # UPDATE #######################

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type ==  MOUSEMOTION:
            hovered=get_hovered_node(event.pos)

    if hovered is not None:
        print n.level, n.x, n.y

    ################################


    # DISPLAY ######################
    DISPLAYSURF.blit(BG, (0,0))
    for n in network:
        lvl = 4-n.level if n.occupant>0 else n.level-5
        DISPLAYSURF.blit(NODE_IMG[lvl], (n.x-NODE_R[lvl]/2, n.y-NODE_R[lvl]/2))
    pygame.display.update()

    ################################

