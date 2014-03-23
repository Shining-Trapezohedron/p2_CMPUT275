import pygame
import sys
import pyganim
from pygame.locals import *
import time
from random import randint
from random import random

pygame.init()

right = 'right'
left = 'left'

class FishArtist():
    def __init__(self,screen, fish_x, fish_y, fish_n, fish_rate, fish_height = 34, fish_width = 45): 
        self.f_h = fish_height
        self.f_w = fish_width
        self.f_x = fish_x
        self.f_y = fish_y
        self.f_n = fish_n
        self.f_rate = fish_rate
        self.screen = screen
        main_fish = 'fishdish/' + str(self.f_n)
        self.AObjs = {}
        

        
        right_facing = pyganim.PygAnimation([(main_fish + '_right_1.png', 0.1),
                                             (main_fish + '_right_2.png', 0.1),
                                             (main_fish + '_right_3.png', 0.1),
                                             (main_fish + '_right_4.png', 0.1),
                                             (main_fish + '_right_5.png', 0.1)])
        
        left_facing = pyganim.PygAnimation([(main_fish + '_left_1.png', 0.1),
                                            (main_fish + '_left_2.png', 0.1),
                                            (main_fish + '_left_3.png', 0.1),
                                            (main_fish + '_left_4.png', 0.1),
                                            (main_fish + '_left_5.png', 0.1)])
        self.AObjs['left_facing'] = left_facing
        self.AObjs['right_facing'] = right_facing 

        
        moveCond = pyganim.PygConductor(self.AObjs)
        self.d = right 
        moveCond.play()
        print("done initializing")


    def stationary_fish_movements(self, percent):
        #takes a percent chance (0, %100) of blinking while stationary
        if (randint(0,100) > (100-percent)): # because we want to the eye blinking every few seconds 
        # not at every iteration of the loop
            if self.d == right:
                self.AObjs['right_facing'].blit(self.screen, (self.f_x, self.f_y))
            
            if self.d == left:
                self.AObjs['left_facing'].blit(self.screen, (self.f_x, self.f_y))

    def keys_pressed_response(self, k):
        #takes in the keys pressed and responds accordingly
        if (k[pygame.K_RIGHT]):
            print('right facing')
            self.screen.fill((200, 200, 200)) # fill screen with grey color
            self.f_x += self.f_rate
            self.AObjs['right_facing'].blit(self.screen, (self.f_x, self.f_y))

        if (k[pygame.K_LEFT]):
            print('left facing')
            self.screen.fill((200, 200, 200)) # fill screen with grey color
            self.f_x -= self.f_rate
            self.AObjs['left_facing'].blit(self.screen, (self.f_x, self.f_y))
            
        if (k[pygame.K_UP]):
            print('up facing')
            self.screen.fill((200, 200, 200)) # fill screen with grey color
            self.f_y -= self.f_rate
            if self.d == right:
                self.AObjs['right_facing'].blit(self.screen, (self.f_x, self.f_y))
            elif self.d == left:
                self.AObjs['left_facing'].blit(self.screen, (self.f_x, self.f_y))

        if (k[pygame.K_DOWN]):
            print('down facing')
            self.screen.fill((200, 200, 200)) # fill screen with grey color
            self.f_y += self.f_rate
            if self.d == right:
                self.AObjs['right_facing'].blit(self.screen, (self.f_x, self.f_y))
            elif self.d == left:
                self.AObjs['left_facing'].blit(self.screen, (self.f_x, self.f_y))

    def move_right(self):
        print('right facing')
        self.d = right
        self.screen.fill((200, 200, 200)) # fill screen with grey color
        self.f_x += self.f_rate
        self.AObjs['right_facing'].blit(self.screen, (self.f_x, self.f_y))

    def move_left(self):
        print('left facing')
        self.d = left
        self.screen.fill((200, 200, 200)) # fill screen with grey color
        self.f_x -= self.f_rate
        self.AObjs['left_facing'].blit(self.screen, (self.f_x, self.f_y))
        
    def move_up(self):
        print('up facing')
        self.screen.fill((200, 200, 200)) # fill screen with grey color
        self.f_y -= self.f_rate
        if self.d == right:
            self.AObjs['right_facing'].blit(self.screen, (self.f_x, self.f_y))
        elif self.d == left:
            self.AObjs['left_facing'].blit(self.screen, (self.f_x, self.f_y))

    def move_down(self):
        print('down facing')
        self.screen.fill((200, 200, 200)) # fill screen with grey color
        self.f_y += self.f_rate
        if self.d == right:
            self.AObjs['right_facing'].blit(self.screen, (self.f_x, self.f_y))
        elif self.d == left:
            self.AObjs['left_facing'].blit(self.screen, (self.f_x, self.f_y))

    def grow(self):
#        width_height
#        self.AObjs['right_facing']._makeTransformedSurfacesIfNeeded()
#        for i in range(len(self.AObjs['right_facing']._images)):
#            selfself.AObjs['right_facing']._transformedImages[i] = pygame.transform.scale(self.AObjs['right_facing'].getFrame(i), width_height)
#        print(self.AObjs['right_facing'].getCopy().get_size())
#        print(self.AObjs['left_facing'].getCopy().get_size())
#        self.f_w, self.f_h = self.AObjs['left_facing'].getMaxSize()
#        a1,b1 = self.AObjs['left_facing'].getMaxSize()
        self.AObjs['right_facing'].smoothscale((self.f_w + 10,self.f_h + 10))
        self.AObjs['left_facing'].smoothscale((self.f_w + 10,self.f_h + 10))
        self.f_w += 10
        self.f_h += 10
        print(self.AObjs['left_facing'].getMaxSize())
        print(self.AObjs['right_facing'].getMaxSize())

        

#        self.AObjs['right_facing'].scale((200,300))
#        self.AObjs['left_facing'].scale((200,300))
#        self.AObjs['right_facing'] = pygame.transform.scale2x(self.AObjs['right_facing'])
#        self.AObjs['left_facing'] = pygame.transform.scale2x(self.AObjs['left_facing'])
        print('grown to twice its size')

                
                
