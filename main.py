
import pygame
import sys
import pyganim
from pygame.locals import *
import time
from fish_artist import FishArtist
from random import *
import random
import Creep
#http://stackoverflow.com/questions/5555712/generate-a-random-number-in-python
#from handler import DrawHandling

pygame.init()


SCREEN_HEIGHT = 300 + 400
SCREEN_WIDTH = 470 + 400
background = 'fishdish/fishtitle.png'
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

#http://stackoverflow.com/questions/9961563/how-can-i-make-a-sprite-move-when-key-is-held-down
BGCOLOR = (100, 50, 50)
#Red, Green, Blue
main_fish = FishArtist(screen, 300, 200, 'blue_fish', 5)

CREEP_FILENAMES = [
    "green_fish",
    "grey_fish",
    "purple_fish",
    "yellow_fish"
    ]
N_CREEPS = len(CREEP_FILENAMES)
creeps = [] 

for i in range(N_CREEPS):
    creeps.append(Creep.Creep(screen, 
                        CREEP_FILENAMES[(i)],
                        (randint(0, SCREEN_HEIGHT),
                        randint(0, SCREEN_HEIGHT)),
                        (random.choice([-1,1]),
                         random.choice([-1,1])),
                        0.1, 10, 15))

while 1:
    # clock to slow down (only being called 30 times per second)
    timePass = clock.tick(60) 

    main_fish.stationary_fish_movements(20)

#    k = pygame.key.get_pressed()
    main_fish.keys_pressed_response(pygame.key.get_pressed())
    for creep in creeps:
        creep.stationary_fish_movements(20)
        creep.move_right()
           
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

        if (event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE)):
            main_fish.grow()

        if ( (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT)):
            main_fish.move_right()

        if ((event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT)):
            main_fish.move_left()

        if ((event.type == pygame.KEYDOWN and event.key == pygame.K_UP)):
            main_fish.move_up()

        if ((event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN)):
            main_fish.move_down()

        

    pygame.display.update()


