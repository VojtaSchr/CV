from turtle import forward, goto, left, pen, pendown, penup, right, back, exitonclick, speed
import turtle

turtle.speed(1)

for _o in range(3):
    for _i in range(3):
        for _p in range(4):
            forward(50)
            left(90)
        forward(50)
    left(90)
    forward(50)
    left(90)
    forward(150)
    left(180)

#xi=input("Vložte x")
#x=int(xi)
x=11111
y=11111

while x!=1 and x!=2 and x!=3:
    print("Vložte pouze číslo 1, 2 nebo 3")
    xi=input("Vložte sořadnici x:")
    x=int(xi)

while x!=1 and x!=2 and x!=3:
    print("Vložte pouze číslo 1, 2 nebo 3")   
    yi=input("Vložte souřadnici y")
    y=int(yi)




exitonclick()
