import json
from pyproj import Transformer
import math


def nacti_data(adresy, kontejnery):                     #Funkce na načtení dat ze souboru typu geojson
    try:
        with open(adresy, encoding="utf-8") as adresa:  #Načtení dat z souboru adress
            address_l = json.load(adresa)
            address = address_l["features"]             #Data jsou načtena do proměné address
    except:                                             #Ošetření chyby vstupních dat
        print("Nepodařilo se načíst data adres.")
        quit()
    try:
        with open(kontejnery, encoding="utf-8") as kontejner:       #Načtení dat z souboru kontejnerů
            bins_l = json.load(kontejner)
            bins = bins_l["features"]                   #Data jsou načtena do proměné bins
    except:                                             #Ošetření chyby vstupních dat
        print("Nepodařilo se načíst data kontejnerů.")
        quit()
    print("Množství adres: "+str(len(address)))         #Vypsání množství adres
    print("Množství kontejnerů: "+str(len(bins)))       #Vypsání množství kontejnerů
    return(address, bins)

def typy_kontejneru(bins):                              #Funkce pro rozdělení kontejnerů na veřejné a privátní
    verejne_kontejnery = []                             #Slovník pro veřejné kontejnery
    privatni_kontejnery = []                            #Slovník pro privátní kontejnery
    
    for i in range (len(bins)):                         #Funkce proběhne tolikrát, kolik míme kontejnerů a roztřídí kontejnery  
        bins_i = bins[i]                                #Voláme kontejnery po jednom
        if bins_i["properties"]["PRISTUP"] == "volně":  #Pokud je přistum uveden jako "volně", tak...
            verejne_kontejnery.append(bins_i)           #...přidáme kontejner do slovníku pro veřejné kontejnery

        elif bins_i["properties"]["PRISTUP"] == "obyvatelům domu": #Pokud je přistum uveden jako "obyvatelům domu", tak...
            privatni_kontejnery.append(bins_i)          #...přidáme kontejner do slovníku pro privátní kontejnery
        
        else:                                           #Ošetření chyby, pro případ kdy je jako přístup uvedeno 
                                                        #něco jiného než "volně" nebo "obyvatelům domu"
            print("V datech je chyba v určení přístupu k kontejnerům, program uznává pouze typy: "
                "volně nebo obyvatelům domu. Problém je u údaje na " +i+ " místě.")
    print("Množství veřejných kontejnerů:"+str(len(verejne_kontejnery)))    #Vypsání množství veřejných kontejnerů
    print("Množství privátních kontejnerů:"+str(len(privatni_kontejnery)))  #Vypsání množství privátních kontejnerů
    return(verejne_kontejnery,privatni_kontejnery)

def WGS_to_JTSK(x,y):                                   #Funkce pro převod souřadnic z WGS84 do S-JTSK
    wgs = Transformer.from_crs(4326, 5514, always_xy = True)    #Pro převod použijeme funkci Transformer
    jtsk = wgs.transform(x,y)                           #Souřadnice ve formátu jtsk se uloží do proměnné jtsk
    #print(jtsk)
    return(jtsk)

def vzdalenost(xa,ya,xb,yb):                            #Funkce pro výpočet vzdálenosti dvou bodů
                                                        #xa..x-ová souřadnice adresy, ya..y-ová souřadnice adresy
                                                        #xb..x-ová souřadnice kontejneru, yb..y-ová souřadnice kontejneru
    vzdal=math.sqrt((xa-xb)**2+(ya-yb)**2)              #Vypočteno jako přepona pravoúhlého trojúhelniku, nahráno jako proměnná vzdal
    print(vzdal)
    return(vzdal)

#def typy_adres()

address, bins = nacti_data("adresy.geojson", "kontejnery.geojson")
#WGS_to_JTSK(0,0)
verejne_kontejnery, privatni_kontejnery = typy_kontejneru(bins)
vzdalenost(5,7,2,3)