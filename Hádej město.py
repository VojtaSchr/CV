import random

a=["a","š"]
b=["b","r","n","o"]
c=["c","v","i","k","o","v"]
d=list("děčín")
f=["f","r","ý","d","l","a","n","d"]

mesto = random.choice([a,b,c,d,f])
print(mesto)
delka = len(mesto)
print(delka)

podt=list()

for _ in range(delka):
    podt.append("_") 
print(podt)

def hadej_pismeno ():
    pismeno=input("Hádejte písmeno: ")
    print(pismeno)
    for (idx,val) in enumerate(mesto):
        print("index: "+str(idx) +"  val: " +str(val))
    _x=mesto.index(pismeno)
    print(_x)

    podt[_x] =pismeno
    print(podt)

while "_" in podt:
    hadej_pismeno()
else:
    print("HOTOVO")