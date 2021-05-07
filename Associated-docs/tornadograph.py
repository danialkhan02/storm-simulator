import time
import random
import pygame
pygame.init()
def windState():
    global lastPos
    windFile = open("windspeed.txt","r")
    checkLast = windFile.readline()
    if checkLast != "":
        lastPos = checkLast
    else:
        lastPos = 38
    windFile.close() 
    windspeed = int(lastPos) + 62
    print(windspeed)
    return windspeed
def denState():
    global density
    denFile = open("DENSITY.txt","r")
    checkLast = denFile.readline()
    if checkLast != "":
        density = checkLast
    else:
        density = 2
    denFile.close() 
    print(density)
    return int(density)
def timeStateTor():
    global lastPos3
    timFile = open("torTime.txt","r")
    checkLast = timFile.readline()
    if checkLast != "":
        lastPos3 = checkLast
    else:
        lastPos3 = 169
    timFile.close()
    torntime = (int(lastPos3)-165)/7
    return int(torntime) 
SIZE = (1000, 700)
screen = pygame.display.set_mode(SIZE)
fontGraph = pygame.font.SysFont("Times New Roman", 15)
timeSpan = timeStateTor()  
diameter1 = 1000                   
diameter = diameter1/500                 
windspeed1 = windState()
windspeed  = (windspeed1)*diameter
density = denState()
startpoint1 = (790,500)
startpoint2 = (790,500)
startpoint3 = (790,210)
def procedure(state):
    if state == True:
        time.sleep(.1)
    elif state == False:
        time.sleep(0)        
potty = 1
origcounter = 0
randomvariable = random.random()   
t = (windspeed / 500)*(density)
injured = 500
deaths = 500
alive = 210
bluecounter = t
realcounter = 0
compresscounter = 0
population = 10000000             #the total population of the town
def tornadoSimulator():
    global startpoint1, poop, droughtScale, potty, origcounter, randomvariable, t, injured, deaths, bluecounter, realcounter, realcounter, origcounter, compresscounter, startpoint2, startpoint3, alive
    compresscounter += 20
    
    procedure(True)
    
    #if counter >= 10:
        #threecounter += (1)
        #counter -= 1
    #twocounter -= (1)
    #pygame.draw.circle(screen, (255,255,255), (origcounter, counter),5)
    #pygame.draw.circle(screen, (255,255,255), (origcounter, twocounter),5)
    #pygame.draw.circle(screen, (255,255,255), (origcounter, twocounter),5)
    #pygame.display.flip()
    
    
    realcounter += 1
    procedure(True)
    value =  random.randint(1,5)
    if value <= 4 and deaths + injured > 850 and potty == 1:
        bluecounter *= 1.02
        deaths -= bluecounter    
        injured  = 500 - ((500 - deaths)/3)
        
        print (500-deaths,bluecounter,500-injured)
    elif value <= 4:
        potty = 0
        bluecounter  = 2
        bluecounter *= 1.02
        deaths += 0.5*bluecounter            
        injured -= bluecounter      
    if deaths >= 500:
        deaths = 500
    
    if alive >= 500:
        alive = 500
    if injured <= 200:
        injured = 200
    alive = 210 + (500-deaths) + (500 - injured)
    
    
    
    
    
    if compresscounter % 1 == 0:    
        origcounter += 1/(timeSpan/45)
        endpoint1 = (origcounter+790, deaths)
        endpoint2 = (origcounter+790, injured)
        endpoint3 = (origcounter+790, alive)
        
        pygame.draw.line(screen, (255,255,255), (startpoint1),(endpoint1))
        pygame.draw.line(screen, (255,255,255), (startpoint2),(endpoint2))
        pygame.draw.line(screen, (255,255,255), (startpoint3),(endpoint3))
        
        
        startpoint1 = endpoint1
        startpoint2 = endpoint2
        startpoint3 = endpoint3
                
        
        
        
        #pygame.draw.rect(screen, INDIGO, (950,150,50,350))
        pygame.draw.line(screen, (255,255,255), (990,200),(990,500))
        pygame.draw.line(screen, (255,255,255), (980, 200), (1000, 200))
        pygame.draw.line(screen, (255,255,255), (980, 300), (1000, 300))
        pygame.draw.line(screen, (255,255,255), (980, 400), (1000, 400))
        pygame.draw.line(screen, (255,255,255), (980, 500), (1000, 500))
        text = fontGraph.render("%s"%population, 1, (255,255,255))
        screen.blit(text, pygame.Rect(950,200,400,100))
        text = fontGraph.render("%s"%(population*0.66), 1, (255,255,255))
        screen.blit(text, pygame.Rect(950,300,400,100))
        text = fontGraph.render("%s"%(population*0.33), 1, (255,255,255))
        screen.blit(text, pygame.Rect(950,400,400,100))
        text = fontGraph.render("0", 1, (255,255,255))
        screen.blit(text, pygame.Rect(970,485,400,100))  
        
        return deaths, injured, origcounter
        #pygame.display.flip()
#def COOR(Coordinate): # obtains coordinate
    #comma = Coordinate.find(",")
    #brack2 = Coordinate.find(")") # indentifying second bracket
    #x = Coordinate[1:comma]
    #y = Coordinate[comma + 1:brack2]
    #return float(x)
#def runner():
    #tornadoSimulator()
    ##if COOR(str(startpoint1)) >= 950:
        ##break