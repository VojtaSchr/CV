from random import randrange

x=11
pv=input("Od jedničky do kolika chcete hádat:")
p=int(10)
#pp=str(p)
r=randrange(p)+1

#r=5

while x!=r:
    y=input("Hadej cislo od 1 do "+pv+":")
    x=int(y)
    if x<r:
        print("Hledané číslo je vyšší")
    elif x>r:
        print("Hledané číslo je menší")
    if x==r+(p//10) or x==r-(p//10):
        print("Ale bylo to těsně")
print("Máš to!!!")

print("A je to")