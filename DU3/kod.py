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

def typy_adres():
    adresy_s_kon=[]
    adresy_bez_kon=[]
    stoper=0
    for a1 in range(len(address)):
        adresa_a1=address[a1]
        ulice_a = str(adresa_a1["properties"]["addr:street"])
        dom_cislo_a = str(adresa_a1["properties"]["addr:housenumber"])
        stoper=0
        mover=1
        for a2 in range(len(privatni_kontejnery)):
            if stoper!=1:
                mover+=1
                kontejner_a2=bins[a2]
                ulice_b = str(kontejner_a2["properties"]["STATIONNAME"])
                if (ulice_b.find(ulice_a)!=-1):
                    if (ulice_b.find(dom_cislo_a)!=-1):
                        adresy_s_kon.append(adresa_a1)
                        stoper=1
        if stoper !=1:
            adresy_bez_kon.append(adresa_a1)
    print("Množství adres závyslích na veřejných kontejnerech:"+str(len(adresy_bez_kon)))    #Vypsání množství adres 
                                                                                             #bez privátního kontejneru
    print("Množství adres s privátním kontejnerem:"+str(len(adresy_s_kon)))     #Vypsání množství adres s privátním kontejnerem
    return(adresy_s_kon, adresy_bez_kon)

def vzdalenost(xa,ya,xb,yb):                            #Funkce pro výpočet vzdálenosti dvou bodů
                                                        #xa..x-ová souřadnice adresy, ya..y-ová souřadnice adresy
                                                        #xb..x-ová souřadnice kontejneru, yb..y-ová souřadnice kontejneru
    vzdal=math.sqrt((xa-xb)**2+(ya-yb)**2)              #Vypočteno jako přepona pravoúhlého trojúhelniku, nahráno jako proměnná vzdal
    print(vzdal)
    return(vzdal)


address, bins = nacti_data("adresy.geojson", "kontejnery.geojson")
#WGS_to_JTSK(0,0)
verejne_kontejnery, privatni_kontejnery = typy_kontejneru(bins)
adresy_s_kon, adresy_bez_kon = typy_adres()
vzdalenost(5,7,2,3)