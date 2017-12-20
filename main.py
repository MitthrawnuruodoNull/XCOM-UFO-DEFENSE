#IMPORTING MODULES
import pygame
import random
#THERE MAY BE MORE LATER
pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('X-COM UFO DEFENSE')
done = False
while done == False:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True
          pygame.quit()
        
          
  

    
