#draw mickey mouse using turtle

#importing necessary modules
from tkinter import N
import turtle
import colorsys

#Initialize a variable for turtle
micky_mouse = turtle.Turtle()
micky_mouse.speed(0)

#Create a turtle screen
screen= turtle.Screen()
#Define height and width of screen
screen.setup(1200,600)
#Define Background color of screen
screen.bgcolor('#ffdbac')
screen.update()


# Define title of program
turtle.title("Copy Assignment Turtle")


#Code for drawing head of mickey mouse

#initializing starting point of head
micky_mouse.goto(0,-150)
#filling color in head
micky_mouse.begin_fill()
#setting color of head
micky_mouse.color('black')
#drawing head
micky_mouse.circle(150)
#ending fill
micky_mouse.end_fill()


#Code for drawing ears of mickey mouse

#left ear
#initializing starting point of left ear
micky_mouse.goto(-120,100)
#filling color in left ear
micky_mouse.begin_fill()
#setting color of left ear
micky_mouse.color('black')
#drawing left ear
micky_mouse.circle(90)
#ending fill
micky_mouse.end_fill()

#right ear
#initializing starting point of right ear
micky_mouse.goto(120,100)
#filling color in right ear
micky_mouse.begin_fill()
#setting color of right ear
micky_mouse.color('black')
#drawing right ear
micky_mouse.circle(90)
#ending fill
micky_mouse.end_fill()



#Code for drawing face of mickey mouse

#initializing starting point of face dip
micky_mouse.goto(40,-190)
#filling color in face dip
micky_mouse.begin_fill()
#setting color of face dip
micky_mouse.color('#ffdbac')
#drawing face dip
micky_mouse.circle(120)
#ending fill
micky_mouse.end_fill()

micky_mouse.goto(-40,-190)
micky_mouse.begin_fill()
micky_mouse.color('#ffdbac')
micky_mouse.circle(120)
micky_mouse.end_fill()

#Code for face outline

#initializing starting point of face outline
micky_mouse.goto(0,-150)
#setting color of face outline
micky_mouse.color('black')
#drawing face outline
micky_mouse.circle(150)



#Code for drawing eyes of mickey mouse

#initializing starting point of left eye
micky_mouse.penup()
micky_mouse.goto(-50,-25)
micky_mouse.pendown()

def draw_left_eye(rad):
    for i in range(4):
     
    # two arcs
        #filling color in eyes
        micky_mouse.begin_fill()
        #setting color of eyes
        micky_mouse.color('white')
        #DRAW eyes
        micky_mouse.circle(rad,90)
        micky_mouse.circle(rad//4,90)
        #ending fill                              
        micky_mouse.end_fill()

# Main section
# tilt the shape to negative 45
micky_mouse.seth(45)
draw_left_eye(40)


#Code  of left eye ball
micky_mouse.penup()
micky_mouse.goto(-50,-20)
micky_mouse.pendown()
#filling color in left eye
micky_mouse.begin_fill()
#setting color of left eye
micky_mouse.color('black')
#drawing left eye
micky_mouse.circle(8)
#ending fill
micky_mouse.end_fill()

#initializing starting point of right eye

micky_mouse.penup()
micky_mouse.goto(55,-25)
micky_mouse.pendown()

def draw_eye(rad):
    for i in range(4):
     
    # two arcs
        #filling color in eyes
        micky_mouse.begin_fill()
        #setting color of eyes
        micky_mouse.color('white')
        #DRAW eyes
        micky_mouse.circle(rad,90)
        micky_mouse.circle(rad//4,90)
        #ending fill                              
        micky_mouse.end_fill()

# Main section
# tilt the shape to negative 45
micky_mouse.seth(45)
draw_eye(40)

# code for right eye ball
micky_mouse.penup()
micky_mouse.goto(50,-20)
micky_mouse.pendown()
#filling color in right eye
micky_mouse.begin_fill()
#setting color of right eye
micky_mouse.color('black')
#drawing right eye
micky_mouse.circle(8)
#ending fill
micky_mouse.end_fill()

#Code for drawing outline of eyes of mickey mouse
#initializing starting point of right eye outline
micky_mouse.penup()
micky_mouse.goto(55,-25)
micky_mouse.pendown()

def draw_reye_outline(rad):
    for i in range(4):
     
    # two arcs
        micky_mouse.circle(rad,90)
        micky_mouse.circle(rad//4,90)
        
# Main section
# tilt the shape to negative 45
micky_mouse.seth(45)
draw_reye_outline(40)

#initializing starting point of left eye outline
micky_mouse.penup()
micky_mouse.goto(-50,-25)
micky_mouse.pendown()

def draw_leye_outline(rad):
    for i in range(4):
     
    # two arcs
        micky_mouse.circle(rad,90)
        micky_mouse.circle(rad//4,90)
        
# Main section
# tilt the shape to negative 45
micky_mouse.seth(45)
draw_leye_outline(40)



#Code for drawing nose of mickey mouse

#initializing starting point of nose
micky_mouse.penup()
micky_mouse.goto(-20,-50)
micky_mouse.pendown()
def draw(rad):
    for i in range(3):
     
    # two arcs
        #filling color in nose
        micky_mouse.begin_fill()
        #setting color of nose
        micky_mouse.color('black')
        #DRAW NOSE
        micky_mouse.circle(rad,90)
        micky_mouse.circle(rad//3,90)
        #ending fill                              
        micky_mouse.end_fill()

# Main section
# tilt the shape to negative 45
micky_mouse.seth(-45)
draw(25)

#speed of turtle
micky_mouse.speed(3)


#Code for drawing lips of mickey mouse

#initializing starting point of lips
micky_mouse.speed(0)
micky_mouse.penup()
micky_mouse.goto(-48,-78)
micky_mouse.pendown()
#direction of turtle
micky_mouse.right(90)
#setting heading of turtle
micky_mouse.setheading(-50)
#drawing lips
for x in range (110):
  micky_mouse.forward(1)
  micky_mouse.left(1)
# micky_mouse.left(110)
# micky_mouse.forward(110)
# micky_mouse.end_fill()
micky_mouse.speed(0)

#Code for drawing eyebrows of mickey mouse


micky_mouse.setheading(-155)
#setting color of left eyebrow
micky_mouse.color('black')
#intialze pen thickness
micky_mouse.pensize(2)
micky_mouse.penup()
#initializing starting point of left eyebrow
micky_mouse.goto(-40,-70)
micky_mouse.pendown()
#drawing left eyebrow
micky_mouse.circle(30,40)
#hide turtle
micky_mouse.hideturtle()


#code for drawing right eyebrow
micky_mouse.setheading(-245)
#setting color of right eyebrow
micky_mouse.color('black')
#intialze pen thickness
micky_mouse.pensize(2)
micky_mouse.penup()
#initializing starting point of right eyebrow
micky_mouse.goto(50,-80)
micky_mouse.pendown()
#drawing right eyebrow
micky_mouse.circle(30,40)
#hide turtle
micky_mouse.hideturtle()

#Code for drawing tongue of mickey mouse
micky_mouse.pensize(1)
micky_mouse.penup()
micky_mouse.goto(-33,-92)
micky_mouse.pendown()
#direction of turtle
micky_mouse.right(90)
#setting heading of turtle
micky_mouse.setheading(-45)
#drawing lips
micky_mouse.forward(20)
micky_mouse.circle(25,95)
micky_mouse.forward(20)

turtle.done()    

#code for holding the output screen
turtle.mainloop()
