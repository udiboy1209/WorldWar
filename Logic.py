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
        if initial.occupant == self.occupant :
            self.number = number_move + self.number
            if CMove == True :
                self.cannon += 1
                initial.canon -= 1
        elif valid == 1:
            if Cmove == False :
                if self.fortress == 0:
                    self.number = number_move + self.number - 2*int((self.number)/10)
                else:
                    print "Change"#############################

            else :
                if self.fortress == 0:
                    print "Change"##Cannon moved and no fortress

                else:
                    print "Change"##Cannon moved and fortress

        elif valid == 2:
            if Cmove == False :
                if self.fortress == 0:
                    self.number = number_move + self.number - 2*int((self.number)/10)
                    self.occupant = initital.occupant

                else:
                    print "Change"##############################

            else:
                if self.fortress == 0:
                    self.occupant = initial.occupant
                 ####################### Cannon Moved and No Fowindow_wrtress

                else:
                    print "channnge"##################################### Cannon Moved and Fortress
        return

##Changing Troops at Initial Location
    def changetroops_ini(self , number_move , Cmove):
        self.number = self.number - number_move
        self.allowed = self.allowed - number_move
        if Cmove == True:
            self.cannon -= 1

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
            return False
        else:
            initial.cannon_time = 0
            initial.allowed -= cannon_makers
            return True

    ## Fortress Build
    elif fortress == 1:
        if initial.allowed < fortress_makers:  ##Cannon Fortress Successive
            return False
        else:
            initial.cannon_time = 0
            initial.allowed -= fortress_makers
            return True


    else:
        Valid_type = final.Valid_attack( move , initial , Cmove )
        if Valid_type == 0:
            print "Less Available to send than told"
            return False

        elif Valid_type == -1:
            print "Dont have cannons can't move"
            return False

        else :
            final.changetroops_final(move , initial.occupant , Valid_type)


##Return array of indices of adjacent levels
def adjacent_levels ( ref , network):
    adjacent = []
    for i in range(2*total_levels):
        if( abs(ref.level - network[i].level)) < 2:
            adjacent.append(i)
    return adjacent

##Initiate Network
network = []
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


