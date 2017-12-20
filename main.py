#IMPORTING MODULES
import pygame
import random
black = (250,250,250)
white = (0,0,0)
#SETTING UP STUFF
pygame.init()
#ADDING FONTS AND TEXT
myfont = pygame.font.SysFont("monospace", 15)
title = myfont.render("X-COM: UFO DEFENSE", 1, (white))
#MORE SETTING UP
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('X-COM UFO DEFENSE')
#ADDING BACKGROUND AND TITLE
pygame.surface.fill(black)
#MAIN LOOP STARTS HERE
done = False
while done == False:
      screen.blit(title, (100,100))
      screen.fill(black)
      pygame.display.flip()
      

        
          
  

    
