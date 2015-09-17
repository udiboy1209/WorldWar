#!/usr/bin/env python
import pygame, sys
from pygame import *
from Logic import *
import math

pygame.init()

# SIZES ##################

WINDOW_W,WINDOW_H= (950,700)
NODE_R = [8,10,15,20]


##########################

DISPLAYSURF = pygame.display.set_mode((WINDOW_W,WINDOW_H))
pygame.display.set_caption('World War!')

# COLORS #################

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (0, 0, 0)

COLOR_HOVER = (128,0,128)
COLOR_SELECTED = (0,128,128)

##########################

BASICFONT = pygame.font.Font(None, 20)
NODE_IMG = [pygame.image.load("img/node1.png"),
    pygame.image.load("img/node2.png"),
    pygame.image.load("img/node3.png"),
    pygame.image.load("img/node4.png")]

BG = pygame.image.load("img/map.png")

###########################

def display_text(text, color, center):
    textSurfaceObj = BASICFONT.render(text, True, color)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = center
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

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
        elif event.type == MOUSEBUTTONUP:
            selected_1=hovered

    ################################


    # DISPLAY ######################
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(BG, (0,0))

    if hovered not in (None,selected_1,selected_2):
        pygame.draw.circle(DISPLAYSURF, COLOR_HOVER, (hovered.x,hovered.y), NODE_R[hovered.rank] + 5, 3)

    if selected_1 is not None:
        pygame.draw.circle(DISPLAYSURF, COLOR_SELECTED, (selected_1.x,selected_1.y), NODE_R[selected_1.rank] + 7, 5)
        for n in adjacent_levels(selected_1):
            pygame.draw.line(DISPLAYSURF, BLACK, (selected_1.x, selected_1.y), (n.x,n.y), 2)

    for n in network:
        nodeimg = NODE_IMG[n.rank]
        imgRect = nodeimg.get_rect()
        imgRect.center = (n.x,n.y)
        DISPLAYSURF.blit(nodeimg,imgRect)

        display_text("%d" % n.number,
                BLACK,
                (n.x, n.y + NODE_R[n.rank]+5))

    pygame.display.update()

    ################################

