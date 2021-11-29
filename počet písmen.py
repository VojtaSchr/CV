slovoin=input("Zadejte slovo: ")

slovo=list(slovoin)
slovnik={}
slovolen=int(len(slovo))
x=slovolen
print(slovo)
i=0


def pocet_pismen (pismeno):
    print(pismeno)
    for (idx,val) in enumerate(slovo):
        print("index: "+str(idx) +"  val: " +str(val))
    _x=slovo.index(pismeno)
    print(pismeno + str(_x))
    return()

for i in range(slovolen):
    a=slovo[i]
    print(a)
    if a in slovnik:
        slovnik[a]+=1
    else:
        slovnik[a]=1


print(slovnik)
