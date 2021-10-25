from turtle import forward, left, pen, pendown, penup, right, back, exitonclick, speed
import turtle

speed(0)

forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

left(60)
forward(50)
left(60)
forward(50)
left(60)
forward(50)
left(60)
forward(50)
left(60)
forward(50)
left(60)
forward(50)


for _i in range(9):
    left(40)
    forward(50)

for _i in range(12):
    left(30)
    forward(50)

penup()
right(90)
forward(200)
pendown()

for _o in range(6):
    for _i in range(6):
        left(60)
        forward(30)
    right(60)
    forward(30)

left(60)
forward(30)
left(60)
forward(30)
left (60)
forward(15)

right(90)
forward(100)
right(120)

for _o in range(2):
    for _i in range(2):
        forward(50)
        left(30)
        forward(50)
        left(150)
    right(150)




exitonclick()
