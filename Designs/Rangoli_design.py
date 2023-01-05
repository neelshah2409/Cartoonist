import turtle as tur
import colorsys as cs

tur.setup(600,600)
tur.speed(0)
tur.width(2)
tur.bgcolor("black")
for j in range(15):
  for i in range(10):
    tur.pensize(j)
    tur.color(cs.hsv_to_rgb(i/15,j/15,1))
    tur.right(90)
    tur.circle(200-j*4,90)
    tur.left(90)
    tur.circle(200-j*4,90)
    tur.right(360)
    tur.circle(50,24)
tur.circle(50,24)
tur.hideturtle()
tur.done
