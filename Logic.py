from random import randint
from math import *
##DEFINE Levels
level1 = 5
level2 = 3
level3 = 1
hq = 0

total_levels = level1 + level2 + level3 + hq

# Axis- RED #################
paris = "Paris had been ruled by Nazi Germany since the signing of the Second Compigne Armistice on 22 June 1940. It was one of the largest cities in Europe at that time and thus was a major centre for the Nazis. The Liberation of Paris was a military combat that took place during World War II from 19 August 1944 until the German garrison surrendered the French capital."
paris1="img/paris.jpg"
kiev="Kiev-The First Battle of Kiev was the German name for the operation that resulted in a very large encirclement of Soviet troops in the vicinity of Kiev. This encirclement is considered the largest encirclement in the history of warfare. Kiev then became a major victory for Germany."
kiev1="img/kiev.jpg"
minsk = "Minsk- The Battle of Bialystok\nMinsk was a German strategic operation and aimed at the encirclement and destruction of the Red Armys Western Front forces around Minsk in 1941. All major Soviet counter-attacks and break-through attempts failed. Some believed the Germans had effectively won the war against the Soviet Union already."
minsk1 = "img/minsk.jpg"
crete="YO BC"
#crete = "Crete-On 20 May 1941, German paratroopers were dropped over the airfields of northern Crete to occupy the island. They were met by heavy resistance from Allied forces and the local Cretan population but eventually the defenders were overwhelmed by the tactically superior German forces. The British Government ordered an evacuation on 27 May and the remaining forces surrendered on 1 June."
crete1 = "img/crete.jpg"
belgrade = "Belgrade-Belgrade was the capital of the Kingdom of Yugoslavia. Operation Punishment, was the codename used for the April 1941 German bombing of Belgrade which paralysed communications between the Yugoslav military and its headquarters, and contributed decisively to the rapid collapse of Yugoslav resistance resulting in around 24,000 casualties."
belgrade1 = "img/belgrade.jpg"

hamburg= "Hamburg-The city was an important port and industrial center and the site of major German shipyards and U-boat pens. The most severe bombing raid on the city came from a combined force of British and American bombers which left 42,600 dead and 37,000 wounded."
hamburg1= "img/hamburg.jpg"
dresden= "Dresden-Dresden, Germany's seventh biggest city and an extremely important industrial centre, experienced one of the most severe bombing campaigns. Fifteen square miles of the city center were utterly destroyed by the devastating firestorm that swept through the streets killing around 25,000."
dresden1="img/dresden.jpg"
warsaw="Warsaw-Captured hours after the withdrawal of German troops, in violation of Hitlers order to hold the Fortress.  During the course of the war approximately 84% of the city was destroyed due to German and Soviet mass bombings, heavy artillery fire and a planned demolition campaign."
warsaw1="img/warsaw.jpg"

berlin="Berlin-The German capital was one of the focal points of the war and was the most important stronghold of the Nazis during the war. It endured a prolonged period of strategic bombing that lasted for almost the entire duration of the war. In total, Berlin was the target of 363 air raids from the airplanes of the British, the Americans and the Soviets."
berlin1="img/berlin.jpg"

#LEVEL-1

_node_axis_1 = [(217, 378,paris ,paris1),
        (500,400,kiev,kiev1),
        (484,296,minsk,minsk1),
        (427,575,crete,crete1),
        (405,458,belgrade,belgrade1)]



#LEVEL-2
_node_axis_2 = [(297,309,hamburg,hamburg1),
            (320,404,dresden,dresden1),
            (403,333,warsaw,warsaw1)]



#LEVEL-3

_node_axis_3 = [(334,346,berlin,berlin1)]



#LEVEL-4

##_node_axis_4 = [(373,393)]

############################


# Allies- GREEN #############

#LEVEL-1
coventry="Coventry-Coventry was an industrial city and contained major metal-working industries.The city was bombed many times during the Second World War by the German Air Force-Luftwaffe. The most devastating of these attacks occurred on the evening of 14 November 1940."
coventry1="img/coventry.jpg"
london="London- The capital of the United Kingdom was subjected to a sustained strategic bombing campaign carried out by the German Luftwaffe that is said to have lasted for 76 consecutive nights and was directly responsible for the deaths of 20,000 people. Britain's resolve and unwillingness to succumb to the Germans helped changed the course of the war for the Allied fight back."
london1="img/london.jpg"
murmansk="Murmansk-The city of Murmansk was a strategically important sea port and industrial city. It was the only Soviet port on the northern coast that did not freeze in the winter, and was vital for the transport of supplies to the South. More than 180,000 grenades and inflammable shells were fired on the city. Fierce Soviet resistance in the tundra and several Soviet counter-attacks made an Axis breakthrough impossible."
murmansk1="img/murmansk.jpg"
barcelona="Barcelona-Germany and Italy aided General Francisco Franco with an abundance of planes, tanks, and arms to attack Catalonia, while the Soviet Union aided the Republican side to help defend Barcelona. In January 1939, the Catalonian capital, Barcelona, was captured, and soon after the rest of Catalonia fell. The most significant contribution of these foreign units was the successful defense of Madrid until the end of the war."
barcelona1="img/barcelona.jpg"
novo="Novorossiysk-The city of Novorossiysk on the eastern coast of the Black Sea provided a stronghold against the German summer offensive of 1942. Intense fighting in and around the city lasted from August until it was captured by the Germans in mid-September 1942. The Soviets however retained possession of the eastern part of the bay, which prevented the Germans from using the port for supply shipments."
novo1="img/novorossiysk.jpg"
_node_ally_1 = [(178,251,coventry,coventry1),
        (200,314,london,london1),
        (461,83,murmansk,murmansk1),
        (159,486,barcelona,barcelona1),
        (618,431,novo,novo1)]



#LEVEL-2
brest="Brest- It was located right on the border between the Soviet Union and Nazi Germany.  The Brest garrison, although cut off from the outside world and having run out of food, water and ammunition, fought and counter-attacked until the very last minute. The Germans deployed tanks, tear gas and flame throwers and ruined fortifications causing heavy casualties."
stalin="Stalingrad- The Battle of Stalingrad is often regarded as the single largest and bloodiest battle in the history of warfare.  The attack was supported by intensive Luftwaffe bombing that reduced much of the city to rubble. It is considered to be turning point of World War II."
lenin="Leningrad- The Leningrad Blockade was a prolonged military blockade undertaken by the German Army Group against Leningrad, currently known as Saint Petersburg, in the Eastern Front theatre of World War II. The political status of Leningrad as the former capital of Russia and the symbolic capital of the Russian Revolution, its military importance as a main base of the Soviet Baltic Fleet and its industrial strength, housing numerous arms factories."
brest1="img/brest.jpg"
stalin1="img/stalingrad.jpg"
lenin1="img/leningrad.jpg"

_node_ally_2 = [(531,317,brest,brest1),
        (670,338,stalin,stalin1),
        (511,210, lenin ,lenin1)]


moscow = "Moscow-The Soviet capital was one of the most important city for the Allies during the war. Joseph Stalin led the Soviet Union during World War II and he operated primarily from Moscow. Moscow was one of the primary military and political objectives for Axis forces in their invasion of the Soviet Union. The German-Operation Typhoon, was planned to conduct two pincer offensives on Moscow in which 35,757 were killed."
moscow1 = "img/moscow.jpg"
#LEVEL-3

_node_ally_3 = [(600,240,moscow,moscow1)]



#LEVEL-4

##_node_ally_4 = [(643,221)]

#############################

##Define Troops at each level
troops1 = 100
troops2 = 300
troops3 = 500
##troops4 = 100

cannon_ready = 7
fortress_ready = 9

cannon_makers = 100
fortress_makers = 100

class node:
    def __init__(self , number , occupant , level, cannon, cannon_time, fortress, fortress_time, allowed, x, y , text , image):
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
        self.text = text
        self.image = image
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
                                if number_move > int(1.5*self.number):
                                    self.occupant = initial.occupant
                                    self.number = number_move - int(.75*self.number)

                                else:
                                    self.number -= int(number_move/4)
                                    self.cannon = 0

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

                                elif number_move < int(1.5*self.number):
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
##                        self.number = int(self.number/2)
##                        x = (randint(0,9))
##                        print x
##                        if x < 5:
##                            self.occupant = initial.occupant
                        if Cmove == False:
                            if self.cannon == 0 and self.fortress == 0:
                                self.number = int(self.number/2)
                                x = (randint(0,9))
                                print x
                                if x < 5:
                                    self.occupant = initial.occupant

                            elif self.cannon == 1 and self.fortress == 0:
                                self.number = int(0.75*self.number)

                        else:
                            if self.cannon == 0 and self.fortress == 0:
                                self.occupant = initial.occupant
                                self.number = int(0.75*self.number)

                            elif self.cannon == 1 and self.fortress == 0:
                                self.cannon = 0
                                self.number = int(self.number/2)
                                x = (randint(0,9))
                                print x
                                if x < 5:
                                    self.occupant = initial.occupant

                            elif self.cannon == 0 and self.fortress == 1:
                                self.fortress = 0
                                self.number = int(self.number/2)
                                x = (randint(0,9))
                                print x
                                if x < 5:
                                    self.occupant = initial.occupant

                            elif self.cannon == 1 and self.fortress == 1:
                                self.cannon = 0







                    self.allowed = self.number


            ## Either cannon or fortress being made
            elif (self.cannon_time == -1) != (self.fortress_time == -1):
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
                        self.cannon_time = -1
                        self.fortress_time = -1
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
                    self.cannon = 0
                    self.fortress = 0
                    self.cannon_time = -1
                    self.fortress_time = -1

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
                        self.cannon_time = -1
                        self.fortress_time = -1

                        ## Cannon not moved from Initial Node
                        if Cmove == False :

                            ## Final Node has No Fortress and No Cannon
                            if self.fortress == 0 and self.cannon == 0:
                                self.number = number_move - int((self.number)/2)
                                self.occupant = initial.occupant

                            ## Final Node has No Fortress But A Cannon
                            elif self.fortress == 0 and self.cannon == 1:
                                self.cannon == 0
                                if number_move > int(1.5*self.number):
                                    self.occupant = initial.occupant
                                    self.number = number_move - int(.75*self.number)

                                else:
                                    self.number -= int(number_move/4)
                                    self.cannon = 0

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

                                elif number_move < int(1.5*self.number):
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
                        self.cannon_time = -1
                        self.fortress_time = -1
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
                    self.cannon = 0
                    self.fortress = 0
                    self.cannon_time = -1
                    self.fortress_time = -1

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
                        self.cannon_time = -1
                        self.fortress_time = -1

                        ## Cannon not moved from Initial Node
                        if Cmove == False :

                            ## Final Node has No Fortress and No Cannon
                            if self.fortress == 0 and self.cannon == 0:
                                self.number = number_move - int((self.number)/2)
                                self.occupant = initial.occupant

                            ## Final Node has No Fortress But A Cannon
                            elif self.fortress == 0 and self.cannon == 1:
                                self.cannon == 0
                                if number_move > int(1.5*self.number):
                                    self.occupant = initial.occupant
                                    self.number = number_move - int(.75*self.number)

                                else:
                                    self.number -= int(number_move/4)
                                    self.cannon = 0

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

                                elif number_move < int(1.5*self.number):
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
            self.occupant = 0

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

        if Cmove == True:
            if initial.allowed == 0 :
                return -3

        if number_move == 0:
            return -4

        if not initial.occupant == self.occupant:
            if self.number > number_move:
                return 1

            if self.number == number_move:
                return 3
        return 2

##Update Cannons and Fortresses
    def update(self):
        self.cannon_update()
        self.fortress_update()
        return

    def cannon_update(self):
        if self.cannon_time > -1:
            print "update ho raha hai cannon bc"
            print self.level
            self.cannon_time += 1
            print self.cannon_time

        if self.cannon_time == cannon_ready :
            self.cannon = 1
            self.cannon_time = -1
            self.allowed = self.allowed + cannon_makers
            print  "Cannon ready bc"
            print self.level
        return

    def fortress_update(self):
        if self.fortress_time > -1:
            print "fortress update ho raha hai"
            self.fortress_time += 1
            print self.fortress_time

        if self.fortress_time == fortress_ready :
            self.fortress = 1
            self.fortress_time = -1
            self.allowed = self.allowed + fortress_makers
            print "fortress ready bc"
        return

##Possible Moves By Players
def move( initial , final , move, Cmove, cannon , fortress ):
    ## Canon Build
    if cannon == 1:
        if initial.level == 2 or initial.level == 7:
            return False , " Sorry, Cant Build cannon or fortress at headquarters"

        if initial.allowed < cannon_makers:  ##Cannon Fortress Successive
            return False , "Less allowed people than cannon makers"

        if not initial.cannon_time == -1:
            return False , "Already Cannon Is Being Made"

        if initial.cannon == 1:
            return False , "Already Cannon Present"

        else:
            print "Cannon banane baith gaye bc"
            initial.cannon_time = 0
            initial.allowed -= cannon_makers
            return True , "Cool"

    ## Fortress Build
    elif fortress == 1:

        if initial.level == 2 or initial.level == 7:
            return False , " Sorry, Cant Build cannon or fortress at headquarters"

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
            return False , "Less Available to send than told"

        elif Valid_type == -1:
            print "Dont have cannons can't move"
            return False , "Dont have cannons can't move"

        elif Valid_type == -2:
            return False , "Already cannon present in final place"

        elif Valid_type == -3:
            if initial.number == 0:
                return False , "No troops there to move cannon"
            if initial.allowed == 0:
                return False , "No troops there to move cannon , others making fortress"

        elif Valid_type == -4 :
            return False , "Input Some Troops Please"

        else :
            if Cmove == True:
##                print "Moving Cannon BC"
                pass
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

##for j in range(hq):
##    network.append(node(troops4, 1 , 1 , 0 , cannon_ready , 0 , fortress_ready  , troops4, _node_ally_4[j][0],_node_ally_4[j][1]))
for j in range(level3):
    network.append(node(troops3, 1 , 2 , 0 , cannon_ready , 0 , fortress_ready  , troops3, _node_ally_3[j][0],_node_ally_3[j][1] ,_node_ally_3[j][2],_node_ally_3[j][3]))
for j in range(level2):
    network.append(node(troops2, 1 , 3 ,  0 , cannon_ready , 0 , fortress_ready  , troops2, _node_ally_2[j][0],_node_ally_2[j][1],_node_ally_2[j][2],_node_ally_2[j][3]))
for j in range(level1):
    network.append(node(troops1, 1 , 4 ,  0 , cannon_ready , 0 , fortress_ready  , troops1, _node_ally_1[j][0],_node_ally_1[j][1],_node_ally_1[j][2],_node_ally_1[j][3]))
for j in range(level1):
    network.append(node(troops1, -1 , 5 ,  0 , cannon_ready , 0 , fortress_ready  , troops1, _node_axis_1[j][0],_node_axis_1[j][1],_node_axis_1[j][2],_node_axis_1[j][3]))
for j in range(level2):
    network.append(node(troops2, -1 , 6 ,  0 , cannon_ready , 0 , fortress_ready  , troops2, _node_axis_2[j][0],_node_axis_2[j][1],_node_axis_2[j][2],_node_axis_2[j][3]))
for j in range(level3):
    network.append(node(troops3, -1 , 7 ,  0 , cannon_ready , 0 , fortress_ready  , troops3, _node_axis_3[j][0],_node_axis_3[j][1],_node_axis_3[j][2],_node_axis_3[j][3]))







