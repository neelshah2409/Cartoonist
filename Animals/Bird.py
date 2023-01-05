import turtle

turtle.Screen().bgcolor("red")

tur = turtle.Turtle()
tur.pensize(7)

def go(x,y):
    tur.penup()
    tur.goto(x,y)
    tur.pendown()

# Main Body
tur.fillcolor("#9cf71b")
go(-150,-70)
tur.seth(-30)


tur.begin_fill()
tur.circle(220,130)
tur.circle(120,180)
tur.circle(-120,110)
tur.seth(-52)
tur.circle(220,30)
tur.end_fill()

# Feather
tur.fillcolor("#dcf53b")
go(-100,90)
tur.seth(160)
tur.begin_fill()
tur.circle(-25,180)
tur.circle(-120,60)
tur.circle(-40,60)
tur.circle(-120,60)
tur.circle(-30,180)
tur.seth(180)
tur.circle(-50,45)
tur.circle(-30,190)
tur.end_fill()

# Eye
tur.fillcolor("#1c0508")
tur.pencolor("#1c0508")
tur.pensize(7)
go(60,200)
tur.seth(-180)

tur.begin_fill()
tur.circle(35)
tur.end_fill()

tur.fillcolor("white")
tur.begin_fill()
tur.circle(35,180)
tur.end_fill()

# Foot
go(-30,-100)
tur.seth(-80)
tur.pensize(10)
tur.circle(-90,40)

go(30,-90)
tur.seth(-80)
tur.pensize(10)
tur.circle(-120,35)

# Chonch
go(180,170)
tur.seth(15)
tur.circle(60,30)
go(180,160)
tur.seth(-15)
tur.circle(-50,40)

tur.hideturtle()
turtle.done()
