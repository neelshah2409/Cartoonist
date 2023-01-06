import turtle

win = turtle.Screen()
win.title("Spiral design")
win.bgcolor("Black")

t = turtle.Turtle()
t.pencolor("silver")
t.pensize(3)
t.speed(100)
circle_radius = 40

for i in range(200):
    t.circle(circle_radius)
    t.right(40)
    if((i+1)%4==0):
        circle_radius = circle_radius+10

turtle.done()
