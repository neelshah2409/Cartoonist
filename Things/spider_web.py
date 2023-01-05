import turtle as t

# define turtle speed
t.speed(2)

# radical thread
for i in range(6):
   t.forward(150)
   t.backward(150)
   t.right(60)

# spiral thread length
side = 50

# Spider web color
t.fillcolor("Orange")

# building web
t.begin_fill()

for i in range(15):
   t.penup()
   t.goto(0, 0)
   t.pendown()
   t.setheading(0)
   t.forward(side)
   t.right(120)
   # Inner for loop of range 6
   for j in range(6):
      t.forward(side-2)#for each iteration side decreases by 2
      t.right(60)
   side = side - 10 #Side decreases by 10
#Fill color completes
t.end_fill()
turtle.done()
