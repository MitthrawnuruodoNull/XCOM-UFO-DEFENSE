#IMPORTING MODULES
import pygame
import random
black = (250,250,250)
white = (0,0,0)
#THERE MAY BE MORE LATER
pygame.init()
myfont = pygame.font.SysFont("monospace", 15)
title = myfont.render("X-COM: UFO DEFENSE", 1, (white))
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('X-COM UFO DEFENSE')
pygame.surface.fill(black)
screen.blit(title, (100,100))
done = False
while done == False:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True
          pygame.quit()
        
          
  

    
