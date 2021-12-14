import turtle

delka = int(input("Zvolte délku: ")) *3
uroven = int(input("Nastavte úroveň: "))

def vlocka(d,u):
    i=0
    x=0
    y=0
    if u>0:
        i+=1
        a=d/(3*i)
        u=u-1
        def zub(a):
            turtle.forward(a)
            turtle.left(60)
            turtle.forward(a)
            turtle.right(120)
            turtle.forward(a)
            turtle.left(60)
            turtle.forward(a)
        
    turtle.exitonclick()
    return()

vlocka(delka,uroven)