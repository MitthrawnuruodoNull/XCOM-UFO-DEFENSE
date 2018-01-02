#IMPORTING MODULES
import pygame
import random
white = (250,250,250)
black = (0,0,0)
#SETTING UP STUFF
pygame.init()
#ADDING FONTS AND TEXT
myfont = pygame.font.SysFont("monospace", 25)
title = myfont.render("X-COM: UFO DEFENSE", 1, (black))
#MORE SETTING UP
display_width = 800
display_height = 600
scene = "start"
screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('X-COM UFO DEFENSE')
class Button(object):
    def __init__(self, x, y, width, height,text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    def draw(self):
        text1 = myfont.render(str(self.text), 1, (black))
        pygame.draw.rect(screen,[255,255,255],[int(self.x),int(self.y),int(self.width),int(self.height)],0)
        screen.blit(text1, (self.x + self.width/3,self.y + self.height/3))
        
    def click(self):
        if self.get_rect.collidepoint(pygame.mouse.get_pos()): 
            print("hi")
titlescreen = Button(300,300,200,100,"Start")
#MAIN LOOP STARTS HERE
done = False
while done == False:
      screen.fill(white)
      screen.blit(title, (300,50))
      titlescreen.draw()
      pygame.display.flip()
