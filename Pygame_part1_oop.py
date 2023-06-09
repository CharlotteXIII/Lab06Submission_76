import sys 
import pygame as pg

class Rec:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.R = 250
        self.G = 0
        self.B = 0
    def draw(self,screen):
        pg.draw.rect(screen,(self.R,self.G,self.B),(self.x,self.y,self.w,self.h))

class Button(Rec):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rec.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        x = 0 
        B = 0
        x,B = pg.mouse.get_pos()
        if x >= self.x and x <= self.x + self.w and B >= self.y and B <= self.y + self.h :
            return True  #function activated
        else : return False
        pass

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(400-50,240-50,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    if btn.isMouseOn():
        btn.R = 192
        btn.G = 192
        btn.B = 192
        if pg.mouse.get_pressed()==(1,0,0) :
            btn.R = 128
            btn.G = 0
            btn.B = 128
    else:
        btn.R = 250
        btn.G = 0
        btn.B = 0
    btn.draw(screen)
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    