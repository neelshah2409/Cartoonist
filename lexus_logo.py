import turtle

win = turtle.Screen()
win.title("Lexus")
win.bgcolor("silver")

t = turtle.Turtle()
t.pencolor("black")
t.pensize(20)
t.penup()
t.setposition(-150, -150)
t.speed(10)
t.pendown()

def draw_eclipse(rad):
    for i in range(2):
        t.circle(rad,90)
        t.circle(rad//2,90)
t.seth(-45)
draw_eclipse(300)

t.penup()
t.forward(50)
t.left(90)

t.forward(150)
t.pendown()
t.forward(280)
t.right(180)
t.forward(280)
t.left(135)
t.forward(310)



turtle.done()