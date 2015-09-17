#!/usr/bin/env python
import pygame, sys
from pygame import *
from Logic import *
import math

pygame.init()

# SIZES ##################

WINDOW_W,WINDOW_H= (950,700)
NODE_R = [8,10,15,20]

# CONSTANTS ###############

BLANK=1
ACTION=2

PLAYER_ALLY=1
PLAYER_AXIS=-1

SELECT=1
MOVE=2

DISPLAYSURF = pygame.display.set_mode((WINDOW_W,WINDOW_H))
pygame.display.set_caption('World War!')

BASICFONT = pygame.font.Font(None, 20)
LARGEFONT = pygame.font.Font(None, 40)
LARGEFONT.set_bold(True)


NODE_IMG = [pygame.image.load("img/node1.png"),
    pygame.image.load("img/node2.png"),
    pygame.image.load("img/node3.png"),
    pygame.image.load("img/node4.png")]

BG = pygame.image.load("img/map.png")

# COLORS #################

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (0, 0, 0)

COLOR_VALID = (128,255,255)
COLOR_HOVER = (128,0,128)
COLOR_SELECTED = (0,128,128)

# FUNCTIONS ###############

def display_text(text, center, color=BLACK, font=BASICFONT):
    textSurfaceObj = font.render(text, True, color)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = center
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

def get_hovered_node(pos):
    for n in network:
        if math.sqrt((n.x-pos[0])**2 + (n.y-pos[1])**2)<NODE_R[n.rank]+5:
            return n

# STATE DATA ##############

hovered=None
selected_1=None
selected_2=None

menu_state = BLANK
game_state = SELECT
player = PLAYER_ALLY

move_pointer=None
num_to_move = ""

###########################

while True: # main game loop

    # UPDATE #######################

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type ==  MOUSEMOTION:
            hovered=get_hovered_node(event.pos)
            if game_state == MOVE:
                move_pointer = event.pos

        elif event.type == MOUSEBUTTONUP:
            if(event.pos[0] < 750): # Clicked on Map
                if game_state == SELECT:
                    if hovered.occupant==player:
                        selected_1=hovered
                elif game_state == MOVE:
                    if hovered in adjacent_levels(selected_1):
                        selected_2=hovered

                menu_state = ACTION if selected_1 is not None else BLANK
            else: # Clicked on Menu
                if menu_state == ACTION and event.pos[0]>830 and event.pos[0]<870 and event.pos[1]>170 and event.pos[1]<230:
                    game_state=MOVE if game_state is SELECT else SELECT

        elif event.type == KEYUP:
            if menu_state == ACTION:
                if event.key >= 48 and event.key < 58:
                    num_to_move+=str(event.key-48)
                elif event.key == K_BACKSPACE:
                    num_to_move=num_to_move[:-1]

        if selected_1 is not None and selected_2 is not None:
            if num_to_move == '':
                print "Enter a number to move"
                selected_2 = None
            elif move(selected_1,selected_2, int(num_to_move), 0, 0, 0):
                selected_1=None
                selected_2=None
                game_state=SELECT
                menu_state=BLANK
                num_to_move=""
                player = PLAYER_AXIS if player is PLAYER_ALLY else PLAYER_ALLY

    ################################


    # DISPLAY ######################
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(BG, (0,0))

    if hovered not in (None,selected_1,selected_2):
        pygame.draw.circle(DISPLAYSURF, COLOR_HOVER, (hovered.x,hovered.y), NODE_R[hovered.rank] + 5, 3)

    if selected_1 is not None:
        pygame.draw.circle(DISPLAYSURF, COLOR_SELECTED, (selected_1.x,selected_1.y), NODE_R[selected_1.rank] + 7, 5)
        for n in adjacent_levels(selected_1):
            pygame.draw.aaline(DISPLAYSURF, BLACK, (selected_1.x, selected_1.y), (n.x,n.y), 2)
        if game_state == MOVE and move_pointer is not None:
            pygame.draw.aaline(DISPLAYSURF, RED, (selected_1.x, selected_1.y), (move_pointer[0],move_pointer[1]), 4)


    for n in network:
        nodeimg = NODE_IMG[n.rank]
        imgRect = nodeimg.get_rect()
        imgRect.center = (n.x,n.y)
        DISPLAYSURF.blit(nodeimg,imgRect)

        txtcol = BLACK
        if n.occupant==PLAYER_AXIS:
            txtcol = (128,0,0)
        if n.occupant==PLAYER_ALLY:
            txtcol = (0,128,0)

        display_text("%d" % n.number,
                (n.x, n.y + NODE_R[n.rank]+5), txtcol)

    if menu_state == ACTION:
        display_text("Troops: %d" % selected_1.number, (850, 50), BLUE, LARGEFONT)
        display_text(num_to_move, (850,100), BLACK, LARGEFONT)
        display_text("MOVE" if game_state is SELECT else "CANCEL", (850,200), BLACK, LARGEFONT)

    pygame.display.update()

    ################################

