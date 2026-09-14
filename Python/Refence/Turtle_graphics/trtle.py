import turtle
fred = turtle.Turtle()
turtle.speed(speed=0)
def shape(sides,dst,fillc):
    for i in range (sides):
        fred.fillcolor(fillc)
        fred.begin_fill()
        fred.fd (dst)
        fred.lt (360/sides)
        fred.end_fill()

shape(10,100,"green")
