import turtle
import math

window = turtle.Screen()
window.bgcolor("yellow")

cursor = turtle.Turtle() # Cursor
cursor.shape("turtle")
cursor.color("black")
cursor.speed(3)
cursor.pensize(10)


def movePen(cursor, x, y):
  cursor.penup()
  cursor.setposition(x, y)
  cursor.pendown()

def movePenX(cursor, x):
  cursor.penup()
  cursor.setx(x)
  cursor.pendown()

def movePenY(cursor, y):
  cursor.penup()
  cursor.sety(y)
  cursor.pendown()

def positionAlongCircle(x, y, radius, angle):
  radians = math.radians(angle)
  return [x + (radius*math.sin(radians)),
            y + (radius*math.cos(radians))]

# Draw the head

movePenY(cursor, -150)
cursor.circle(150)

# Draw the nose

noseMouthOffset = -15

movePenY(cursor, -20 + noseMouthOffset)
cursor.circle(20)

# Draw the mouth

movePen(cursor, -100, -20 + noseMouthOffset)
cursor.right(90)
cursor.circle(50, 180)
cursor.left(180)
cursor.circle(50, 180)

# Draw the eyes

eyeSpacingX = 30
eyePosY = 40
eyeRadius = 30

# Right eye

movePen(cursor, eyeSpacingX, eyePosY)
cursor.right(180)
cursor.circle(eyeRadius, -180)

# Left eye

movePen(cursor, -eyeSpacingX, eyePosY)
cursor.circle(eyeRadius, 180)

# Draw the tongue

movePen(cursor, -20, -60 + noseMouthOffset)
cursor.circle(20, 180)

# Draw the ears

# Right ear

earBeginAngle = 25
earSize = 85
earWidth = 22
positionA = positionAlongCircle(0, 0, 150, earBeginAngle)
movePen(cursor, positionA[0], positionA[1])

positionB = positionAlongCircle(0, 0, 150 + earSize, earBeginAngle + earWidth)
cursor.setposition(positionB[0], positionB[1])

positionC = positionAlongCircle(0, 0, 150, earBeginAngle + earWidth * 2)
cursor.setposition(positionC[0], positionC[1])

# Left ear

positionA = positionAlongCircle(0, 0, 150, -earBeginAngle)
movePen(cursor, positionA[0], positionA[1])

positionB = positionAlongCircle(0, 0, 150 + earSize, -earBeginAngle + -earWidth)
cursor.setposition(positionB[0], positionB[1])

positionC = positionAlongCircle(0, 0, 150, -earBeginAngle + -earWidth * 2)
cursor.setposition(positionC[0], positionC[1])

# Whiskers

whiskerLength = 180

# Right whiskers

movePen(cursor, 50, -15)
cursor.setheading(0)
cursor.forward(whiskerLength)

movePen(cursor, 50, 0)
cursor.left(5)
cursor.forward(whiskerLength)

# Left whiskers

movePen(cursor, -50, -15)
cursor.setheading(180)
cursor.forward(whiskerLength)

movePen(cursor, -50, 0)
cursor.left(-5)
cursor.forward(whiskerLength)

window.exitonclick()
