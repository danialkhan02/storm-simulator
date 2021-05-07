import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(0, 0) # window appears left side of screen
from pygame import * # imports pygame
from colours import *
from random import * #imports random 
from tornadograph import *
from droughtgraph import *
from volcanograph import *
from earthquakegraph import *
from visualrep import *
from volcanorep import *
from earthquakerep import *
import math #imports math
init() #intializes pygame 

MAINSTATE = 1 # defining mainstate
OPTIONSTATE = 2 # defining option state
mox = 0
moy = 0
mx = 0 # predefining mouse click
my = 0 # predefining mouse click
drag = False # sets drag for tornado as false
drag1 = False # magnitude drag
drag2 = False # Explosivity drag
drag3 = False # tornado timeline
drag4 = False # drought drag
drag5 = False # earthquake drag
drag6 = False # drought drag
drag7 = False 
simulation = False
density = 0


#Defining/functions for all shapes
def line(colour, xCoor1, yCoor1, xCoor2, yCoor2, width): # function for creating line
    draw.line(screen, colour, (xCoor1, yCoor1), (xCoor2, yCoor2), width)
def circle(colour, x, y, radius, width): # function for circle
    draw.circle(screen, colour, (x, y), radius, width)
def rect(colour, x1, y1, w, h, width): # function for creating rectangle
    draw.rect(screen, colour, (x1, y1, w, h), width)
def poly(colour, x1, y1, x2, y2, x3, y3, width):#function for creating polygon
    draw.polygon(screen, colour, [[x1, y1], [x2, y2],[x3, y3]], width) 
def mainScreen(MAINSTATE, running):

    #Main screen
    if MAINSTATE == 1:
        rect(MIDBLUE, 0, 0, 1000, 150, 0) # creates top bar
        rect(SUPERLIGHTBLUE, 0, 150, 140, 550, 0) # creates left bar where options will go
        text1 = fontB.render("CATASTROPHE", 1, BLACK)
        text2 = fontB.render("TYPE", 1, BLACK)
        screen.blit(text1, (1, 155)) 
        screen.blit(text2, (47, 177))
        screen.blit(tornado, (-12, 160))
        screen.blit(earthquake, (-16, 302))
        screen.blit(drought, (18, 475))
        screen.blit(volcano, (15, 592))
        rect(BLUEBERRY, 140, 150, 650, 450, 0) # creates middle rectangle
        #rect(INDIGO, 790, 150, 210, 350, 0) # creates rectangle for graph
        rect(SUPERLIGHTBLUE, 790, 500, 210, 200, 0) #creates rectangle for visual representation
        rect(MIDBLUE, 140, 600, 650, 100, 0)
        rect(SUPERLIGHTBLUE, 950, 0, 50, 25,0)
        line(BLACK,965,8,985,18,2)
        line(BLACK,985,8,965,18,2)
        rect(SUPERLIGHTBLUE, 160, 635, 600, 30, 0)
        line(SUPERLIGHTBLUE, 161, 600, 161, 635, 4)
        line(SUPERLIGHTBLUE, 757, 600, 757, 635, 4)
        text67 = fontB.render("TIMELINE", 1, WHITE)  
        screen.blit(text67, (400, 675))    
    return MAINSTATE, running

#All (images) options for user to choose  
def options(OPTIONSTATE, lastPos, density, simulation):
    
    #Option for tornado; User interface
    if OPTIONSTATE == 3:
        mainScreen(MAINSTATE, True) # redraws mainscreen
        rect(SUPERLIGHTBLUE, 0, 0, 125, 25, 0) # 
        text1 = fontB.render("TORNADO", 1, BLACK)
        screen.blit(text1, (15,1))     
        line(SUPERLIGHTBLUE, 35, 80, 200, 80, 10)
        line(SUPERLIGHTBLUE, 35, 60, 35, 80, 2)
        line(SUPERLIGHTBLUE, 199, 60, 199, 80, 2)
        text2 = fontB.render("%s Kilometres/Hour" %(windspeed1), 1, WHITE)
        screen.blit(text2, (38, 90))
        text3 = fontB.render("WIND SPEED", 1, WHITE)
        screen.blit(text3, (60, 120))
        text3 = fontB.render("WIND SPEED", 1, WHITE)
        screen.blit(text3, (60, 120))
        rect(GREEN, 265, 40, 100, 40, 0)
        text4 = fontB.render("START", 1, BLACK)
        screen.blit(text4, (285, 50)) 
        rect(DARKRED, 440, 40, 100, 40, 0)        
        text5 = fontB.render("RESET", 1, BLACK)
        screen.blit(text5, (460, 50))
        rect(RED, 620, 40, 100, 40, 0) 
        text6 = fontB.render("STOP", 1, BLACK)
        screen.blit(text6, (645, 50))
        rect(SUPERLIGHTBLUE, 750, 40, 80, 70, 0)
        line(BLACK, 750, 61, 830, 61, 2)
        line(BLACK, 750, 85, 830, 85, 2)
        text7 = fontB.render("HIGH", 1, BLACK)
        screen.blit(text7, (765, 42)) 
        text8 = fontB.render("MEDIUM", 1, BLACK)
        screen.blit(text8, (752, 65))         
        text9 = fontB.render("LOW", 1, BLACK)
        screen.blit(text9, (768, 88))  
        text10 = fontB.render("%.2f days" %(torntime), 1, WHITE)
        screen.blit(text10, (195, 675))        
        if startP.collidepoint(mox,moy):
            rect(BRIGHTGREEN, 265, 40, 100, 40, 0)
            screen.blit(text4, (285, 50))
        elif resetP.collidepoint(mox,moy):
            rect(RED, 441, 40, 100, 40, 0)
            screen.blit(text5, (460, 50))
        elif stopP.collidepoint(mox,moy):
            rect(DARKRED,619,40,101,40,0)
            screen.blit(text6, (645, 50))
        if highH.collidepoint(mox,moy) and simulation == False:
            rect(LIGHTGRAY, 750, 40, 80, 21, 0)
            screen.blit(text7, (765, 42))
        elif medH.collidepoint(mox,moy) and simulation == False:
            rect(LIGHTGRAY, 750, 63, 80, 21, 0)
            screen.blit(text8, (752, 65))
        elif lowH.collidepoint(mox,moy) and simulation == False:
            rect(LIGHTGRAY, 750, 87, 80, 21, 0)  
            screen.blit(text9, (768, 88))
        if highH.collidepoint(mx,my) and simulation == False:
            density = 3
            rect(WHITE, 750, 40, 80, 21, 2)
            screen.blit(text7, (765, 42))
        elif medH.collidepoint(mx,my) and simulation == False:
            density = 2
            rect(WHITE, 750, 63, 80, 21, 2)
            screen.blit(text8, (752, 65))            
        elif lowH.collidepoint(mx,my) and simulation == False:
            density = 1 
            rect(WHITE, 750, 87, 80, 21, 2)  
            screen.blit(text9, (768, 88))            
        if startP.collidepoint(mx,my):
            simulation = True
            tornadoSimulator()
        if stopP.collidepoint(mx,my):
            simulation = False
            rect(BLACK,790,150,200,350,0)
            #procedure(False)
        drawScreen()

    #Option for earthquake; User interface
    elif OPTIONSTATE == 4:
        mainScreen(MAINSTATE, True)
        rect(SUPERLIGHTBLUE, 10, 10, 10, 10, 0) 
        rect(SUPERLIGHTBLUE, 0, 0, 150, 25, 0) # 
        text1 = fontB.render("EARTHQUAKE", 1, BLACK)
        screen.blit(text1, (15,1))     
        line(SUPERLIGHTBLUE, 35, 80, 200, 80, 10)
        line(SUPERLIGHTBLUE, 35, 60, 35, 80, 2)
        line(SUPERLIGHTBLUE, 199, 60, 199, 80, 2)
        text2 = fontB.render("%.2f"%magScale, 1, WHITE)
        screen.blit(text2, (60, 90))
        text3 = fontB.render("MAGNITUDE SCALE", 1, WHITE)
        screen.blit(text3, (32, 120))
        rect(GREEN, 265, 40, 100, 40, 0)
        text4 = fontB.render("START", 1, BLACK)
        screen.blit(text4, (285, 50)) 
        rect(DARKRED, 440, 40, 100, 40, 0)        
        text5 = fontB.render("RESET", 1, BLACK)
        screen.blit(text5, (460, 50))
        rect(RED, 620, 40, 100, 40, 0) 
        text6 = fontB.render("STOP", 1, BLACK)
        screen.blit(text6, (645, 50))
        rect(SUPERLIGHTBLUE, 750, 40, 80, 65, 0)
        line(BLACK, 750, 61, 830, 61, 2)
        line(BLACK, 750, 85, 830, 85, 2)
        text7 = fontB.render("HIGH", 1, BLACK)
        screen.blit(text7, (765, 42)) 
        text8 = fontB.render("MEDIUM", 1, BLACK)
        screen.blit(text8, (752, 65))         
        text9 = fontB.render("LOW", 1, BLACK)
        screen.blit(text9, (765, 88))
        text10 = fontB.render("%.2f seconds" %(magtime), 1, WHITE)
        screen.blit(text10, (195, 675))             
        if startP.collidepoint(mox,moy):
            rect(BRIGHTGREEN, 265, 40, 100, 40, 0)
            screen.blit(text4, (285, 50))
        elif resetP.collidepoint(mox,moy):
            rect(RED, 441, 40, 100, 40, 0)
            screen.blit(text5, (460, 50))
        elif stopP.collidepoint(mox,moy):
            rect(DARKRED,619,40,101,40,0)
            screen.blit(text6, (645, 50))
        if highH.collidepoint(mox,moy) and simulation == False:
            rect(LIGHTGRAY, 750, 40, 80, 21, 0)
            screen.blit(text7, (765, 42))
        elif medH.collidepoint(mox,moy) and simulation == False:
            rect(LIGHTGRAY, 750, 63, 80, 21, 0)
            screen.blit(text8, (752, 65))
        elif lowH.collidepoint(mox,moy) and simulation == False:
            rect(LIGHTGRAY, 750, 87, 80, 21, 0)  
            screen.blit(text9, (768, 88))
        if highH.collidepoint(mx,my) and simulation == False:
            density = 3
            rect(WHITE, 750, 40, 80, 21, 2)
            screen.blit(text7, (765, 42))
        elif medH.collidepoint(mx,my) and simulation == False:
            density = 2
            rect(WHITE, 750, 63, 80, 21, 2)
            screen.blit(text8, (752, 65))            
        elif lowH.collidepoint(mx,my) and simulation == False:
            density = 1 
            rect(WHITE, 750, 87, 80, 21, 2)  
            screen.blit(text9, (768, 88))            
        if startP.collidepoint(mx,my):
            simulation = True
            earthquakeSimulator()
        if stopP.collidepoint(mx,my):
            simulation = False
            rect(BLACK,790,150,200,350,0)
            #procedure(False)
        drawScreen3()
        
    #Option for Drought; User interface    
    elif OPTIONSTATE == 5:
        mainScreen(MAINSTATE, True)
        rect(SUPERLIGHTBLUE, 10, 10, 10, 10, 0) 
        rect(SUPERLIGHTBLUE, 0, 0, 125, 25, 0) # 
        text1 = fontB.render("DROUGHT", 1, BLACK)
        screen.blit(text1, (15,1))     
        line(SUPERLIGHTBLUE, 35, 80, 200, 80, 10)
        line(SUPERLIGHTBLUE, 35, 60, 35, 80, 2)
        line(SUPERLIGHTBLUE, 199, 60, 199, 80, 2)
        text2 = fontB.render("D%.i"%drougScale, 1, WHITE)
        screen.blit(text2, (60, 90))
        text3 = fontB.render("DROUGHT LEVEL", 1, WHITE)
        screen.blit(text3, (60, 120))
        rect(GREEN, 265, 40, 100, 40, 0)
        text4 = fontB.render("START", 1, BLACK)
        screen.blit(text4, (285, 50)) 
        rect(DARKRED, 440, 40, 100, 40, 0)        
        text5 = fontB.render("RESET", 1, BLACK)
        screen.blit(text5, (460, 50))
        rect(RED, 620, 40, 100, 40, 0) 
        text6 = fontB.render("STOP", 1, BLACK)
        screen.blit(text6, (645, 50))
        rect(SUPERLIGHTBLUE, 750, 40, 80, 65, 0)
        line(BLACK, 750, 61, 830, 61, 2)
        line(BLACK, 750, 85, 830, 85, 2)
        text7 = fontB.render("HIGH", 1, BLACK)
        screen.blit(text7, (765, 42)) 
        text8 = fontB.render("MEDIUM", 1, BLACK)
        screen.blit(text8, (752, 65))         
        text9 = fontB.render("LOW", 1, BLACK)
        screen.blit(text9, (765, 88))  
        text10 = fontB.render("%.2f months" %(drougTime), 1, WHITE)
        screen.blit(text10, (195, 675))         
        if startP.collidepoint(mox,moy):
            rect(BRIGHTGREEN, 265, 40, 100, 40, 0)
            screen.blit(text4, (285, 50))
        elif resetP.collidepoint(mox,moy):
            rect(RED, 441, 40, 100, 40, 0)
            screen.blit(text5, (460, 50))
        elif stopP.collidepoint(mox,moy):
            rect(DARKRED,619,40,101,40,0)
            screen.blit(text6, (645, 50))
        if highH.collidepoint(mox,moy) and simulation == False:
            rect(LIGHTGRAY, 750, 40, 80, 21, 0)
            screen.blit(text7, (765, 42))
        elif medH.collidepoint(mox,moy) and simulation == False:
            rect(LIGHTGRAY, 750, 63, 80, 21, 0)
            screen.blit(text8, (752, 65))
        elif lowH.collidepoint(mox,moy) and simulation == False:
            rect(LIGHTGRAY, 750, 87, 80, 21, 0)  
            screen.blit(text9, (768, 88))
        if highH.collidepoint(mx,my) and simulation == False:
            density = 3
            rect(WHITE, 750, 40, 80, 21, 2)
            screen.blit(text7, (765, 42))
        elif medH.collidepoint(mx,my) and simulation == False:
            density = 2
            rect(WHITE, 750, 63, 80, 21, 2)
            screen.blit(text8, (752, 65))            
        elif lowH.collidepoint(mx,my) and simulation == False:
            density = 1 
            rect(WHITE, 750, 87, 80, 21, 2)  
            screen.blit(text9, (768, 88))            
        if startP.collidepoint(mx,my):
            simulation = True
            droughtSimulator()
        if stopP.collidepoint(mx,my):
            simulation = False
            rect(BLACK,790,150,200,350,0)
            #procedure(False)
            
    #Option for volcanic eruption; User interface
    elif OPTIONSTATE == 6:
        mainScreen(MAINSTATE, True)
        rect(SUPERLIGHTBLUE, 10, 10, 10, 10, 0) 
        rect(SUPERLIGHTBLUE, 0, 0, 125, 25, 0) # 
        text1 = fontB.render("VOLCANO", 1, BLACK)
        screen.blit(text1, (15,1))     
        line(SUPERLIGHTBLUE, 35, 80, 200, 80, 10)
        line(SUPERLIGHTBLUE, 35, 60, 35, 80, 2)
        line(SUPERLIGHTBLUE, 199, 60, 199, 80, 2)
        text2 = fontB.render("%.2f" %volScale, 1, WHITE)
        screen.blit(text2, (60, 90))
        text3 = fontB.render("Explosivity Scale", 1, WHITE)
        screen.blit(text3, (60, 120))
        rect(GREEN, 265, 40, 100, 40, 0)
        text4 = fontB.render("START", 1, BLACK)
        screen.blit(text4, (285, 50)) 
        rect(DARKRED, 440, 40, 100, 40, 0)        
        text5 = fontB.render("RESET", 1, BLACK)
        screen.blit(text5, (460, 50))
        rect(RED, 620, 40, 100, 40, 0) 
        text6 = fontB.render("STOP", 1, BLACK)
        screen.blit(text6, (645, 50))
        rect(SUPERLIGHTBLUE, 750, 40, 80, 65, 0)
        line(BLACK, 750, 61, 830, 61, 2)
        line(BLACK, 750, 85, 830, 85, 2)
        text7 = fontB.render("HIGH", 1, BLACK)
        screen.blit(text7, (765, 42)) 
        text8 = fontB.render("MEDIUM", 1, BLACK)
        screen.blit(text8, (752, 65))         
        text9 = fontB.render("LOW", 1, BLACK)
        screen.blit(text9, (765, 88))         
        if startP.collidepoint(mox,moy):
            rect(BRIGHTGREEN, 265, 40, 100, 40, 0)
            screen.blit(text4, (285, 50))
        elif resetP.collidepoint(mox,moy):
            rect(RED, 441, 40, 100, 40, 0)
            screen.blit(text5, (460, 50))
        elif stopP.collidepoint(mox,moy):
            rect(DARKRED,619,40,101,40,0)
            screen.blit(text6, (645, 50))
        if highH.collidepoint(mox,moy) and simulation == False:
            rect(LIGHTGRAY, 750, 40, 80, 21, 0)
            screen.blit(text7, (765, 42))
        elif medH.collidepoint(mox,moy) and simulation == False:
            rect(LIGHTGRAY, 750, 63, 80, 21, 0)
            screen.blit(text8, (752, 65))
        elif lowH.collidepoint(mox,moy) and simulation == False:
            rect(LIGHTGRAY, 750, 87, 80, 21, 0)  
            screen.blit(text9, (768, 88))
        if highH.collidepoint(mx,my) and simulation == False:
            density = 3
            rect(WHITE, 750, 40, 80, 21, 2)
            screen.blit(text7, (765, 42))
        elif medH.collidepoint(mx,my) and simulation == False:
            density = 2
            rect(WHITE, 750, 63, 80, 21, 2)
            screen.blit(text8, (752, 65))            
        elif lowH.collidepoint(mx,my) and simulation == False:
            density = 1 
            rect(WHITE, 750, 87, 80, 21, 2)  
            screen.blit(text9, (768, 88))            
        if startP.collidepoint(mx,my):
            simulation = True
            volcanoSimulator()
        if stopP.collidepoint(mx,my):
            simulation = False
            rect(BLACK,790,150,200,350,0)
            #procedure(False)
        drawScreen2()
    return density, simulation

#Checks if user presses on any of the collide points, then draws screen
def checkPress(OPTIONSTATE):
    if tornIcon.collidepoint(mx, my):
        OPTIONSTATE = 3
        drawScreen()
    elif earthIcon.collidepoint(mx, my):
        OPTIONSTATE = 4
        if OPTIONSTATE == 4:
            drawScreen3()
    elif drotIcon.collidepoint(mx, my):
        OPTIONSTATE = 5
    elif volIcon.collidepoint(mx, my):
        OPTIONSTATE = 6
    return OPTIONSTATE

#Mouse over function for highlights
def mousOver():
    if tornIcon.collidepoint(mox, moy):
        rect(BLACK, 0, 195, 140, 140,2) 
    elif earthIcon.collidepoint(mox, moy):
        rect(BLACK, 0, 337, 140, 130, 2) 
    elif drotIcon.collidepoint(mox, moy):
        rect(BLACK, 0, 468, 140, 112, 2) 
    elif volIcon.collidepoint(mox, moy):
        rect(BLACK, 0, 578, 140, 122, 2)

#Checks last position for wind speeds
def windState():
    global lastPos
    windFile = open("windspeed.txt","r")
    checkLast = windFile.readline()
    if checkLast != "":
        lastPos = checkLast
    else:
        lastPos = 38
    windFile.close() 
    return int(lastPos)

#Checks last position for earthquake magnitude
def earthState():
    global lastPos1
    earthFile = open("magnitudeScale.txt","r")
    checkLast = earthFile.readline()
    if checkLast != "":
        lastPos1 = checkLast
    else:
        lastPos1 = 38
    earthFile.close() 
    return int(lastPos1) 

#Checks last position for volcanic explosivity scale
def volState():
    global lastPos2
    explodeFile = open("explodeScale.txt","r")
    checkLast = explodeFile.readline()
    if checkLast != "":
        lastPos2 = checkLast
    else:
        lastPos2 = 38
    explodeFile.close() 
    return int(lastPos2) 

#Checks last position for drought level (scale)
def droughtState():
    global lastPos4
    droughtFile = open("droughtScale.txt","r")
    checkLast = droughtFile.readline()
    if checkLast != "":
        lastPos4 = checkLast
    else:
        lastPos4 = 38
    droughtFile.close() 
    return int(lastPos4)

#Checks last position of time state for tornado
def timeStateTor():
    global lastPos3
    timFile = open("torTime.txt","r")
    checkLast = timFile.readline()
    if checkLast != "":
        lastPos3 = checkLast
    else:
        lastPos3 = 169
    timFile.close() 
    return int(lastPos3) 

#Checks last position of time state for earthquake
def timeStateEarth():
    global lastPos5
    timFile = open("earthTime.txt","r")
    checkLast = timFile.readline()
    if checkLast != "":
        lastPos5 = checkLast
    else:
        lastPos5 = 169
    timFile.close() 
    return int(lastPos5)

#Checks last position of time state for drought
def timeStateDroug():
    global lastPos6
    timFile = open("droughtTime.txt","r")
    checkLast = timFile.readline()
    if checkLast != "":
        lastPos6 = checkLast
    else:
        lastPos6 = 169
    timFile.close() 
    return int(lastPos6) 

#Checks last position of time state for volcano
#def timeStateVol():
    #global lastPos6
    #timFile = open("volcanotxt.txt","r")
    #checkLast = timFile.readline()
    #if checkLast != "":
        #lastPos7 = checkLast
    #else:
        #lastPos7 = 169
    #timFile.close() 
    #return int(lastPos7) 

# grabs fonts, pictures
fontA = font.Font("Modern.otf", 55)
fontB = font.Font("Modern.otf", 20)
tornado = image.load("tornado.png")
earthquake = image.load("earthquake.png")
drought = image.load("drought.png")
volcano = image.load("volcano.png")

#Icons, start, reset, stop, high,medium,low, and xButton parameters
tornIcon = Rect(-12, 160, tornado.get_width(), tornado.get_height()) # defining collision point for the tornado icon
earthIcon = Rect(-16, 302, earthquake.get_width(), earthquake.get_height()) # defining collision point for the earthquake icon
drotIcon = Rect(18, 475, drought.get_width(), drought.get_height()) # defining collision point for the droiught icon
volIcon = Rect(15, 592, volcano.get_width(), volcano.get_height()) # defining collision point for the droiught icon
dragPar = Rect(35, 60, 199, 15)
startP = Rect(265, 40, 100, 40)
resetP = Rect(441, 40, 100, 40)
stopP = Rect(619,40,100,40)
highH = Rect (750,40,80,20)
medH = Rect (750,63,80,20)
lowH = Rect (750,87,80,20)
timeL = Rect(165,600,600,30)
xButton= Rect(950, 0, 50, 25)

#lastPos = 38
SIZE = (1000, 700) # sets screen size
screen = display.set_mode(SIZE) # creates screen  

running = True # sets the loop state as True


#Mouse interface and buttons
while running:
    button = 0 # setting button as 0
    for evnt in event.get(): # checking all events
        if evnt.type==QUIT: # checking if event is QUIT
            running = False
        if evnt.type == MOUSEBUTTONDOWN: # checks if event is mouse button down
            mx, my = evnt.pos     #if true, mouse position is given
            print(mx, my)
            button = evnt.button   # button is recorded
        if evnt.type == MOUSEMOTION: # checks for events with mouse motion
            mox, moy = evnt.pos # if true, mouse position is given
        if evnt.type == MOUSEBUTTONUP:
            mux, muy = evnt.pos
    if xButton.collidepoint(mox,moy):
        rect(BRIGHTRED,950, 0, 50, 25, 0)
    elif xButton.collidepoint(mx,my):
        running = False    
    MAINSTATE, running = mainScreen(MAINSTATE, running) # draws the interface for the main state
    textU = fontA.render("CATASTROPHE SIMULATOR V1.0", 1, SUPERLIGHTBLUE)
    screen.blit(textU, (50, 30))    # creates title
    OPTIONSTATE = checkPress(OPTIONSTATE) # checks if any of the options were clicked
    lastPos = windState()
    lastPos1 = earthState()
    lastPos2 = volState()
    lastPos3 = timeStateTor()
    lastPos4 = droughtState()
    lastPos5 = timeStateEarth()
    lastPos6 = timeStateDroug()
    
    #Creates the choices for each catastrophe chosen
    density, simulation = options(OPTIONSTATE, lastPos, density, simulation)
    if OPTIONSTATE == 3 and simulation == False:
        if dragPar.collidepoint(mx, my) and button == 1:
            drag = True  
        if drag == True:
            if mox <= 38 or mox >= 190:
                drag = False
            else:
                lastPos = mox            
            rect(BLUEBERRY, lastPos, 60, 10, 15, 0)
            if evnt.type == MOUSEBUTTONUP:
                lastPos = mux
                drag = False
        if OPTIONSTATE == 3 and drag == False:
            rect(BLUEBERRY, lastPos, 60, 10, 15, 0)       
    if OPTIONSTATE == 4 and simulation == False:
        if dragPar.collidepoint(mx, my) and button == 1:
            drag1 = True  
        if drag1 == True:
            if mox <= 38 or mox >= 190:
                drag1 = False
            else:
                lastPos1 = mox            
            rect(BLUEBERRY, lastPos1, 60, 10, 15, 0)
            if evnt.type == MOUSEBUTTONUP:
                lastPos1 = mux
                drag1 = False
        elif OPTIONSTATE == 4 and drag1 == False:
            rect(BLUEBERRY, lastPos1, 60, 10, 15, 0)    
    if OPTIONSTATE == 6 and simulation == False :
        if dragPar.collidepoint(mx, my) and button == 1:
            drag2 = True  
        elif drag2 == True:
            if mox <= 38 or mox >= 190:
                drag2 = False
            else:
                lastPos2 = mox            
            rect(BLUEBERRY, lastPos2, 60, 10, 15, 0)
            if evnt.type == MOUSEBUTTONUP:
                lastPos2 = mux
                drag2 = False
        elif OPTIONSTATE == 6 and drag2 == False:
            rect(BLUEBERRY, lastPos2, 60, 10, 15, 0)
    if OPTIONSTATE == 5 and simulation == False :
        if dragPar.collidepoint(mx, my) and button == 1:
            drag4 = True  
        elif drag4 == True:
            if mox <= 38 or mox >= 190:
                drag4 = False
            else:
                lastPos4 = mox            
            rect(BLUEBERRY, lastPos4, 60, 10, 15, 0)
            if evnt.type == MOUSEBUTTONUP:
                lastPos4 = mux
                drag4 = False
        elif OPTIONSTATE == 5 and drag4 == False:
            rect(BLUEBERRY, lastPos4, 60, 10, 15, 0)    
    if OPTIONSTATE == 3 and simulation == False:
        if timeL.collidepoint(mx, my) and button == 1:
            drag3 = True  
        if drag3 == True:
            if mox <= 163 or mox >= 743:
                drag3 = False
            else:
                lastPos3 = mox            
            rect(BLUEBERRY, lastPos3, 605, 20, 30, 0)
            if evnt.type == MOUSEBUTTONUP:
                lastPos3 = mux
                drag3 = False
        if OPTIONSTATE == 3 and drag3 == False:
            rect(BLUEBERRY, lastPos3, 605, 20, 30, 0) 
    if OPTIONSTATE == 4 and simulation == False:
        if timeL.collidepoint(mx, my) and button == 1:
            drag5 = True  
        if drag5 == True:
            if mox <= 163 or mox >= 743:
                drag5 = False
            else:
                lastPos5 = mox            
            rect(BLUEBERRY, lastPos5, 605, 20, 30, 0)
            if evnt.type == MOUSEBUTTONUP:
                lastPos5 = mux
                drag5 = False
        if OPTIONSTATE == 4 and drag5 == False:
            rect(BLUEBERRY, lastPos5, 605, 20, 30, 0)  
    if OPTIONSTATE == 5 and simulation == False:
        if timeL.collidepoint(mx, my) and button == 1:
            drag6 = True  
        if drag6 == True:
            if mox <= 163 or mox >= 743:
                drag6 = False
            else:
                lastPos6 = mox            
            rect(BLUEBERRY, lastPos6, 605, 20, 30, 0)
            if evnt.type == MOUSEBUTTONUP:
                lastPos6 = mux
                drag6 = False
        if OPTIONSTATE == 5 and drag6 == False:
            rect(BLUEBERRY, lastPos6, 605, 20, 30, 0)     
   
    #Density file.txt
    if density == 1 or density == 2 or density == 3:
        denFile = open("DENSITY.txt", "w")
        denFile.write(str(density))
        denFile.close()
        
    windspeed1 = lastPos + 62 #windspeed scale and last position
    magScale = (lastPos1 + 200)/42 #magnitude scale and last position
    volScale = (lastPos2 + 200)/42 #explosivity scale and last position
    drougScale = (lastPos4)/40.5 #drought scale and last position
    torntime = (lastPos3-165)/7 #tornado time ellapsed and last position
    magtime = (lastPos5-165)/21 #earthquake time ellapsed and last position
    drougTime = (lastPos6-165)/53 #drought time ellapsed and last position
    #voltime = (lastPos7-165)/? #volcano time ellapsed and last position
    
    #Write in file at last position for windspeed
    wind1File = open("windspeed.txt","w")
    wind1File.write(str(lastPos))
    wind1File.close()  
    
     #Write in file at last position for the magnitude scale
    earth1File = open("magnitudeScale.txt","w")
    earth1File.write(str(lastPos1))
    earth1File.close()  
    
     #Write in file at last position for the explosivity scale
    explodeFile = open("explodeScale.txt","w")
    explodeFile.write(str(lastPos2))
    explodeFile.close()  
    
     #Write in file at last position for the drought level scale
    droughtFile = open("droughtScale.txt","w")
    droughtFile.write(str(lastPos4))
    droughtFile.close()  
    
     #Write in file at last position for tornado time ellapsed
    timeFile = open("torTime.txt","w")
    timeFile.write(str(lastPos3))
    timeFile.close() 
    
     #Write in file at last position for earthquake time ellapsed
    time1File = open("earthTime.txt","w")
    time1File.write(str(lastPos5))
    time1File.close()  
    
     #Write in file at last position for drought's time ellapsed
    time2File = open("droughtTime.txt","w")
    time2File.write(str(lastPos6))
    time2File.close()  
    
    # mouse over function for the catastrophe type
    mousOver() 
    
    #Draws everything (without this 1 command... EVERYTHING IS USELESS)
    display.update()


quit() # quit python