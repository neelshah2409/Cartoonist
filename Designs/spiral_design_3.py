import turtle

wn=turtle.Screen()
wn.setup(600,600)
wn.title("Spiral design")
t=turtle.Turtle()
t.speed(100)
r=10
for i in range(200):
    t.circle(r+i,45)
    t.pencolor("black")
t.penup()
t.home()
t.pendown()

m=20
for i in range(200):
    t.circle(m+i,45)
    t.pencolor("grey")
t.penup()
t.home()
t.pendown()

n=30
for i in range(200):
    t.circle(n+i,45)
    t.pencolor("black")    

turtle.done()