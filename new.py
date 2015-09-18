#!/usr/bin/python

import Tkinter as tk
from Tkinter import Tk, Canvas, Frame, Label, Button
from tkSimpleDialog import *
from tkMessageBox import *
import Image
import ImageTk

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

            data = Label(self.menu, text=self.selected_2.text, wraplength=200, padx=5, pady=5)
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

            data = Label(self.menu, text=self.selected.text, wraplength=200, padx=5, pady=5)
            data.pack(fill=tk.X,padx=5,pady=5)

    def confirm_move(self):
        num = askinteger("Troops:","Enter number of troops :",parent=self)
        if num==0:
            showerror("Kuch to hila",parent=self)
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
                showerror(result[1])
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
        self.selected=None
        self.selected_2=None
        self.state=SELECT
        self.player=PLAYER_AXIS if self.player is PLAYER_ALLY else PLAYER_ALLY

def main():

    root = Tk()
    ex = WorldWar(root)
    root.geometry("950x700+0+0")

    showinfo("Instructions", "1.ADOLF HITLER HAS RISEN AS A DICTATOR IN GERMANY. THE

            HITLER LED NAZI FORCES ARE GETTING STRONGER EVERYDAY.

            THEY HAVE OTHER FORCES LIKE FRANCE, AUSTRIA, HUNGARY,

            ITALY, THE BALKANS, BELARUS AND UKRAINE TO THEIR SUPPORT.

            THESE TOGETHER CONSTITUTE - 'THE AXIS POWERS'. ON THE

            OTHER SIDE OF EUROPE, ANOTHER NEW LEADER IS IN THE MAKING

            - JOSEPH STALIN OF THE SOVIET UNION. HIS FORCES HAVE

            JOINED HANDS WITH THOSE FROM THE UNITED KINGDOM, SPAIN,

            PORTUGAL, TURKEY AND SWEDEN AND TOGETHER THESE CONSTITUTE

            - 'THE ALLIED POWERS'


            2.TENSIONS ARE RISING IN BOTH THE CAMPS AND THE WAR IS

            ABOUT TO BEGIN..........


            3.THE HEAD-QUARTERS IS CRUCIAL TO THE SIDE WINNING THE WAR

            AS ALL THE WAR RELATED ACTIVITIES ARE STRATEGIZED AND

            MANAGED HERE.THE AXIS POWERS HAVE THEIR HEAD-QUARTERS IN

            BERLIN WHILE THE ALLIES HAVE THEIRS IN MOSCOW. YOUR AIM

            IS TO CAPTURE YOUR ENEMY'S HEAD-QUARTERS AND DEFEND YOUR

            OWN SUCCESFULLY. THE TEAM WHOSE HEADQUARTERS IS CAPTURED

            FIRST BY THEIR ENEMY LOSES.


             YOUR WHOLE EMPIRE IS A COLLECTION OF CITIES EACH HAVING

             VARIED IMPORTANCE. ALL CITIES ARE DIVIDED INTO 3 LEVELS-

             LEVEL-1 (WAR-CITY) , LEVEL-2 (MAJOR-WAR-CITY) AND LEVEL-3

             (HEAD-QUARTERS). EACH LEVEL OF CITY IS CONNECTED TO ITS

             SUCCESSIVE LEVEL BY ROAD. ALSO THE WAR CITIES OF BOTH THE

    SIDES- AXIS AND ALLIES ARE ALSO CONNECTED BY ROADS. EACH

    CITY HAS A CERTAIN NUMBER OF ARMY TROOPS. INITIALLY ALL

    YOUR CITIES HAVE TROOPS HAVING YOUR FLAG. TO CAPTURE AN

    ENEMY CITY, THE CITIES HAVE TO BE JOINED BY A ROAD AND

    YOUR TROOPS SHOULD BE ABLE TO DEFEAT THE ENEMY'S TROOPS.

    -

    EACH MOVE BY A PLAYER CORRESPONDS TO ONE MONTH IN THE

    TIMELINE OF THE WAR. EACH MONTH, ONLY ONE MOVE CAN BE

    PLAYED BY EACH PLAYER.

    -

    IF A CITY HAVING YOUR TROOPS ATTACKS A CITY HAVING THE

    OPPONENT'S TROOPS, THE SIDE HAVING THE LARGER NUMBER OF

    TROOPS WINS THE WAR IN THAT CITY. IF YOU WIN THE WAR IN

    THAT CITY THEN ALL OF YOUR OPPONENT'S TROOPS DIE , BUT SO

    DO SOME OF YOURS. HALF THE NUMBER OF YOUR OPPONENT'S

    TROOPS MANAGE TO TAKE ONE TROOP FROM YOUR CITY WHEN THEY

    DIE. AS A RESULT YOU JUST HAVE (YOUR INITIAL TROOPS -

    HALF OF YOUR OPPONENT'S TROOPS) REMAINING THAT TOO IN THE

    CITY WHICH YOU ATTACKED. IF THE NUMBER OF TROOPS IN BOTH

    OF THE CITIES ARE THE SAME, THEN ANY OF THE SIDES WINS

    RANDOMLY. HOWEVER THIS RULE HAS 2 EXCEPTIONS- FORTRESS

    AND CANONS

    -

    A CITY CAN BE CONVERTED INTO A FORTRESS BY EMPLOYING 100

    TROOPS IN THAT CITY TO MAKE THE FORTRESS. BUILDING A

    FORTRESS TAKES 4 MONTHS AND THE FORTRESS IS READY TO USE

    BY THE 5TH MONTH. ONCE TROOPS ARE EMPLOYED IN MAKING A

    FORTRESS, THEY ARE UNABLE TO PARTICIPATE IN WAR TILL THEY

    HAVE COMPLETED WORK ON THE FORTRESS. MEANWHILE IF THE

    ENEMY IS ABLE TO DEFEAT THE REMAINING TROOPS OF THE CITY,

    THE ENEMY TAKES OVER THE WHOLE CITY WITH THE TROOPS

    CREATING THE FORTRESS ALSO SUCCUMBIMG TO DEATH. A

    FORTRESS MADE IN A CITY CANNOT BE MOVED TO ANOTHER CITY.
    A CITY CAN BE MADE INTO A FORTRESS ONLY ONCE AT ANY

    MOMENT OF TIME.
    FOR A CITY WHICH IS A FORTRESS, MINIMUM ONE AND A HALF

    TIMES THAT CITY'S TROOPS NEED TO BE EMPLOYED TO CAPTURE

    OVER THAT CITY. A FORTRESS WILL ONLY USE ITS POWER IF IT

    IS UNABLE TO DEFEAT ITS OPPONENT IN THE NORMAL WAY

    DESCRIBED PREVIOUSLY. AFTER THE FORTRESS HAS BEEN USED,

    IT GETS DESTROYED AND CAN NOW AGAIN BE CREATED IN THAT

    CITY. IF THE FORTRESS IS ABLE TO PROTECT YOUR CITY, NONE

    OF YOUR TROOPS DIE. IF THE FORTRESS IS UNABLE TO DEFEND

    YOUR CITY FROM THE OPPONENTS, ALL YOUR TROOPS AS WELL AS

    THE FORTRESS GET DESTROYED.

    -

    A CANON CAN BE MADE IN A CITY BY EMPLOYING 100 TROOPS IN

    THAT CITY TO MAKE THE CANON. BUILDING A CANON TAKES 3

    MONTHS AND THE CANON IS READY TO USE BY THE 4TH MONTH.

    ONCE TROOPS ARE EMPLOYED IN MAKING A CANON, THEY ARE

    UNABLE TO PARTICIPATE IN WAR TILL THEY HAVE COMPLETED

    WORK ON THE CANON. MEANWHILE IF THE ENEMY IS ABLE TO

    DEFEAT THE REMAINING TROOPS OF THE CITY, THE ENEMY TAKES

    OVER THE WHOLE CITY WITH THE TROOPS CREATING THE CANON

    ALSO SUCCUMBIMG TO DEATH. A CANON CAN BE MOVED VIA ROADS

    TO OTHER CITIES . A CITY CANNOT HAVE 2 CANONS AT ANY

    INSTANT OF TIME.
    A CITY HAVING A CANNON CAN ATTACK UPTO ONE AND A HALF

    TIMES THAT CITY'S TROOPS. IN DOING SO, ALL THE OPPONENTS

    TROOPS DIE AND THE CITY'S TROOP'S DECREASE BUT ONLY BY A

    SMALL AMOUNT (ONE-FOURTH OF THE OPPONENT'S TROOPS IN

    CONTRAST TO HALF OF THE OPPONENT'S TROOPS EARLIER). AFTER

    THE CANON HAS BEEN USED, IT GETS DESTROYED AND CAN NOW

    AGAIN BE CREATED IN THAT CITY. IF IT IS UNABLE TO DEFEAT

    THE OPPONENT'S CITY BUT IS STILL USED, THE CANON GETS

    DESTROYED.

    -

    AT EVERY MOVE, YOU ARE SUPPOSED TO SELECT A CITY HAVING

    YOUR TROOPS AND TYPE THE NUMBER OF TROOPS THAT YOU WANT

    TO MOVE FROM THAT CITY TO ANY OTHER CITY. THEN SELECT THE

    OTHER CITY FROM THE ONES WHICH ARE CONNECTED BY ROADS TO

    THE CITY THAT YOU SELECTED INIITIALLY. ALSO IF YOU WANT

    TO START MAKING A CANON OR A FORTRESS IN A CITY, YOU HAVE

    TO SELECT THAT CITY AND THEN SELECT ON THE MAKE-CANON OR

    MAKE-FORTRESS BUTTON. ONCE A CANON OR FORTRESS IS MADE,

    IT IS DISPLAYED ON THE MAP BESIDES THE CITY. HOWEVER

    THESE ARE ALSO COUNTED AS MOVES AND SO A PLAYER CANNONT

    START MAKING A CANON OR FORTRESS AND SIMULTANEOUSLY

    ATTACK ANOTHER CITY. ALSO YOU MAY MOVE THE CANON ALONG

    WITH YOUR TROOPS FROM ONE CITY TO THE OTHER BY CLICKING

    THE MOVE-CANON BUTTON")

    root.mainloop()

main()
