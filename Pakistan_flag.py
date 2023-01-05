import turtle as z

z.shape("arrow")
z.speed(5)
z.penup()
z.goto(-500, 275)
z.pendown()

z.color("black", "dark green")
z.begin_fill()
for n in range(2):
    z.forward(1000)
    z.right(90)
    z.forward(550)
    z.right(90)
z.end_fill()

z.penup()
z.goto(150, 0)

z.penup()
z.backward(75)
z.left(90)
z.forward(125)
z.left(90)
z.pendown()

z.color("dark green", "white")
z.begin_fill()
z.circle(127.5)
z.end_fill()

z.penup()
z.goto(113, 127.5)
z.pendown()

z.color("dark green", "dark green")
z.begin_fill()
z.circle(107)
z.end_fill()

z.penup()
z.color("dark green", "white")
z.goto(225, 20)
z.right(20)
z.begin_fill()
for x in range(5):
    z.forward(100)
    z.right(144)
z.end_fill()

z.color("black", "white")
z.goto(-250, -275)
z.left(20)
z.pendown()

z.begin_fill()
for n in range(2):
    z.forward(250)
    z.right(90)
    z.forward(550)
    z.right(90)
z.end_fill()

z.penup()
z.goto(350, -255)
z.right(154)
z.color("white", "white")
z.write("Pakistan", font=("chiller", 14, 'normal', 'bold', 'italic'))
z.goto(450, -350)
