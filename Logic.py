from math import *
##DEFINE Levels 
level1 = 10 
level2 = 6
level3 = 3
hq = 1

total_levels = level1 + level2 + level3 + hq

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
    def __init__(self , number , occupant , level, cannon, cannon_time, fortress, fortress_time, allowed):
        self.number = number
        self.occupant = occupant
        self.level = level
        self.cannon = 0
        self.fortress = 0
        self.cannon_time = -1
        self.fortress_time = -1
        self.allowed = number
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
                 ####################### Cannon Moved and No Fortress

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
    network.append(node(troops4, 1 , 1 , 0 , cannon_ready , 0 , fortress_ready  , troops4))
for l in range(level3):
    network.append(node(troops3, 1 , 2 , 0 , cannon_ready , 0 , fortress_ready  , troops3))
for j in range(level2):
    network.append(node(troops2, 1 , 3 ,  0 , cannon_ready , 0 , fortress_ready  , troops2))
for j in range(level1):
    network.append(node(troops1, 1 , 4 ,  0 , cannon_ready , 0 , fortress_ready  , troops1))
for j in range(level1):
    network.append(node(troops1, -1 , 5 ,  0 , cannon_ready , 0 , fortress_ready  , troops1))                   
for j in range(level2):
    network.append(node(troops2, -1 , 6 ,  0 , cannon_ready , 0 , fortress_ready  , troops2))
for j in range(level3):
    network.append(node(troops3, -1 , 7 ,  0 , cannon_ready , 0 , fortress_ready  , troops3))
for j in range(hq):
    network.append(node(troops4, -1 , 8 ,  0 , cannon_ready , 0 , fortress_ready  , troops4))

print network[22].level


