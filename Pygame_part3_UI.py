import sys
import pygame as pg

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
    def t(self):
        return self.text

pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

font = pg.font.Font('freesansbold.ttf', 20) # font and fontsize
text1 = font.render('First Name', True, (255,255,255),(0,0,0)) # (text,is smooth?,letter color,background color)
textRect1 = text1.get_rect() # text size
textRect1.center = (152, 90)

font = pg.font.Font('freesansbold.ttf', 20) # font and fontsize
text2 = font.render('Last Name', True, (255,255,255), (0,0,0)) # (text,is smooth?,letter color,background color)
textRect2 = text2.get_rect() # text size
textRect2.center = (151, 190)

font = pg.font.Font('freesansbold.ttf', 20) # font and fontsize
text3 = font.render('Age', True, (255,255,255), (0,0,0)) # (text,is smooth?,letter color,background color)
textRect3 = text3.get_rect() # text size
textRect3.center = (118, 290)

font = pg.font.Font('freesansbold.ttf', 20) # font and fontsize
text4 = font.render('Submit', True, (255,255,255), (0,0,0)) # (text,is smooth?,letter color,background color)
textRect4 = text4.get_rect() # text size
textRect4.center = (500, 290)

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(100, 100, 140, 32) # สร้าง InputBox1
input_box2 = InputBox(100, 200, 140, 32) # สร้าง InputBox2
input_box3 = InputBox(100, 300, 140, 32) # สร้าง InputBox2

input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True

while run:

    screen.fill((255, 255, 255))
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text4, textRect4)
    nnn = input_box3.t
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
            if input_box3.t().isdigit() :
                pass
            else: print("ERROR")

        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()