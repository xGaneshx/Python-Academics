import turtle
t=turtle.Turtle()
def square(dist,angle):
    for i in range(4):
       t.forward(dist)
       t.right(angle)
square(100,90)
t.circle(10)
turtle.done()