#IMPORTING MODULES
import pygame
import random
import sys
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
#SETTING UP BUTTON CLASS
class Button(object):
    def __init__(self, x, y, width, height,text,touching,clicked):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.rect = pygame.Rect([int(self.x),int(self.y),int(self.width),int(self.height)])
        self.touching = touching
        self.clicked = clicked
    def draw(self):
        #DRAW FUNCTION(MAY NEED WORK ON THE TEXT FORMULA)
        text1 = myfont.render(str(self.text), 1, (black))
        pygame.draw.rect(screen,[255,255,255],self.rect,0)
        screen.blit(text1, (self.x + self.width/3,self.y + self.height/3))
        
    def click(self):
        #EASY CLICK DETECTION
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.touching = True
            print(scene)
        else:
            self.touching = False
#BUTTONS
titlescreen = Button(300,300,200,100,"Start",False,False)
#MAIN LOOP STARTS HERE
done = False
while done == False:
    if scene == "start":
      screen.fill(white)
      screen.blit(title, (300,50))
      titlescreen.draw()
      titlescreen.click()
      #EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if titlescreen.touching == True and event.type == pygame.MOUSEBUTTONDOWN:
            titlescreen.clicked = True
        else:
            titlescreen.clicked = False
    if titlescreen.clicked == True:
        scene = "game"
    if scene == "game":
        screen.fill(black)
    pygame.display.flip()
