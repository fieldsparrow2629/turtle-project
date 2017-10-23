from turtle import *
import random
colormode(255)
speed(100)
setup(width = 1300, height = 700, startx = 0, starty = 0)
r = 0
sun = Turtle()

#sky
bgcolor(000,000,255)
#grass
def draw_tree():
    penup()
    sety(-150)
    setx(random.randrange(-800,800))
    setheading(90)

    #trunk
    color(56,30,30)
    pendown()
    begin_fill()
    rt(-90)
    fd(10)
    rt(90)
    fd(50)
    rt(90)
    fd(10)
    rt(90)
    fd(50)
    end_fill()
    rt(180)
    fd(50)
    
    #leaves
    color(40,130,50)
    begin_fill()
    rt(90)
    fd(15)
    rt(240)
    fd(40)
    rt(-120)
    fd(40)
    rt(-120)
    fd(40)
    end_fill()
    
def draw_ground():
    penup()
    sety(-150)
    setx(700)
    setheading(180)
    pendown()
    begin_fill()
    fd(1400)
    rt(-90)
    fd(400)
    rt(-90)
    fd(1400)
    rt(-90)
    fd(400)
    end_fill()

def draw_sun(r):
    sun.penup()
    sun.goto(350,250)
    sun.pendown()
    sun.begin_fill()
    sun.color(240,242,90)
    sun.circle(50 + r)
    sun.end_fill()
    r += 5
    


for i in range(10):
    draw_tree()

while True:
    draw_sun(r)

    
draw_ground()
penup()
goto(0,0)

def k(x,y):
    if y > -150:
        if bgcolor() == (00,00,00):
            bgcolor(000,000,255)
        else:
            bgcolor(00,00,00)

onscreenclick(k)

listen()
mainloop()
