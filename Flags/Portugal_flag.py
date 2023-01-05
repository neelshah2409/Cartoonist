import turtle as z

z.shape("arrow")
z.penup()
z.goto(-450, 300)
z.pendown()

z.color("black", "green")
z.begin_fill()
for x in range(2):
    z.forward(300)
    z.right(90)
    z.forward(600)
    z.right(90)
z.end_fill()
z.forward(200)

z.color("black", "red")
z.begin_fill()
for x in range(2):
    z.forward(600)
    z.right(90)
    z.forward(600)
    z.right(90)
z.end_fill()
z.right(90)
z.forward(600)

z.penup()
z.goto(200, -290)
z.right(154)
z.color("white", "white")
z.write("portugal", font=("chiller", 14, 'normal', 'bold', 'italic'))
z.goto(450, -350)
