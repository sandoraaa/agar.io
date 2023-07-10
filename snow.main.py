import pygame
import random

bg=pygame.image.load('bg.jpg')
pygame.init()
class Snow ():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed= random.randint(1,3)
        self.img_filename = 'snow1.png'
        self.image = pygame.image.load (self.img_filename)



    def draw(self):
        window.blit(self.image,(self.x,self.y))
    def fall(self):
        self.y+=2
        if self.y>height:
            self.y=-50
            #self.y=random.randint(0,500)
        #self.y=+self.speed
        #self.x+= self.speed


width=600
height =400

n=100

snow_list=[]

for i in range(n):
    s=Snow(random.randint(0,width),random.randint(0,height))
    snow_list.append(s)


#s=Snow(100,100)

size_window = (width, height)
window = pygame.display.set_mode(size_window)
pygame.display.set_caption('Game ')
run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    window.fill ('black')
    window.blit(bg, (0, 0))
    for e in range(n):
        snow_list[e].draw()
        snow_list[e].fall()




    pygame.time.delay(50)
    pygame.display.update()

pygame.quit()