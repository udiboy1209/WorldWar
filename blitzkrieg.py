#!/usr/bin/python

import Tkinter as tk
from Tkinter import Tk, Canvas, Frame, Label, Button
from tkSimpleDialog import *
from tkMessageBox import *
import Image
import ImageTk
import pygame

import Logic


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

def get_node_at(x,y):
    for n in Logic.network:
        if (x-n.x)**2+(y-n.y)**2+5<NODE_R[n.rank]**2:
            return n


class WorldWar(Frame):
    canvas=None
    menu=None
    selected=None
    selected_2=None
    state=SELECT
    player=PLAYER_ALLY

    def __init__(self, parent):

        # IMAGES #########
        self.NODE_IMG = [ImageTk.PhotoImage(Image.open("img/node1.png")),
            ImageTk.PhotoImage(Image.open("img/node2.png")),
            ImageTk.PhotoImage(Image.open("img/node3.png")),
            ImageTk.PhotoImage(Image.open("img/node4.png"))]

        self.BG = ImageTk.PhotoImage(Image.open("img/map.png"))

        self.FLAG_AXIS = ImageTk.PhotoImage(Image.open("img/flag_axis.png"))
        self.FLAG_ALLY = ImageTk.PhotoImage(Image.open("img/flag_ally.png"))

        self.CANNON = ImageTk.PhotoImage(Image.open("img/cannon.png"))
        self.FORTRESS = ImageTk.PhotoImage(Image.open("img/fort.png"))
        #################

        Frame.__init__(self, parent)

        self.parent = parent
        self.init_ui()
        self.update_ui()
        self.update_menu()

    def init_ui(self):
        self.parent.title("World War II")
        self.pack(fill=tk.BOTH, expand=1)

        self.canvas = Canvas(self, width=WINDOW_W-200,height=WINDOW_H)

        #self.canvas.bind("<Motion>",self.motion)
        self.canvas.bind("<Button-1>",self.click)

        self.canvas.pack(side=tk.LEFT)

    def update_ui(self):
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.BG)

        for n in Logic.network:
            self.canvas.create_image(n.x,n.y,anchor=tk.CENTER, image=self.NODE_IMG[n.rank])
            if n.occupant==PLAYER_AXIS:
                self.canvas.create_image(n.x,n.y-NODE_R[n.rank]-5,anchor=tk.S, image=self.FLAG_AXIS)
            if n.occupant==PLAYER_ALLY:
                self.canvas.create_image(n.x,n.y-NODE_R[n.rank]-5,anchor=tk.S, image=self.FLAG_ALLY)

            if n.cannon or n.cannon_time>-1:
                self.canvas.create_image(n.x-NODE_R[n.rank]-5,n.y,anchor=tk.E, image=self.CANNON)
            if n.cannon_time>-1:
                self.canvas.create_text(n.x-NODE_R[n.rank]-5,n.y+NODE_R[n.rank]+5, anchor=tk.NE , text=str(Logic.cannon_makers))
            if n.fortress or n.fortress_time>-1:
                self.canvas.create_image(n.x+NODE_R[n.rank]+5,n.y,anchor=tk.W, image=self.FORTRESS)
            if n.fortress_time>-1:
                self.canvas.create_text(n.x+NODE_R[n.rank]+5,n.y+NODE_R[n.rank]+5, anchor=tk.NW , text=str(Logic.fortress_makers))

            self.canvas.create_text(n.x,n.y+NODE_R[n.rank]+5, anchor=tk.N , text=str(n.allowed))

            if self.selected is not None:
                self.canvas.create_oval(self.selected.x-NODE_R[self.selected.rank]-5,
                        self.selected.y-NODE_R[self.selected.rank]-5,
                        self.selected.x+NODE_R[self.selected.rank]+5,
                        self.selected.y+NODE_R[self.selected.rank]+5,
                        width=3,
                        outline="#0000FF")

                for n in Logic.adjacent_levels(self.selected):
                    self.canvas.create_line(self.selected.x,self.selected.y, n.x,n.y, arrow=tk.LAST, dash=(3,3))

            if self.selected_2 is not None:
                self.canvas.create_oval(self.selected_2.x-NODE_R[self.selected_2.rank]-5,
                        self.selected_2.y-NODE_R[self.selected_2.rank]-5,
                        self.selected_2.x+NODE_R[self.selected_2.rank]+5,
                        self.selected_2.y+NODE_R[self.selected_2.rank]+5,
                        width=3,
                        outline="#FF0000")

    def update_menu(self):
        if self.menu is not None: self.menu.destroy()
        self.menu = Frame(self, width=200,height=WINDOW_H)
        self.menu.pack(fill=tk.X)

        plr = Label(self.menu, text=("Player: ALLIES" if self.player is PLAYER_ALLY else "Player: AXIS"))
        plr.pack(fill=tk.X, padx=5,pady=5)

        if self.selected_2 is not None:
            if  self.selected_2.cannon_time>-1:
                txt = ("%d moves to build" % (Logic.cannon_ready-self.selected_2.cannon_time))
                if self.selected_2.cannon:
                    txt = "cannon present"
                lbl_can = Label(self.menu, text=txt, image=self.CANNON, compound=tk.LEFT)
                lbl_can.pack(fill=tk.X,padx=5,pady=5)

            if  self.selected_2.fortress_time>-1:
                txt = ("%d moves to build" % (Logic.fortress_ready-self.selected_2.fortress_time))
                if self.selected_2.fortress:
                    txt = "fortress present"
                lbl_can = Label(self.menu, text=txt, image=self.FORTRESS, compound=tk.LEFT)
                lbl_can.pack(fill=tk.X,padx=5,pady=5)

            move = Button(self.menu, text="CONFIRM MOVE", command=self.confirm_move)
            move.pack(fill=tk.X, padx=5, pady=5)

            PHOTO = ImageTk.PhotoImage(Image.open(self.selected_2.image))
            data = Label(self.menu, text=self.selected_2.text, wraplength=200, padx=5, pady=5, image=PHOTO, compound=tk.BOTTOM)
            data.pack(fill=tk.X,padx=5,pady=5)

            return

        if self.state==MOVE:
            an = Label(self.menu, text="Select another node")
            an.pack(fill=tk.X, padx=5,pady=5)
            return


        if self.selected is not None:
            if  self.selected.cannon_time>-1:
                txt = ("%d moves to build" % (Logic.cannon_ready-self.selected.cannon_time))
                if self.selected.cannon:
                    txt = "cannon present"
                lbl_can = Label(self.menu, text=txt, image=self.CANNON, compound=tk.LEFT)
                lbl_can.pack(fill=tk.X,padx=5,pady=5)

            if  self.selected.fortress_time>-1:
                txt = ("%d moves to build" % (Logic.fortress_ready-self.selected.fortress_time))
                if self.selected.fortress:
                    txt = "fortress present"
                lbl_can = Label(self.menu, text=txt, image=self.FORTRESS, compound=tk.LEFT)
                lbl_can.pack(fill=tk.X,padx=5,pady=5)

            if self.player == self.selected.occupant:
                move = Button(self.menu, text="MOVE", command=self.move)
                move.pack(fill=tk.X, padx=5, pady=5)

                if not self.selected.cannon:
                    mk_can = Button(self.menu, text="MAKE CANNON", command=self.mk_cannon)
                    mk_can.pack(fill=tk.X, padx=5, pady=5)

                if not self.selected.fortress:
                    mk_ft = Button(self.menu, text="MAKE FORTRESS", command=self.mk_fortress)
                    mk_ft.pack(fill=tk.X, padx=5, pady=5)

            PHOTO = ImageTk.PhotoImage(Image.open(self.selected.image))
            data = Label(self.menu, text=self.selected.text, wraplength=200, padx=5, pady=5, image=PHOTO, compound=tk.BOTTOM)
            data.pack(fill=tk.X,padx=5,pady=5)

    def confirm_move(self):
        num = askinteger("Troops:","Enter number of troops :",parent=self)
        if num==0:
            showerror("Error","Kuch to hila")
        else:
            result=None
            if self.selected.cannon:
                if askyesno("Move cannon?",parent=self):
                    result=Logic.move(self.selected,self.selected_2,num,True,0,0)
                else:
                    result=Logic.move(self.selected,self.selected_2,num,False,0,0)
            else:
                result=Logic.move(self.selected,self.selected_2,num,False,0,0)
            if result[0]:
                self.next_move()
            else:
                showerror("Error",result[1])
                self.selected_2=None
                self.state=SELECT
        self.update_ui()
        self.update_menu()

    def move(self):
        self.state=MOVE
        self.update_ui()
        self.update_menu()


    def mk_cannon(self):
        result=Logic.move(self.selected,None,0,False,1,0)
        if result[0]:
            self.next_move()
        else:
            showerror("Error", result[1])

    def mk_fortress(self):
        result=Logic.move(self.selected,None,0,False,0,1)
        if result[0]:
            self.next_move()
        else:
            showerror("Error", result[1])

    def click(self, event):
        if self.state == SELECT:
            self.selected=get_node_at(event.x,event.y)
        else:
            self.selected_2=get_node_at(event.x,event.y)
            if self.selected_2 == self.selected:
                self.selected_2 = None
        self.update_ui()
        self.update_menu()

    def next_move(self):
        if Logic.network[0].occupant == PLAYER_AXIS:
            showinfo("Game Ends","Player AXIS wins!")
            sys.exit()
        if Logic.network[17].occupant == PLAYER_ALLY:
            showinfo("Game Ends","Player ALLY wins!")
            sys.exit()

        self.selected=None
        self.selected_2=None
        self.state=SELECT
        self.player=PLAYER_AXIS if self.player is PLAYER_ALLY else PLAYER_ALLY
        self.update_ui()
        self.update_menu()

def main():

    pygame.init()
    pygame.mixer.music.load("sounds/instructions.mp3")
    pygame.mixer.music.play(-1)

    root = Tk()
    ex = WorldWar(root)
    root.geometry("950x700+0+0")

    showinfo("Instructions","Please refer to README file for required instrcutions")
    root.mainloop()

main()
