#IMPORTING MODULES
import pygame
import random
white = (250,250,250)
black = (0,0,0)
#SETTING UP STUFF
pygame.init()
#ADDING FONTS AND TEXT
myfont = pygame.font.SysFont("monospace", 15)
title = myfont.render("X-COM: UFO DEFENSE", 1, (black))
#MORE SETTING UP
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('X-COM UFO DEFENSE')
#MAIN LOOP STARTS HERE
done = False
while done == False:
      screen.fill(white)
      screen.blit(title, (300,50))
      pygame.display.flip()
