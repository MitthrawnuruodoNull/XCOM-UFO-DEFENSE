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
SIZE = 25
keys = [False,False,False,False]
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
        else:
            self.touching = False
#Creating GRID class
class GridSquare(object):
    def __init__(self, internal_row, internal_column, touching,clicked):
        self.internal_row = internal_row
        self.internal_column = internal_column
        self.touching = touching
        self.clicked = clicked
        self.cameraoffset = [0,0]
    
    def draw(self):
        self.rect = pygame.Rect([int(self.internal_row) + self.cameraoffset[0],int(self.internal_column) + self.cameraoffset[1],50,50])
        pygame.draw.rect(screen,[0,0,255],self.rect,0)
    def cameraupdate(self):
        if keys[0] == True:
            self.internal_column += 4
            self.cameraoffset[1] = 0
        elif keys[1] == True:
            self.internal_row += 4
            self.cameraoffset[0] = 0
        elif keys[2] == True:
            self.internal_column -= 4
            self.cameraoffset[1] = 0
        elif keys[3] == True:
            self.internal_row -= 4
            self.cameraoffset[0] = 0
        
#BUTTONS
grid = []
for i in range(-100,900,52):
    for k in range(-100,700,52):
        grid.append(GridSquare(i,k,False,False))    
titlescreen = Button(300,300,200,100,"Start",False,False)
#MAIN LOOP STARTS HERE
while True:
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys[0] = True
            elif event.key == pygame.K_a:
                keys[1] = True
            elif event.key == pygame.K_s:
                keys[2] = True
            elif event.key == pygame.K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0]=False
            elif event.key == pygame.K_a:
                keys[1]=False
            elif event.key == pygame.K_s:
                keys[2]=False
            elif event.key == pygame.K_d:
                keys[3]=False
            elif event.key == pygame.K_SPACE:
                shooting = False
    if titlescreen.clicked == True:
        scene = "game"
    if scene == "game":
        screen.fill(black)
        for grids in grid:
           grids.cameraupdate()
           grids.draw()
           
    pygame.display.flip()
