import turtle

win = turtle.Screen()
win.title("Audi")
win.bgcolor("Black")

t = turtle.Turtle()
t.pencolor("silver")
t.pensize(3)
circle_radius = 80
t.penup()
t.setposition(-200, -80)
t.pendown()
for i in range(4):
    t.circle(circle_radius)
    t.penup()
    t.forward(3*circle_radius/2)
    t.pendown()
t.hideturtle()
turtle.done()