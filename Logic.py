from random import randint
from math import *
##DEFINE Levels
level1 = 10
level2 = 6
level3 = 3
hq = 1

total_levels = level1 + level2 + level3 + hq

# Axis- RED #################

#LEVEL-1

_node_axis_1 = [(92,636),
        (234,679),
        (338,516),
        (463,469),
        (219,452),
        (297,389),
        (173,389),
        (302,260),
        (424,268),
        (499,371)]



#LEVEL-2
_node_axis_2 = [(198,590),
        (256,428),
        (246,367),
        (348,318),
        (436,396),
        (398,479)]



#LEVEL-3

_node_axis_3 = [(300,460),
        (310,342),
        (419,340)]



#LEVEL-4

_node_axis_4 = [(373,393)]

############################


# Allies- GREEN #############

#LEVEL-1

_node_ally_1 = [(700,508),
        (524,558),
        (676,664),
        (737,324),
        (549,310),
        (623,102),
        (362,189),
        (139,273),
        (72,436),
        (77,527)]



#LEVEL-2

_node_ally_2 = [(577,191),
        (195,291),
        (126,466),
        (425,80),
        (566,515),
        (718,602)]



#LEVEL-3

_node_ally_3 = [(570,253),
        (700,165),
        (663,389)]



#LEVEL-4

_node_ally_4 = [(643,221)]

#############################

##Define Troops at each level
troops1 = 100
troops2 = 100
troops3 = 100
troops4 = 100

cannon_ready = 4
fortress_ready = 5

cannon_makers = 150
fortress_makers = 150

class node:
    def __init__(self , number , occupant , level, cannon, cannon_time, fortress, fortress_time, allowed, x, y):
        self.number = number
        self.occupant = occupant
        self.level = level
        self.rank = 4-self.level if self.occupant>0 else self.level-5
        self.cannon = 0
        self.fortress = 0
        self.cannon_time = -1
        self.fortress_time = -1
        self.allowed = number
        self.x = x
        self.y = y
        return

##Changing Troops at Final Location
    def changetroops_final( self, number_move , initial , valid , Cmove):
        ## initial and final node occupant same
        if initial.occupant == self.occupant :
            self.number = number_move + self.number
            self.allowed = number_move + self.allowed
            if Cmove == True :
                self.cannon = 1
                initial.canon = 0

        ## initial and final node occupant different
        else:

            ## No building goin on
            if self.cannon_time == -1 and self.fortress_time == -1:

                    ## Less Attackers than Defenders
                    if valid == 1:

                        ## Cannon Not Moved From Initial Node
                        if Cmove == False :

                            ## Final Node has No Fortress and No Cannon
                            if self.fortress == 0 and self.cannon == 0 :
                                self.number = self.number - int((number_move)/2)
                                print self.number

                            ## Final Node has No Fortress But A Cannon
                            elif self.fortress == 0 and self.cannon == 1:
                                self.number = self.number - int((number_move)/4)
                                print self.number

                            ## Final Node Has A Fortress
                            #### No Change

            #############CHECK FORTRESS POWER

                        ## Cannon Moved From Initial Node
                        else :

                            ## Final Node has No Fortress and No Cannon
                            if self.fortress == 0 and self.cannon == 0:
                                if self.number > int(1.5*number_move):
                                    self.number = self.number -  int(3*number_move/4)
                                    print self.number
                                else:
                                    self.occupant = initial.occupant
                                    self.number = number_move - int(self.number/4)

                            ## Final Node has No Fortress But A Cannon
                            elif self.fortress == 0 and self.cannon == 1:
                                self.cannon == 0
                                self.number -= int(number_move/2)

                            ## Final Node has A Fortress But No Cannon
                            elif self.fortress == 1 and self.cannon == 0:
                                self.fortress = 0
                                self.number = self.number - int(number_move/2)

                            ## Final Node has A Fortress as well as A Cannon
                            else:
                                self.cannon = 0


                    ## More Attackers than Defenders
                    elif valid == 2:

                        ## Cannon not moved from Initial Node
                        if Cmove == False :

                            ## Final Node has No Fortress and No Cannon
                            if self.fortress == 0 and self.cannon == 0:
                                self.number = number_move - int((self.number)/2)
                                self.occupant = initial.occupant

                            ## Final Node has No Fortress But A Cannon
                            elif self.fortress == 0 and self.cannon == 1:
                                self.cannon == 0
                                if number_moved > int(1.5*self.number):
                                    self.occupant = initial.occupant
                                    self.number = number_moved - int(.75*self.number)

                                else:
                                    self.number -= int(number_moved/4)

                            ## Final Node has A Fortress and No Cannon
                            elif self.fortress == 1 and self.cannon == 0:
                                if number_move > int(1.5*(self.number)):
                                    self.occupant = initial.occupant
                                    self.number = number_move - int(3*self.number/4)


                                else:
                                    self.number = self.number - int(number_move/4)
                                    self.fortress -= 1

                            ## Final Node has A Fortress and A Cannon
                            else:
                                if number_move > 2*(self.number):
                                    self.cannon = 0
                                    self.fortress = 0
                                    self.occupant = initial.occupant
                                    self.number = number_move - self.number

                                elif number_moved < int(1.5*self.number):
                                    self.fortress = 0

                                else:
                                    self.cannon = 0

                        ## Cannon is Moved from Initial Node
                        else:

                            ## Final Node has No Fortress and No Cannon
                            if self.fortress == 0 and self.cannon == 0:
                                self.occupant = initial.occupant
                                self.cannon += 1
                                self.number = number_move - int(self.number/4)

                            ## Final Node has No Fortress But A Cannon
                            elif self.fortress == 0 and self.cannon == 1:
                                self.cannon = 0
                                self.number = number_move - int((self.number)/2)
                                self.occupant = initial.occupant

                            ## Final Node has A Fortress And A Cannon
                            elif self.fortress == 1 and self.cannon == 1:
                                if number_move > int(1.5*(self.number)):
                                    self.occupant = initial.occupant
                                    self.number = number_move - int(3*self.number/4)

                                else:
                                    self.number = self.number - int(number_move/4)
                                    self.fortress -= 1

                            ## Final Node has A Fortress But No Cannon
                            else:
                                self.fortress = 0
                                self.number = number_move - int((self.number)/2)
                                self.occupant = initial.occupant

                    ## Equal
                    else:
                        self.number = int(self.number/2)
                        x = (randint(0,9))
                        if x < 5:
                            self.occupant = initial.occupant


            ## Either cannon or fortress being made
            elif self.cannon_time == -1 != self.fortress_time == -1:
                self.allowed = self.number - self.cannon*cannon_makers - self.fortress*fortress_makers + self.number*self.cannon*0.5 + self.number*self.fortress*0.5

                    ## Less Attackers than Defenders
                if valid == 1 and number_move < self.allowed :

                        ## Cannon Not Moved From Initial Node
                        if Cmove == False :

                            ## Final Node has No Fortress and No Cannon
                            if self.fortress == 0 and self.cannon == 0 :
                                self.number = self.number - int((number_move)/2)
                                print self.number

                            ## Final Node has No Fortress But A Cannon
                            elif self.fortress == 0 and self.cannon == 1:
                                self.number = self.number - int((number_move)/4)
                                print self.number

                            ## Final Node Has A Fortress
                            #### No Change

            #############CHECK FORTRESS POWER

                        ## Cannon Moved From Initial Node
                        else :

                            ## Final Node has No Fortress and No Cannon
                            if self.fortress == 0 and self.cannon == 0:
                                if self.number > int(1.5*number_move):
                                    self.number = self.number -  int(3*number_move/4)
                                    print self.number
                                else:
                                    self.occupant = initial.occupant
                                    self.number = number_move - int(self.number/4)

                            ## Final Node has No Fortress But A Cannon
                            elif self.fortress == 0 and self.cannon == 1:
                                self.cannon == 0
                                self.number -= int(number_move/2)

                            ## Final Node has A Fortress But No Cannon
                            elif self.fortress == 1 and self.cannon == 0:
                                self.fortress = 0
                                self.number = self.number - int(number_move/2)

                            ## Final Node has A Fortress as well as A Cannon
                            else:
                                self.cannon = 0

                        self.allowed=self.number - 100



                elif valid == 1 and self.allowed < number_move:

                        ## Cannon Not Moved From Initial Node
                        if Cmove == False :

                            ## Final Node has No Fortress and No Cannon
                            if self.fortress == 0 and self.cannon == 0 :
                                self.number = self.number - int((number_move)/2)
                                print self.number

                            ## Final Node has No Fortress But A Cannon
                            elif self.fortress == 0 and self.cannon == 1:
                                self.number = self.number - int((number_move)/4)
                                print self.number

                            ## Final Node Has A Fortress
                            #### No Change


            #############CHECK FORTRESS POWER

                        ## Cannon Moved From Initial Node
                        else :

                            ## Final Node has No Fortress and No Cannon
                            if self.fortress == 0 and self.cannon == 0:
                                if self.number > int(1.5*number_move):
                                    self.number = self.number -  int(3*number_move/4)
                                    print self.number
                                else:
                                    self.occupant = initial.occupant
                                    self.number = number_move - int(self.number/4)

                            ## Final Node has No Fortress But A Cannon
                            elif self.fortress == 0 and self.cannon == 1:
                                self.cannon == 0
                                self.number -= int(number_move/2)

                            ## Final Node has A Fortress But No Cannon
                            elif self.fortress == 1 and self.cannon == 0:
                                self.fortress = 0
                                self.number = self.number - int(number_move/2)

                            ## Final Node has A Fortress as well as A Cannon
                            else:
                                self.cannon = 0

                        self.cannon_time = -1
                        self.fortress_time = -1
                        self.allowed=self.number

                elif valid == 1 and self.allowed == number_move:
                    self.number = self.number - number_move
                    self.allowed = 0

                    ## More Attackers than Defenders
                elif valid == 2:

                        ## Cannon not moved from Initial Node
                        if Cmove == False :

                            ## Final Node has No Fortress and No Cannon
                            if self.fortress == 0 and self.cannon == 0:
                                self.number = number_move - int((self.number)/2)
                                self.occupant = initial.occupant

                            ## Final Node has No Fortress But A Cannon
                            elif self.fortress == 0 and self.cannon == 1:
                                self.cannon == 0
                                if number_moved > int(1.5*self.number):
                                    self.occupant = initial.occupant
                                    self.number = number_moved - int(.75*self.number)

                                else:
                                    self.number -= int(number_moved/4)

                            ## Final Node has A Fortress and No Cannon
                            elif self.fortress == 1 and self.cannon == 0:
                                if number_move > int(1.5*(self.number)):
                                    self.occupant = initial.occupant
                                    self.number = number_move - int(3*self.number/4)


                                else:
                                    self.number = self.number - int(number_move/4)
                                    self.fortress -= 1

                            ## Final Node has A Fortress and A Cannon
                            else:
                                if number_move > 2*(self.number):
                                    self.cannon = 0
                                    self.fortress = 0
                                    self.occupant = initial.occupant
                                    self.number = number_move - self.number

                                elif number_moved < int(1.5*self.number):
                                    self.fortress = 0

                                else:
                                    self.cannon = 0

                        ## Cannon is Moved from Initial Node
                        else:

                            ## Final Node has No Fortress and No Cannon
                            if self.fortress == 0 and self.cannon == 0:
                                self.occupant = initial.occupant
                                self.cannon += 1
                                self.number = number_move - int(self.number/4)

                            ## Final Node has No Fortress But A Cannon
                            elif self.fortress == 0 and self.cannon == 1:
                                self.cannon = 0
                                self.number = number_move - int((self.number)/2)
                                self.occupant = initial.occupant

                            ## Final Node has A Fortress And A Cannon
                            elif self.fortress == 1 and self.cannon == 1:
                                if number_move > int(1.5*(self.number)):
                                    self.occupant = initial.occupant
                                    self.number = number_move - int(3*self.number/4)

                                else:
                                    self.number = self.number - int(number_move/4)
                                    self.fortress -= 1

                            ## Final Node has A Fortress But No Cannon
                            else:
                                self.fortress = 0
                                self.number = number_move - int((self.number)/2)
                                self.occupant = initial.occupant

                            self.cannon_time = -1
                            self.fortress_time = -1
                            self.allowed = self.number


            ## Both Cannon and Fortress are being made
            elif self.cannon_time != -1 and self.fortress_time != -1:
                self.allowed = self.number - cannon_makers - fortress_makers

                ## Less Attackers than Defenders
                if valid == 1 and number_move < self.allowed :

                        ## Cannon Not Moved From Initial Node
                        if Cmove == False :

                            ## Final Node has No Fortress and No Cannon
                            if self.fortress == 0 and self.cannon == 0 :
                                self.number = self.number - int((number_move)/2)
                                print self.number

                            ## Final Node has No Fortress But A Cannon
                            elif self.fortress == 0 and self.cannon == 1:
                                self.number = self.number - int((number_move)/4)
                                print self.number

                            ## Final Node Has A Fortress
                            #### No Change

            #############CHECK FORTRESS POWER

                        ## Cannon Moved From Initial Node
                        else :

                            ## Final Node has No Fortress and No Cannon
                            if self.fortress == 0 and self.cannon == 0:
                                if self.number > int(1.5*number_move):
                                    self.number = self.number -  int(3*number_move/4)
                                    print self.number
                                else:
                                    self.occupant = initial.occupant
                                    self.number = number_move - int(self.number/4)

                            ## Final Node has No Fortress But A Cannon
                            elif self.fortress == 0 and self.cannon == 1:
                                self.cannon == 0
                                self.number -= int(number_move/2)

                            ## Final Node has A Fortress But No Cannon
                            elif self.fortress == 1 and self.cannon == 0:
                                self.fortress = 0
                                self.number = self.number - int(number_move/2)

                            ## Final Node has A Fortress as well as A Cannon
                            else:
                                self.cannon = 0

                        self.allowed = self.number - cannon_makers - fortress_makers


                elif valid == 1 and self.allowed < number_move:

                        ## Cannon Not Moved From Initial Node
                        if Cmove == False :

                            ## Final Node has No Fortress and No Cannon
                            if self.fortress == 0 and self.cannon == 0 :
                                self.number = self.number - int((number_move)/2)
                                print self.number

                            ## Final Node has No Fortress But A Cannon
                            elif self.fortress == 0 and self.cannon == 1:
                                self.number = self.number - int((number_move)/4)
                                print self.number

                            ## Final Node Has A Fortress
                            #### No Change

            #############CHECK FORTRESS POWER

                        ## Cannon Moved From Initial Node
                        else :

                            ## Final Node has No Fortress and No Cannon
                            if self.fortress == 0 and self.cannon == 0:
                                if self.number > int(1.5*number_move):
                                    self.number = self.number -  int(3*number_move/4)
                                    print self.number
                                else:
                                    self.occupant = initial.occupant
                                    self.number = number_move - int(self.number/4)

                            ## Final Node has No Fortress But A Cannon
                            elif self.fortress == 0 and self.cannon == 1:
                                self.cannon == 0
                                self.number -= int(number_move/2)

                            ## Final Node has A Fortress But No Cannon
                            elif self.fortress == 1 and self.cannon == 0:
                                self.fortress = 0
                                self.number = self.number - int(number_move/2)

                            ## Final Node has A Fortress as well as A Cannon
                            else:
                                self.cannon = 0

                        self.cannon_time = -1
                        self.fortress_time = -1
                        self.allowed = self.number

                elif valid == 1 and self.allowed == number_move:
                    self.number = self.number - number_move
                    self.allowed = 0


                ## More Attackers than Defenders
                elif valid == 2:

                        ## Cannon not moved from Initial Node
                        if Cmove == False :

                            ## Final Node has No Fortress and No Cannon
                            if self.fortress == 0 and self.cannon == 0:
                                self.number = number_move - int((self.number)/2)
                                self.occupant = initial.occupant

                            ## Final Node has No Fortress But A Cannon
                            elif self.fortress == 0 and self.cannon == 1:
                                self.cannon == 0
                                if number_moved > int(1.5*self.number):
                                    self.occupant = initial.occupant
                                    self.number = number_moved - int(.75*self.number)

                                else:
                                    self.number -= int(number_moved/4)

                            ## Final Node has A Fortress and No Cannon
                            elif self.fortress == 1 and self.cannon == 0:
                                if number_move > int(1.5*(self.number)):
                                    self.occupant = initial.occupant
                                    self.number = number_move - int(3*self.number/4)


                                else:
                                    self.number = self.number - int(number_move/4)
                                    self.fortress -= 1

                            ## Final Node has A Fortress and A Cannon
                            else:
                                if number_move > 2*(self.number):
                                    self.cannon = 0
                                    self.fortress = 0
                                    self.occupant = initial.occupant
                                    self.number = number_move - self.number

                                elif number_moved < int(1.5*self.number):
                                    self.fortress = 0

                                else:
                                    self.cannon = 0

                        ## Cannon is Moved from Initial Node
                        else:

                            ## Final Node has No Fortress and No Cannon
                            if self.fortress == 0 and self.cannon == 0:
                                self.occupant = initial.occupant
                                self.cannon += 1
                                self.number = number_move - int(self.number/4)

                            ## Final Node has No Fortress But A Cannon
                            elif self.fortress == 0 and self.cannon == 1:
                                self.cannon = 0
                                self.number = number_move - int((self.number)/2)
                                self.occupant = initial.occupant

                            ## Final Node has A Fortress And A Cannon
                            elif self.fortress == 1 and self.cannon == 1:
                                if number_move > int(1.5*(self.number)):
                                    self.occupant = initial.occupant
                                    self.number = number_move - int(3*self.number/4)

                                else:
                                    self.number = self.number - int(number_move/4)
                                    self.fortress -= 1

                            ## Final Node has A Fortress But No Cannon
                            else:
                                self.fortress = 0
                                self.number = number_move - int((self.number)/2)
                                self.occupant = initial.occupant

                        self.cannon_time = -1
                        self.fortress_time = -1
                        self.allowed = self.number
        return

##Changing Troops at Initial Location
    def changetroops_ini(self , number_move , Cmove):
        self.number = self.number - number_move
        self.allowed = self.allowed - number_move
        if Cmove == True:
            self.cannon = 0

        if self.number == 0:
            self.occupancy = 0

        return

##Check Validity of Move
    def Valid_attack(self, number_move , initial , Cmove):
        if initial.allowed < number_move: ##### Less people available to send than ordered
            return 0

        if Cmove == True:
            if initial.cannon == 0:
                return -1

        if Cmove == True:
            if self.occupant == initial.occupant:
                if self.cannon == 1:
                    return -2

        if not initial.occupant == self.occupant:
            if self.number > number_move:
                return 1

        return 2

##Update Cannons and Fortresses
    def update(self):
        self.cannon_update()
        self.fortress_update()
        return

    def cannon_update(self):
        if self.cannon_time == 0:
            self.cannon_time += 1

        if self.cannon_time == cannon_ready :
            self.cannon = 1
            self.cannon_time = -1
        return

    def fortress_update(self):
        if self.fortress_time == 0:
            self.fortress_time += 1

        if self.fortress_time == fortress_ready :
            self.fortress = 1
            self.fortress_time = -1
        return

##Possible Moves By Players
def move( initial , final , move, Cmove, cannon , fortress ):
    ## Canon Build
    if cannon == 1:
        if initial.allowed < cannon_makers:  ##Cannon Fortress Successive
            return False , "Less allowed people than cannon makers"

        if not initial.cannon_time == -1:
            return False , "Already Cannon Is Being Made"

        if initial.cannon == 1:
            return False , "Already Cannon Present"

        else:
            initial.cannon_time = 0
            initial.allowed -= cannon_makers
            return True , "Cool"

    ## Fortress Build
    elif fortress == 1:
        if initial.allowed < fortress_makers:  ##Cannon Fortress Successive
            return False , "Less allowed people than fortress makers"

        if not initial.fortress_time == -1:
            return False , "Already Fortress Is Being Made"

        if initial.fortress == 1:
            return False , "Already Fortress Present"

        else:
            initial.fortress_time = 0
            initial.allowed -= fortress_makers
            return True , "cool"

    else:
        Valid_type = final.Valid_attack( move , initial , Cmove )
        if Valid_type == 0:
            print initial.allowed
            print move
            return False ,  "Less Available to send than told"

        elif Valid_type == -1:
            print "Dont have cannons can't move"
            return False , "Dont have cannons can't move"

        elif Valid_type == -2:
            return False , "Already cannon present in final place"

        else :
            final.changetroops_final(move , initial , Valid_type , Cmove)
            initial.changetroops_ini(move , Cmove)
            print final.allowed
            print initial.allowed
    return True , "Cool"




##Initiate Network
network = []

##Return array of indices of adjacent levels
def adjacent_levels (ref):
    adjacent = []
    for i in range(2*total_levels):
        if( abs(ref.level - network[i].level)) < 2:
            adjacent.append(network[i])
    return adjacent

for j in range(hq):
    network.append(node(troops4, 1 , 1 , 0 , cannon_ready , 0 , fortress_ready  , troops4, _node_ally_4[j][0],_node_ally_4[j][1]))
for j in range(level3):
    network.append(node(troops3, 1 , 2 , 0 , cannon_ready , 0 , fortress_ready  , troops3, _node_ally_3[j][0],_node_ally_3[j][1]))
for j in range(level2):
    network.append(node(troops2, 1 , 3 ,  0 , cannon_ready , 0 , fortress_ready  , troops2, _node_ally_2[j][0],_node_ally_2[j][1]))
for j in range(level1):
    network.append(node(troops1, 1 , 4 ,  0 , cannon_ready , 0 , fortress_ready  , troops1, _node_ally_1[j][0],_node_ally_1[j][1]))
for j in range(level1):
    network.append(node(troops1, -1 , 5 ,  0 , cannon_ready , 0 , fortress_ready  , troops1, _node_axis_1[j][0],_node_axis_1[j][1]))
for j in range(level2):
    network.append(node(troops2, -1 , 6 ,  0 , cannon_ready , 0 , fortress_ready  , troops2, _node_axis_2[j][0],_node_axis_2[j][1]))
for j in range(level3):
    network.append(node(troops3, -1 , 7 ,  0 , cannon_ready , 0 , fortress_ready  , troops3, _node_axis_3[j][0],_node_axis_3[j][1]))
for j in range(hq):
    network.append(node(troops4, -1 , 8 ,  0 , cannon_ready , 0 , fortress_ready  , troops4, _node_axis_4[j][0],_node_axis_4[j][1]))





