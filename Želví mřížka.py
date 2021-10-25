from turtle import forward, goto, left, pen, pendown, penup, right, back, exitonclick, speed
import turtle

speed(0)

xi=input("Zadejte rozměr x:")
yi=input("Zadejte rozměr y:")

x=int(xi)
y=int(yi)

penup()
goto(-300,-250)
pendown()

a=600//x

for _o in range(500//y):
    for _i in range(600//x):
        for _p in range(2):
            forward(x)
            left(90)
            forward(y)
            left(90)
        forward(x)
    left(90)
    forward(y)
    left(90)
    forward(a*x)
    left(180)


exitonclick()