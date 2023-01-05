import turtle as t

t.speed(5)
t.setup(800, 700)
t.bgcolor("blue")

# Bottom of body
t.penup()
t.goto(0, -280)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(110)
t.end_fill()

# Middle of body
t.penup()
t.goto(0, -110)
t.pendown()
t.begin_fill()
t.circle(90)
t.end_fill()

# Head of Snowman
t.penup()
t.goto(0, 20)
t.pendown()
t.begin_fill()
t.circle(70)
t.end_fill()

# Function to draw 1 small black circle
def black_circle():
	t.color("black")
	t.begin_fill()
	t.circle(10)
	t.end_fill()

# Eyes
x = -20
for i in range(2):
	t.penup()
	t.goto(x, 110)
	t.pendown()
	black_circle()
	x = x + 40

# Buttons
y = 0
for i in range(5):
	t.penup()
	t.goto(0, y)
	t.pendown()
	black_circle()
	y = y - 55

# Mouth
t.penup()
t.goto(0,70)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(17)
t.end_fill()

t.penup()
t.goto(0,75)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(17)
t.end_fill()

# Right Arm
t.penup()
t.goto(75, 0)
t.pendown()
t.color("brown")
t.begin_fill()
t.left(40)
for i in range(2):
	t.forward(75)
	t.left(90)
	t.forward(7)
	t.left(90)
t.end_fill()

# Right Finger 1
t.penup()
t.goto(115, 38)
t.pendown()
t.begin_fill()
t.left(40)
for i in range(2):
	t.forward(25)
	t.left(90)
	t.forward(5)
	t.left(90)
t.end_fill()

# Right Finger 2
t.begin_fill()
t.right(100)
for i in range(2):
	t.forward(25)
	t.left(90)
	t.forward(5)
	t.left(90)
t.end_fill()

# Left Arm
t.penup()
t.goto(-130, 50)
t.pendown()
t.begin_fill()
t.right(10)
for i in range(2):
	t.forward(75)
	t.right(90)
	t.forward(7)
	t.right(90)
t.end_fill()

# Left Finger 1
t.penup()
t.goto(-112, 58)
t.pendown()
t.begin_fill()
t.right(40)
for i in range(2):
	t.forward(25)
	t.right(90)
	t.forward(5)
	t.right(90)
t.end_fill()

# Left Finger 2
t.begin_fill()
t.right(100)
t.penup()
t.goto(-108, 31)
t.pendown()
for i in range(2):
	t.forward(25)
	t.right(90)
	t.forward(5)
	t.right(90)
t.end_fill()

# Hat
t.penup()
t.goto(50, 150)
t.pendown()
t.color("black")
t.begin_fill()
t.right(10)
t.forward(100)
t.right(90)
t.forward(10)
t.right(90)
t.forward(20)
t.left(90)
t.forward(45)
t.right(90)
t.forward(60)
t.right(90)
t.forward(45)
t.left(90)
t.forward(20)
t.right(90)
t.end_fill()


t.hideturtle()

t.done()
