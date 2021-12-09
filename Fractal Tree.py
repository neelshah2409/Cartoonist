import turtle
#creating object for this turtle
tu = turtle.Turtle()
tu.screen.bgcolor("black") #background color
tu.pensize(2) #pen size
tu.color("green") #intial color

tu.left(90)
# the tree will go in upward direction
tu.backward(100)
tu.speed(200) #speed of turtle
tu.shape('turtle') 

#using recurssion function to draw the tree 
def tree(i):
    if i<10:
        return
        #base condition to stop recursion 
    else:
        tu.forward(i)
        tu.color("orange")
        tu.circle(2)
        tu.color("brown")
        tu.left(30)
        tree(3*i/4)
        tu.right(60)
        tree(3*i/4)
        tu.left(30)
        tu.backward(i)
tree(100)
turtle.done()
