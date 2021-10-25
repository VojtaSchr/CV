from math import sqrt
#1+2
#print(1+2)
#print("Ahoj")
#print("Čtverec o straně 479 má obvod", 479*4, "a obsah", 479**2)
#x1=479
#print("Čtverec o straně 479 má obvod", x1*4, "a obsah", x1**2)
#strana_čtverce=479
#print("Čtverec o straně 479 má obvod", strana_čtverce*4, "a obsah", strana_čtverce**2)
poloměr=1
pí=3.1415
if poloměr<=0:
    print("chyba")
else: print("Obvod kruhu je", 2*pí*poloměr, "a obsah", pí*poloměr**2)

a=3
b=4
c=1
D=b**2 - 4*a*c
if (D<0):
    print ("Rovnice nemá řešení")
elif (D==0):
    x=(-b/(2*a))
    print ("Výsledek",x)
else:
    x=((-b-sqrt(D))/(a*2))
    y=((-b+sqrt(D))/(a*2))
    print(x,y)
