from math import pi


def r_kruhu(r):
    s=pi*r*r
    return(s)

ri=input("Vložte poloměr")
r=float(ri)
x=r_kruhu(r)
print(x)