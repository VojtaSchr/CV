from turtle import backward, forward, goto, left, pen, pendown, penup, right, back, exitonclick, speed
import turtle

z=11111

#nastavení herní plochy
print("Jak velkou chcete stranu herního pole.")

while z<=1 or z>=11:
    zi=input("Vložte pouze číslo od 2 do 10:")
    try:
        z=int(zi)
    except ValueError:
        print("POUZE CELÁ ČÍSLA!")
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

#funkce vykreslení křížku a kolečka
def krizek ():
    #křížek
    print("Hráč 1 je na tahu:")
    x=11111
    y=11111
    while x<=0 or x>=z+1:
        print("Vložte pouze číslo od 1 do "+zs)
        xi=input("Vložte souřadnici x:")
        try:
            x=int(xi)
        except ValueError:
            print("POUZE CELÁ ČÍSLA!")

    while y<=0 or y>=z+1:
        print("Vložte pouze číslo od 1 do "+zs)   
        yi=input("Vložte souřadnici y:")
        try:
            y=int(yi)
        except ValueError:
            print("POUZE CELÁ ČÍSLA!")

    penup()
    goto(-225+50*(x-1),225-50*(y-1))
    pendown()

    left(45)
    for _i in range (4):
        forward(20)
        backward(20)
        left(90)
    right(45)
    return

def kolecko ():
    print("Hráč 2 je na tahu:")
    x2=1111
    y2=1111
    while x2<=0 or x2>=z+1:
        print("Vložte pouze číslo od 1 do "+zs)
        xi=input("Vložte souřadnici x:")
        try:
            x2=int(xi)
        except ValueError:
            print("POUZE CELÁ ČÍSLA!")

    while y2<=0 or y2>=z+1:
        print("Vložte pouze číslo od 1 do "+zs)   
        yi=input("Vložte souřadnici y:")
        try:
            y2=int(yi)
        except ValueError:
            print("POUZE CELÁ ČÍSLA!")

    penup()
    goto(-225+50*(x2-1),210-50*(y2-1))
    pendown()

    for _i in range (40):
        forward(2)
        left(9)

    return


if z%2==0:

    for _i in range (zz):
        krizek()
        kolecko()

else:
    
    krizek()
    
    for _i in range (zz):
        kolecko()
        krizek()

print("Konec hry, hrací plocha zaplněna.")

exitonclick()