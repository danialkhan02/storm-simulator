import random, math
from pygame import *
from colours import *
SIZE = (1000, 700)
screen = display.set_mode(SIZE)
from tornadograph import *

def circle(colour, x, y, radius, width): # function for circle
    draw.circle(screen, colour, (x, y), radius, width)

onelist = [] # number of deaths
counter = 0 
twolist = [] # number alive
threelist = [] # number injured
startpoint = (300,200)
while True:
    counter += 1
    deaths, injured, origcounter = tornadoSimulator()
    alive = 600 - ((600 - injured) + (600 - deaths))
    onelist.append(deaths)
    twolist.append(alive)
    threelist.append(injured)
    print (origcounter,compresscounter)
    if origcounter > 100:
        print (origcounter,compresscounter)
        break

print(onelist)
print(twolist)
print(threelist)

xList = [] 
yList = []

countD = 0
countA = 0
counts = 0
#for x in range(0, 650, 8):
    #for y in range(0, 450, 17):
        #xList.append(x)
        #yList.append(y)
        #circle(colour(countD, counts, countA), x, y, 4, 0)
        #countD, counts, countA = colour(countD, counts, countA)
        #display.flip()

while True:
    choice = random.choice(["dead", "alive", "injured"])
    dead = int(onelist[counts])
    alive = int(twolist[counts])
    if choice == "dead" and countD != dead:
        countD += 1
        colour = RED
        
    elif choice == "alive" and countA != alive:
        colour = GREEN
        countA += 1
    else:
        colour = WHITE
    counts += 1    
    x = random.randint(0, 650)
    y = random.randint(0, 450)
    xList.append(x)
    yList.append(y)
    circle(colour, x, y, 4, 0)
    display.flip() 
    time.sleep(0.1)
    print(counts)
      
    if counts == 94:
        break


print(xList)
print(yList)
quit()