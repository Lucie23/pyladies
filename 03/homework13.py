from turtle import *
speed(0)
pensize(3)
bgcolor("black")

pencolor("green")
for k in range(20):
    for i in range(4):
        forward(150)
        left(360/4)
    left(18)

pencolor("red")
for k in range(20):
    circle(75)
    left(18)

pencolor("blue")
for k in range(20):
    for i in range(6):
        forward(50)
        left(360/6)
    left(18)

exitonclick()
