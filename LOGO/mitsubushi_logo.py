import turtle

win = turtle.Screen()
win.title("Mitsibushi")
win.bgcolor("white")

t = turtle.Turtle()
t.pencolor("red")
t.pensize(3)
def part1():
    for i in range(4):
        t.forward(length)
        if(i%2 == 0):
            t.right(60)
        else:
            t.right(120)
length = 200
for i in range(3):
    t.begin_fill()
    t.color("red")
    t.left(120)
    part1()
    t.end_fill()

turtle.done()