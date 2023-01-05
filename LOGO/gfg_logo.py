# importing turtle for graphics
import turtle

# Forming the window screen
tut = turtle.Screen()

# background color green
tut.bgcolor("White")

# object
pen = turtle.Turtle()

#speed of pen
pen.speed(10)

# object color
pen.color("Green")

# object width
pen.width(10)
tut = turtle.Screen()


# Code for symbol
# backward C
for x in range(180):
    pen.forward(1)
    pen.right(1)

# up
pen.right(90)
pen.forward(50)

# right
pen.right(90)
pen.forward(130)

# down
pen.right(90)
pen.forward(50)
pen.left(90)

# forward C
for x in range(180):
    pen.backward(1)
    pen.right(1)

turtle.done()
