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