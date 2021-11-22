slovoin=input("Zadejte slovo: ")

slovo=list(slovoin)
slovolen=len(slovo)
print(slovo)

def pocet_pismen (pismeno):
    print(pismeno)
    for (idx,val) in enumerate(slovo):
        print("index: "+str(idx) +"  val: " +str(val))
    _x=slovo.index(pismeno)
    print(pismeno + str(_x))

if _i in range slovolen:
    pismeno = slovo[i]
    pocet_pismen