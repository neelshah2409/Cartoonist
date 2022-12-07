import turtle
turtle.bgcolor ("black")
turtle.colormode (255)

turtle.setup(800,500)
def square ():
  for i in range(4):
    turtle.forward (100)
    turtle.right (90)
    
turtle.left (90)

# red box
turtle.penup()
turtle.goto (-300, 100)
turtle.pendown ()
turtle.color (246,83,20)
turtle.begin_fill()
square()
turtle.end_fill()

# green box
turtle.penup()
turtle.goto (-195, 100)
turtle.pendown ()
turtle.color (124,187,0)
turtle.begin_fill()
square()
turtle.end_fill()

# blue box
turtle.penup()
turtle.goto (-300, -5)
turtle.pendown ()
turtle.color (0,161,241)
turtle.begin_fill()
square()
turtle.end_fill()

# yellow box
turtle.penup()
turtle.goto (-195, -5)
turtle.pendown ()
turtle.color (255, 187, 0)
turtle.begin_fill()
square()
turtle.end_fill()


# turtle.hideturtle()
turtle.done
