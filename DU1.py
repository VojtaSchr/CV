from turtle import backward, forward, goto, left, pen, pendown, penup, right, back, exitonclick, speed
import turtle

#nastavení herní plochy
zi=input("Jak velkou chcete stranu herního pole (max 10)?")
z=int(zi)
while z<=1 or z>=11:
    zi=input("Vložte pouze číslo od 2 do 10:")
    z=int(zi)
zs=str(z)

#posun želvy na začátek
turtle.speed(0)
penup()
goto(-250,250)
pendown()


#vykreslení herní plochy
for _o in range(z):
    for _i in range(z):
        for _p in range(4):
            forward(50)
            right(90)
        forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50*z)
    right(180)

zz=int((z*z)/2)    

for _i in range (zz):
    #křížek
    print("Hráč 1 je na tahu:")
    x=11111
    y=11111
    while x<=0 or x>=z+1:
        print("Vložte pouze číslo od 1 do "+zs)
        xi=input("Vložte sořadnici x:")
        x=int(xi)

    while y<=0 or y>=z+1:
        print("Vložte pouze číslo od 1 do "+zs)   
        yi=input("Vložte souřadnici y:")
        y=int(yi)

    penup()
    goto(-225+50*(x-1),225-50*(y-1))
    pendown()

    left(45)
    for _i in range (4):
        forward(20)
        backward(20)
        left(90)
    right(45)


    #kolečko
    print("Hráč 2 je na tahu:")
    x=11111
    y=11111
    while x<=0 or x>=z+1:
        print("Vložte pouze číslo od 1 do "+zs)
        xi=input("Vložte sořadnici x:")
        x=int(xi)

    while y<=0 or y>=z+1:
        print("Vložte pouze číslo od 1 do "+zs)   
        yi=input("Vložte souřadnici y:")
        y=int(yi)

    penup()
    goto(-225+50*(x-1),210-50*(y-1))
    pendown()

    for _i in range (40):
        forward(2)
        left(9)

print("Konec hry, hrací plocha zaplněna.")

exitonclick()