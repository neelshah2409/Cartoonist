import turtle

yy = turtle.Turtle()
yy.speed('fastest')

window = turtle.Screen()
window.title("YinYang")
window.bgcolor("#ff704d")

def yinyang(radius, color1, color2):
    yy.width(3)
    yy.color(color1, color1)
    yy.begin_fill()
    yy.circle(radius/2., 180)
    yy.circle(radius, 180)
    yy.left(180)
    yy.circle(-radius/2., 180)
    yy.end_fill()
    yy.left(90)
    yy.up()
    yy.forward(radius*0.35)
    yy.right(90)
    yy.down()
    yy.color(color2, color2)
    yy.begin_fill()
    yy.circle(radius*0.15)
    yy.end_fill()
    yy.left(90)
    yy.up()
    yy.backward(radius*0.35)
    yy.down()
    yy.left(90)

def main():
    yy.reset()
    yinyang(200, "black", "white")
    yinyang(200, "white", "black")
    yy.showturtle()
    return "yinyang"

if __name__ == '__main__':
    main()
turtle.done()
