from turtle import *

colors=[ '#f5480f','#2aad21','#288cf7','#ffcc00']

pos = [(0,0),(100,0),(0,-100),(100,-100)]

for (x,y),color in zip(pos, colors):
  up()
  goto(x,y)
  down()
  fillcolor(color)
  begin_fill()
  for i in range(4):
    forward(90)
    right(90)
  end_fill()