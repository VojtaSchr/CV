with open("C:\\Users\\schre\\Desktop\\Úvod do programování\\pozn..txt", encoding="utf-8") as f:
    obsah = f.read()
    print(obsah)

with open("C:\\Users\\schre\\Desktop\\Úvod do programování\\poznVystup.txt", mode="W", encoding="utf-8") as g:
    g.write ("ahoj")
    obsah2 = g.read()
    print(obsah2)
