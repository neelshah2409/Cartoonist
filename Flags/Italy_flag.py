import turtle as w
w.shape("turtle")

w.penup()
w.goto(-450, 300)
w.pendown()

w.color("black", "green")
w.begin_fill()
for x in range(2):
    w.forward(300)
    w.right(90)
    w.forward(600)
    w.right(90)
w.end_fill()

w.forward(600)

w.color("black", "red")
w.begin_fill()
for x in range(2):
    w.forward(300)
    w.right(90)
    w.forward(600)
    w.right(90)
w.end_fill()

w.right(90)
w.forward(600)
w.left(90)
w.backward(300)

w.penup()
w.goto(300, -290)
w.right(154)
w.color("white", "white")
w.write("Italy", font=("chiller", 14, 'normal', 'bold', 'italic'))
w.goto(450, -350)
