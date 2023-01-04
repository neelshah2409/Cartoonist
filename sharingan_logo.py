from turtle import *
pencolor('red')
dot(750)
pencolor('black')
dot(500)
pencolor('red')
dot(475)
#Function For Curve
def curve01(a,d):
    for i in range(d):
        right(a)
        forward(1)
def curve02(a,d):
    for i in range(d):
        left(a)
        forward(1)
pencolor('black')
#Function for Sharingan
def shr(n,p):
    right(n)
    penup()
    forward(230)
    pendown()
    right(p)
    fillcolor('black')
    begin_fill()
    curve02(1.3,200)
    right(125)
    curve01(1,60)
    left(160)
    curve02(0.85,180)
    end_fill()
#Calling Sharingan
shr(200,200)
penup()
home()
pendown()
#Calling Sharingan
shr(-15,200)
penup()
home()
pendown()
#Calling Sharingan
shr(90,200)
done()
