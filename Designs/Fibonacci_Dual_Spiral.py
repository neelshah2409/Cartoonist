import turtle

colors = [
    "#ca5cdd",    #For Purple
    "#4949FF",    #For Blue
    "#A4DE02",    #For Green
    "#FFF44F",    #For Yellow
    "#ff2400",    #For Red
    "#ff2400",
    "#ff2400",
    "#ff2400",
    "#ff2400",
    "#ff2400",
    "#ff2400",
    "#ff2400",
    "#FFF44F",
    "#A4DE02",
    "#4949FF",
    "#ca5cdd"
]

wn = turtle.Screen()

wn.title("Fibonacci Dual Spring")
wn.bgcolor("Black")
turtle.speed(0)

for i in range(24):
    
    angle = 360/len(colors)
    
    turtle.width(1.5)

    for color in colors:
        turtle.color(color)
        turtle.circle(100, angle)
        
    turtle.left(15)
    

turtle.hideturtle()

turtle.done()