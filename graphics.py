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

# STATE #########
BLANK=1
ACTION=2

PLAYER_ALLY=1
PLAYER_AXIS=-1

SELECT=1
MOVE=2
MOVE_POPUP=3
#############

DISPLAYSURF = pygame.display.set_mode((WINDOW_W,WINDOW_H))
pygame.display.set_caption('World War!')

BASICFONT = pygame.font.Font(None, 20)
LARGEFONT = pygame.font.Font(None, 30)
LARGEFONT.set_bold(True)
MEDIUMFONT = pygame.font.Font(None, 25)

# IMAGES #########
NODE_IMG = [pygame.image.load("img/node1.png"),
    pygame.image.load("img/node2.png"),
    pygame.image.load("img/node3.png"),
    pygame.image.load("img/node4.png")]

BG = pygame.image.load("img/map.png")

FLAG_AXIS = pygame.image.load("img/flag_axis.png")
FLAG_ALLY = pygame.image.load("img/flag_ally.png")

CANNON = pygame.image.load("img/cannon.png")
FORT = pygame.image.load("img/fort.png")
#################

RECT_MOVE = pygame.Rect(800, 300, 100, 30)
RECT_MAKE_CANNON = pygame.Rect(800, 400, 100, 60)
RECT_MAKE_FORTRESS = pygame.Rect(775, 525, 150, 60)

RECT_POPUP = pygame.Rect(75, 50, 200, 100)
RECT_MOVE_CANNON = pygame.Rect(100, 100, 20, 20)

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
class TextRectException:
    def __init__(self, message = None):
        self.message = message
    def __str__(self):
        return self.message

def render_textrect(string, font, rect, text_color, background_color, justification=0):
    """Returns a surface containing the passed text string, reformatted
    to fit within the given rect, word-wrapping as necessary. The text
    will be anti-aliased.

    Takes the following arguments:

    string - the text you wish to render. \n begins a new line.
    font - a Font object
    rect - a rectstyle giving the size of the surface requested.
    text_color - a three-byte tuple of the rgb value of the
                 text color. ex (0, 0, 0) = BLACK
    background_color - a three-byte tuple of the rgb value of the surface.
    justification - 0 (default) left-justified
                    1 horizontally centered
                    2 right-justified

    Returns the following values:

    Success - a surface object with the text rendered onto it.
    Failure - raises a TextRectException if the text won't fit onto the surface.
    """
    final_lines = []

    requested_lines = string.splitlines()

    # Create a series of lines that will fit on the provided
    # rectangle.

    for requested_line in requested_lines:
        if font.size(requested_line)[0] > rect.width:
            words = requested_line.split(' ')
            # if any of our words are too long to fit, return.
            for word in words:
                if font.size(word)[0] >= rect.width:
                    raise TextRectException, "The word " + word + " is too long to fit in the rect passed."
            # Start a new line
            accumulated_line = ""
            for word in words:
                test_line = accumulated_line + word + " "
                # Build the line while the words fit.
                if font.size(test_line)[0] < rect.width:
                    accumulated_line = test_line
                else:
                    final_lines.append(accumulated_line)
                    accumulated_line = word + " "
            final_lines.append(accumulated_line)
        else:
            final_lines.append(requested_line)

    # Let's try to write the text out on the surface.

    surface = pygame.Surface(rect.size)
    surface.fill(background_color)

    accumulated_height = 0
    for line in final_lines:
        if accumulated_height + font.size(line)[1] >= rect.height:
            raise TextRectException, "Once word-wrapped, the text string was too tall to fit in the rect."
        if line != "":
            tempsurface = font.render(line, 1, text_color)
            if justification == 0:
                surface.blit(tempsurface, (0, accumulated_height))
            elif justification == 1:
                surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
            elif justification == 2:
                surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
            else:
                raise TextRectException, "Invalid justification argument: " + str(justification)
        accumulated_height += font.size(line)[1]

    return surface

def display_text(text, center, color=BLACK, font=BASICFONT, boundary=False):
    textSurfaceObj = font.render(text, True, color)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = center
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    if boundary:
        textRectObj.inflate_ip(30,20)
        pygame.draw.rect(DISPLAYSURF, color, textRectObj, 3)

def get_hovered_node(pos):
    for n in network:
        if math.sqrt((n.x-pos[0])**2 + (n.y-pos[1])**2)<NODE_R[n.rank]+5:
            return n

def next_turn():
    global selected_1,selected_2,game_state,menu_state,num_to_move,player
    selected_1=None
    selected_2=None
    game_state=SELECT
    menu_state=BLANK
    num_to_move=0
    player = PLAYER_AXIS if player is PLAYER_ALLY else PLAYER_ALLY

# STATE DATA ##############

hovered=None
selected_1=None
selected_2=None

menu_state = BLANK
game_state = SELECT
player = PLAYER_ALLY

move_pointer=None
move_cannon=False
num_to_move = 0

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
                        menu_state=ACTION
                elif game_state == MOVE:
                    if hovered in adjacent_levels(selected_1):
                        selected_2=hovered
                        menu_state=BLANK
                        game_state=MOVE_POPUP
                elif game_state == MOVE_POPUP:
                    if RECT_MOVE_CANNON.collidepoint(event.pos):
                        move_cannon = not move_cannon

            else: # Clicked on Menu
                if menu_state == ACTION and RECT_MOVE.collidepoint(event.pos):
                    game_state=MOVE
                elif menu_state == ACTION and RECT_MAKE_CANNON.collidepoint(event.pos):
                    result = move(selected_1,None, 0, 0, 1, 0)
                    if result[0]:
                        next_turn()
                    else:
                        print result[1]
                elif menu_state == ACTION and RECT_MAKE_FORTRESS.collidepoint(event.pos):
                    result = move(selected_1,None, 0, 0, 0, 1)
                    if result[0]:
                        next_turn()
                    else:
                        print result[1]

        elif event.type == KEYUP:
            if game_state==MOVE_POPUP:
                if event.key >= 48 and event.key < 58:
                    num_to_move=num_to_move*10 + event.key-48
                elif event.key == K_BACKSPACE:
                    num_to_move=num_to_move/10
                elif event.key == K_ESCAPE:
                    game_state=SELECT
                    selected_2=None
                    num_to_move=0
                elif event.key == K_RETURN:
                    result = move(selected_1,selected_2, num_to_move, move_cannon, 0, 0)
                    if result[0]:
                        next_turn()

    ################################


    # DISPLAY ######################

    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(BG, (0,0))


    for n in network:
        nodeimg = NODE_IMG[n.rank]
        imgRect = nodeimg.get_rect()
        imgRect.center = (n.x,n.y)
        DISPLAYSURF.blit(nodeimg,imgRect)

        imgRect = FLAG_AXIS.get_rect()
        imgRect.center = (n.x,n.y-NODE_R[n.rank]-20)
        if n.occupant==PLAYER_AXIS:
            DISPLAYSURF.blit(FLAG_AXIS,imgRect)
        if n.occupant==PLAYER_ALLY:
            DISPLAYSURF.blit(FLAG_ALLY,imgRect)

        if n.cannon:
            imgRect=CANNON.get_rect()
            imgRect.center = (n.x-NODE_R[n.rank]-20,n.y)
            DISPLAYSURF.blit(CANNON,imgRect)

        if n.fortress:
            imgRect=FORT.get_rect()
            imgRect.center = (n.x-NODE_R[n.rank]-20,n.y)
            DISPLAYSURF.blit(FORT,imgRect)

        display_text("%d" % n.number,
                (n.x, n.y + NODE_R[n.rank]+5), BLACK)

    if game_state == MOVE_POPUP:
        pygame.draw.rect(DISPLAYSURF, GREEN, RECT_POPUP, 0)
        pygame.draw.rect(DISPLAYSURF, BLACK, RECT_MOVE_CANNON, 3)
        if move_cannon:
            pygame.draw.rect(DISPLAYSURF, RED, RECT_MOVE_CANNON,0)
        display_text("MOVE CANNON",(RECT_MOVE_CANNON.x+RECT_MOVE_CANNON.width/2+80, RECT_MOVE_CANNON.y+RECT_MOVE_CANNON.height/2), BLACK, MEDIUMFONT)
        display_text("Troops:",(RECT_POPUP.x+50,RECT_POPUP.y+30))
        display_text(str(num_to_move),(RECT_POPUP.x+100,RECT_POPUP.y+30))


    if hovered not in (None,selected_1,selected_2):
        pygame.draw.circle(DISPLAYSURF, COLOR_HOVER, (hovered.x,hovered.y), NODE_R[hovered.rank] + 5, 3)

    if selected_1 is not None:
        pygame.draw.circle(DISPLAYSURF, COLOR_SELECTED, (selected_1.x,selected_1.y), NODE_R[selected_1.rank] + 7, 5)
        if game_state==MOVE:
            for n in adjacent_levels(selected_1):
                pygame.draw.line(DISPLAYSURF, BLACK, (selected_1.x, selected_1.y), (n.x,n.y), 2)

        if game_state == MOVE and move_pointer is not None:
            pygame.draw.line(DISPLAYSURF, RED, (selected_1.x, selected_1.y), (move_pointer[0],move_pointer[1]), 4)
    display_text("Turn: Axis" if player==PLAYER_AXIS else "Turn: Allies", (850,50), BLUE, LARGEFONT)

    if menu_state == ACTION:
        display_text("Troops: %d" % selected_1.number, (850,150), BLUE, LARGEFONT)
        DISPLAYSURF.blit(render_textrect("MOVE",LARGEFONT, RECT_MOVE, BLACK, WHITE, 1), RECT_MOVE)
        pygame.draw.rect(DISPLAYSURF, BLACK, RECT_MOVE.inflate(30,20), 3)
        DISPLAYSURF.blit(render_textrect("MAKE CANNON",LARGEFONT, RECT_MAKE_CANNON, BLACK, WHITE, 1), RECT_MAKE_CANNON)
        pygame.draw.rect(DISPLAYSURF, BLACK, RECT_MAKE_CANNON.inflate(30,20), 3)
        DISPLAYSURF.blit(render_textrect("MAKE FORTRESS",LARGEFONT, RECT_MAKE_FORTRESS, BLACK, WHITE, 1), RECT_MAKE_FORTRESS)
        pygame.draw.rect(DISPLAYSURF, BLACK, RECT_MAKE_FORTRESS.inflate(30,20), 3)

    pygame.display.update()

