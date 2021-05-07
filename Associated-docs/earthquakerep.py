import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(0, 0) # window appears left side of screen
from pygame import * # imports pygame
from colours import *
from random import * #imports random 
import math #imports math
init() #intializes pygame 
SIZE = (1000, 700)
screen = display.set_mode(SIZE) # creates screen  

class Spritequake(object):
    moveRight = [image.load("res/house1.png")]
                 #image.load("res/house2_edited-1.png"),
                 #image.load("res/house31.png"),
                 #image.load("res/house4_edited-1.png")]
    
    moveLeft = [image.load("res/house1.png")]
                 #image.load("res/house2_edited-1.png"),
                 #image.load("res/house31.png"),
                 #image.load("res/house4_edited-1.png")]
    
    
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.moveUnits = 0
        self.vel = 1
    
    def draw(self, screen):
        self.move()
        if self.moveUnits +1 >= 1:
            self.moveUnits = 0
        if self.vel > 0:
            screen.blit (self.moveRight[self.moveUnits//3], (self.x, self.y))
            self.moveUnits += 1
        else:
            screen.blit (self.moveLeft[self.moveUnits//3], (self.x, self.y))
            self.moveUnits += 1 

    def move(self):
        if self.vel > 0:
            if self.x < self.vel + self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.moveUnits = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.moveUnits = 0         

def drawScreen3():
    #time.wait(10)
    Spritequake.draw(screen)
Spritequake = Spritequake(835, 575, 850, 575, 840)