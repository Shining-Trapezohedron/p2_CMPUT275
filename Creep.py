import pygame
import sys
import pyganim
from pygame.locals import *
import time
from random import randint
from random import random

right = 'right'
left = 'left'
class Creep():
    def __init__(
        self, screen, filename, pos, direction, speed, fish_height, fish_width):
        self.filename = "fishdish/" + str(filename)
        '''
        Creep Object
        Screen: A pygame screen (pygame.display)
        filename (image for the creep)
        init_pos: A tuple containing (x,y)
        init_dir: A 2d vector of the creep
        speed: creep speed in pixel/millisecond
        '''
        self.screen = screen
        self.f_h = fish_height
        self.f_w = fish_width
        self.f_x = pos[0]
        self.f_y = pos[1]
        self.f_dir = direction 
        self.f_rate = speed
        self.AObjs = {} 
        
        right_facing = []
        left_facing = []
        for i in range(5):
            right_facing.append( (self.filename + "_right_" +str(i+1) + '.png' , 0.1 ))
            left_facing.append( (self.filename+ "_left_" + str(i+1) + '.png' ,0.1))
        #print(right_facing)
        right_facing = pyganim.PygAnimation(right_facing)
        left_facing = pyganim.PygAnimation(left_facing)

        self.AObjs['left_facing'] = left_facing
        self. AObjs['right_facing'] = right_facing
        moveCond = pyganim.PygConductor(self.AObjs)

        self.d = right
        moveCond.play()

    def update(self):
        screenw, screenh  = self.screen.get_size()
        #print(screenw,screenh)
        for i in range(4):
            self.move_right()
            self.move_up()
        if self.f_y >= screenw + self.f_h or self.f_x >= screenh + self.f_w:
            print(self.filename)
    
    def stationary_fish_movements(self, percent):
        #takes a percent chance (0, %100) of blinking while stationary
        if (randint(0,100) > (100-percent)): # because we want to the eye blinking every few seconds 
        # not at every iteration of the loop
            if self.d == right:
                self.AObjs['right_facing'].blit(self.screen, (self.f_x, self.f_y))
            
            if self.d == left:
                self.AObjs['left_facing'].blit(self.screen, (self.f_x, self.f_y))
    def move_right(self):
        self.d = right
        #self.screen.fill((200, 200, 200)) # fill screen with grey color
        self.screen.fill((200, 200, 200), pygame.Rect(self.f_x,self.f_y, self.f_w,self.f_h))
        self.f_x += self.f_rate
        self.AObjs['right_facing'].blit(self.screen, (self.f_x, self.f_y))

    def move_left(self):
        self.d = left
        #self.screen.fill((200, 200, 200)) # fill screen with grey color
        self.screen.fill((200, 200, 200), pygame.Rect(self.f_x,self.f_y, self.f_w,self.f_h))
        self.f_x -= self.f_rate
        self.AObjs['left_facing'].blit(self.screen, (self.f_x, self.f_y))
        
    def move_up(self):
        #self.screen.fill((200, 200, 200)) # fill screen with grey color
        self.screen.fill((200, 200, 200), pygame.Rect(self.f_x,self.f_y, self.f_w,self.f_h))
        self.f_y -= self.f_rate
        if self.d == right:
            self.AObjs['right_facing'].blit(self.screen, (self.f_x, self.f_y))
        elif self.d == left:
            self.AObjs['left_facing'].blit(self.screen, (self.f_x, self.f_y))

    def move_down(self):
        #self.screen.fill((200, 200, 200)) # fill screen with grey color
        self.screen.fill((200, 200, 200), pygame.Rect(self.f_x,self.f_y, self.f_w,self.f_h))
        self.f_y += self.f_rate
        if self.d == right:
            self.AObjs['right_facing'].blit(self.screen, (self.f_x, self.f_y))
        elif self.d == left:
            self.AObjs['left_facing'].blit(self.screen, (self.f_x, self.f_y))
