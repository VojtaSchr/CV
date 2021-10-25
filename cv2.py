from math import sqrt

#prevod casu na radek
print(int(input("stupne:"))+int(input("minuty:"))/60+int(input("vteriny:"))/3600)

#prevod casu
st_z=input("Zadejte stupně:")
min_z=input("Zadejte minuty:")
vt_z=input("Zadejte vteřiny:")


st=int(st_z)
if st<-180 or st>180: 
    print("Zadejte hodnotu stupňů mezi -180 a 180.") 
    quit()
min=int(min_z)
if min<=0 or min>=60: 
     print("Zadejte hodnotu minut mezi 0 a 60.") 
     quit()
    
vt=float(vt_z)
if vt<=0 or vt>=60: 
    print("Zadejte hodnotu vteřin mezi 0 a 60.") 
    quit()

j=st+min/60+vt/3600
print(j)

deg_z=input("Zapište údaj:")

deg=float(deg_z)
if deg<0 or deg>360:
    print("Zadejte hodnotu správně")
    quit()
st_deg=deg//1
minvt_deg=deg-st_deg
min_deg2 = minvt_deg*60
min_deg=int(min_deg2)
vt_deg2= min_deg2-min_deg
vt_deg=vt_deg2*60

print(type(st_deg))

print(st_deg)
print(min_deg)
print(vt_deg)



#c=input("zč:")
#print(c)
#print(type(c))

av=input("Zadejte kořen a:")
bv=input("Zadejte kořen a:")
cv=input("Zadejte kořen a:")

a=int(av)
b=int(bv)
c=int(cv)


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