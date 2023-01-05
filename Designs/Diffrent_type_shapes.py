#!/bin/python3
#importing the turtle and random modules
import turtle, random

 # set wn to the window object
wn=turtle.Screen()
# set the window background color
wn.bgcolor('#F0F8FF')

#needed if using RGB colors
#turtle.colormode(255)

#use "t" instead of typing "turtle" in code
t=turtle.Turtle()

#delete the turtle's drawings and restore its default values
t.reset()

#puts a dot on the screen
t.dot(10, 'light gray')

t.up()
#going to specific coordinates
t.goto(-200, 0)
#turtle color by name
t.pencolor('light gray')

#variable
line_length=15

#dotted line on x
for i in range(13):
  t.pendown()
  t.forward(line_length)
  t.penup()
  t.forward(5)
  t.pendown()
  line_length=line_length + 2

t.up()
t.goto(0, -250)
t.left(90)

#dotted line on y
for i in range(10):
  t.pendown()
  t.forward(line_length)
  t.penup()
  t.forward(5)
  t.pendown()
  line_length=line_length + 2


t.up()
t.goto(110, 100)
#heading (i.e. direction) 0 is right, 180 is left, 90 is up, 270 is down
t.setheading(0)
t.pencolor('black')

#square
t.down()
t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.forward(60)


t.up()
t.setheading(0)
t.backward(20)
#turtle speed as number
t.speed(3)
t.pencolor('blue')

#setting up a variable
turn=120

#triangle
t.down()
t.backward(70)
#using the variable
t.right(turn)
t.backward(70)
t.right(turn)
t.backward(70)


t.up()
t.setheading(0)
t.goto(-105, 100)
#using HEX color
t.pencolor('#00FA9A')
#turtle pen size
t.pensize(5)

#angled square
#defining a function with parameters
def angled_square(side, angle1, angle2):
  t.down()
  for i in range(2):
    t.forward(side)
    t.left(angle1)
    t.forward(side)
    t.left(angle2)

#calling the function and providing parameters
angled_square(60, 60, 120)


t.up()
t.goto(-150, 100)
t.pencolor('gold')
t.pensize(20)

#circle
t.down()
for i in range(24):
  t.forward(7)
  t.left(15)


t.up()
t.goto(45, 15)
#using RGB color; also need colormode above
t.pencolor(220,20,60)
t.pensize(5)
#octagon
t.down()
for i in range(8):
  t.forward(25)
  t.left(45)


t.up()
t.goto(130, 15)
t.pencolor('purple')
#change the turtle shape to a turtle
t.shape("turtle")

#hexagon
t.down()
#set fill color
t.color('purple')
#start fill when drawing starts
t.begin_fill()
for i in range(6):
  t.forward(35)
  t.left(60)
#end fill when drawing ends
t.end_fill()


t.up()
t.goto(100, -75)
#turtle speed
t.speed('normal')
t.pencolor('pink')

#flower
t.down()
for i in range(4):
  for i in range(2):
    t.forward(40)
    t.left(60)
  for i in range(2):
    t.left(60)
    t.forward(40)
  t.right(150)


t.up()
t.goto(-115, -75)
t.speed('fast')
t.pencolor('#FF0000')
t.pensize(3)
# Setting up variables: list of colors to pick from and length
rainbowColors=['#FF0000','#FFA600','#FFFF00', '#62FF00', '#1E56FC','#4800FF','#CC00FF','#69C5FF']
length=40

#wild
t.down()
for i in range(12):
  #choose a random color from the list above each time
  color = random.choice(rainbowColors)
  for i in range(3):
    t.forward(length)
    t.left(120)
  t.left(30)
  t.pencolor(color)
  length=length + 5


t.up()
#returns turtle to original coordinates (0, 0)
t.home()
#pause in milliseconds
wn.delay(500)
#have turtle print text on the screen
t.write('Diffrent type of shapes', True, align='center', font=('Arial', 14, 'bold'))
wn.delay(500)
#make turtle invisible
t.hideturtle()
wn.delay(5000)
#clear all drawings off the screen
t.clear()
