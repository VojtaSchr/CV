def readint():
    y=0
    while y!=1:
        xi=input("Vložte celé číslo:")
        try:
            x=int(xi)
            y=1
        except ValueError:
            print("Vkládejte POUZE CELÁ ČÍSLA!")
    return (x)

z=str(readint())
print("Vaše celé číslo je: " +z)