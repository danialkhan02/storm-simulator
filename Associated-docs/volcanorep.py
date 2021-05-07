import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(0, 0) # window appears left side of screen
from pygame import * # imports pygame
from colours import *
from random import * #imports random 
import math #imports math
init() #intializes pygame 
SIZE = (1000, 700)
screen = display.set_mode(SIZE) # creates screen  

class Spritevolcano(object):
    moveRight = [image.load("res/volcano1.jpg"),
                image.load("res/volcano2.jpg"),
                image.load("res/volcano3.jpg"),
                image.load("res/volcano4.jpg"),
                image.load("res/volcano5.jpg"),
                image.load("res/volcano6.jpg"),
                image.load("res/volcano7.jpg"),
                image.load("res/volcano8.jpg"),]
    
    moveLeft = [image.load("res/volcano1.jpg"),
                image.load("res/volcano2.jpg"),
                image.load("res/volcano3.jpg"),
                image.load("res/volcano4.jpg"),
                image.load("res/volcano5.jpg"),
                image.load("res/volcano6.jpg"),
                image.load("res/volcano7.jpg"),
                image.load("res/volcano8.jpg"),]
    
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
        if self.moveUnits +1 >= 12:
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

def drawScreen2():
    time.wait(30)
    Spritevolcano.draw(screen)
Spritevolcano = Spritevolcano(855, 575, 850, 575, 875)