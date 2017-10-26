from turtle import *
import random

#setup
colormode(255)
setup(width = 1300, height = 700, startx = 0, starty = 0)
<<<<<<< HEAD

#create other turtles
sun = Turtle()
cld = Turtle()

#list of colors
colors = [(240,248,255),(255,211,155),(0,255,255),(178,34,34),(255,255,224),(255,228,225)]
          
#sky
bgcolor(000,000,255)

=======
colors = [(144, 170, 6),(162, 163, 3),(212, 103, 25),(218, 120, 27)]
bgcolor(000,000,255)

#create other turtles
cld = Turtle()
sun = Turtle()
grs = Turtle()

speed(0)
cld.speed(0)
sun.speed(0)
grs.speed(0)


>>>>>>> 79afc8de8e60752d78d4c211883d8dee78299422
#functions
def draw_tree(leaves):
    penup()
    goto(random.randrange(-650,650),random.randrange(-175,-150))
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
    color(leaves)
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

def make_forest():
    count = 0
    while count < 2:
        for i in range(10):
            draw_tree(colors[random.randrange(0,5)])
        count += 1
    draw_sun()
    
def draw_grass():
    grs.penup()
    grs.goto(random.randrange(-650,650),random.randrange(-300,-160))
    grs.pendown()
    grs.color("green")
             
    x = 0
    for i in range(5):
        grs.setheading(15 + x)
        grs.fd(15)
        grs.rt(180)
        grs.fd(15)
        x += 30
             
def make_forest():
    count = 0
    while count < 5:
        for i in range(5):
            draw_tree(colors[random.randrange(0,3)])
            draw_grass()
            draw_grass()
            
        count += 1
    draw_sun()
    
def draw_ground():
<<<<<<< HEAD
    color(0,123,12)
=======
    color(77, 158, 58)
>>>>>>> 79afc8de8e60752d78d4c211883d8dee78299422
    penup()
    sety(-150)
    setx(700)
    setheading(180)
    pendown()
    begin_fill()
<<<<<<< HEAD
    
    fd(1400)
=======
    fd(2000)
>>>>>>> 79afc8de8e60752d78d4c211883d8dee78299422
    rt(-90)
    fd(400)
    rt(-90)
    fd(2300)
    rt(-90)
    fd(400)
    
    end_fill()

def draw_sun():
    sun.penup()
    sun.goto(350,250)
    sun.pendown()
    sun.begin_fill()

<<<<<<< HEAD
    #if night,draw moon
    #if day,draw sun
=======
    #draws a moon if its night
    #draws a sun if its day
>>>>>>> 79afc8de8e60752d78d4c211883d8dee78299422
    if bgcolor() == (00,00,00):
        sun.color(254, 252, 215)
    else:
        sun.color(240,242,90)
<<<<<<< HEAD
        
=======
>>>>>>> 79afc8de8e60752d78d4c211883d8dee78299422
    sun.circle(75)
    sun.end_fill()

def draw_cloud():
    cld.penup()
    cld.color(255,255,255)
    cld.goto(random.randrange(-700,700),random.randrange(0,300))
    size = 15
    
    for i in range(5):
        cld.pendown()
        cld.begin_fill()
        cld.circle(size)
        cld.rt(72)
        cld.end_fill()
        size += 2.5

def change_sky(x,y):
    if y > -150:
        if bgcolor() == (00,00,00):
            bgcolor(000,000,255)
        else:
            bgcolor(00,00,00)
    draw_sun()

<<<<<<< HEAD
def draw_cloud():
    cld.penup()
    cld.color(255,255,255)
    cld.goto(random.randrange(-700,700),random.randrange(0,300))
    cld.pendown()
    cld.begin_fill()
    
    radius = 15
    for i in range(5):
        cld.begin_fill()
        cld.circle(radius)
        cld.end_fill()
        cld.rt(72)
        radius  = radius + 2.5
        
#drawing the picture
draw_ground()
make_forest()

onscreenclick(change_sky)
onkey(draw_cloud,"Up")
=======
#draw picture
draw_ground()
make_forest()

onkey(draw_cloud,"Up")
onscreenclick(change_sky)
>>>>>>> 79afc8de8e60752d78d4c211883d8dee78299422

listen()
mainloop()
