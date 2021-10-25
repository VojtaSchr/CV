from turtle import forward, goto, left, pen, pendown, penup, right, back, exitonclick, speed
import turtle

speed(1)

xi=input("Zadejte počet šestiúhelníků v rozměru x:")
yi=input("Zadejte počet šestiúhelníků v rozměru y:")

x=int(xi)
y=int(yi)

penup()
goto(-200,-150)
right(90)
pendown()

for _o in range(x):
    for _i in range(3):
        left(60)
        forward(30)
    right(180)
    

left(60)
forward(30)
left(60)
forward(30)
left (60)
forward(15)


exitonclick()