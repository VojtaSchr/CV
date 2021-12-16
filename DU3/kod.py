import json
from pyproj import Transformer
import math
import statistics

print("Program běží dokud nezahlásí: DONE")

def nacti_data(adresy, kontejnery):                     #Funkce na načtení dat ze souboru typu geojson
    try:
        with open(adresy, encoding="utf-8") as adresa:  #Načtení dat z souboru adress
            address_l = json.load(adresa)
            address = address_l["features"]             #Data jsou načtena do proměné address
    except FileNotFoundError:                           #Ošetření chyby vstupních dat
        print("Nepodařilo se najít soubor dat pro adresy. Zkontrolujte, že je vstupní soubor pojmenován správně")
        quit()
    except PermissionError:                             #Ošetření chyby vstupních dat
        print("Program nemá oprávnění číst soubor s daty adres.")
        quit()
    try:
        with open(kontejnery, encoding="utf-8") as kontejner:       #Načtení dat z souboru kontejnerů
            bins_l = json.load(kontejner)
            bins = bins_l["features"]                   #Data jsou načtena do proměné bins
    except FileNotFoundError:                           #Ošetření chyby vstupních dat
        print("Nepodařilo se najít soubor dat pro kontejnery. Zkontrolujte, že je vstupní soubor pojmenován správně.")
        quit()
    except PermissionError:                             #Ošetření chyby vstupních dat
        print("Program nemá oprávnění číst soubor s daty kontejnerů.")
        quit()
    print("Množství adres: "+str(len(address)))         #Vypsání množství adres
    print("Množství kontejnerů: "+str(len(bins)))       #Vypsání množství kontejnerů
    return(address, bins)

def typy_kontejneru(bins):                              #Funkce pro rozdělení kontejnerů na veřejné a privátní
    verejne_kontejnery = []                             #Slovník pro veřejné kontejnery
    privatni_kontejnery = []                            #Slovník pro privátní kontejnery
    for i in range (len(bins)):                         #Cyklus proběhne tolikrát, kolik máme kontejnerů a roztřídí kontejnery  
        bins_i = bins[i]                                #Voláme kontejnery po jednom
        if bins_i["properties"]["PRISTUP"] == "volně":  #Pokud je přistum uveden jako "volně", tak...
            verejne_kontejnery.append(bins_i)           #...přidáme kontejner do slovníku pro veřejné kontejnery
        elif bins_i["properties"]["PRISTUP"] == "obyvatelům domu": #Pokud je přistum uveden jako "obyvatelům domu", tak...
            privatni_kontejnery.append(bins_i)          #...přidáme kontejner do slovníku pro privátní kontejnery
        else:                                           #Ošetření chyby, pro případ kdy je jako přístup uvedeno 
                                                        #něco jiného než "volně" nebo "obyvatelům domu"
            print("V datech je chyba v určení přístupu k kontejnerům, program uznává pouze typy: "
                "volně nebo obyvatelům domu. Problém je u údaje na " +i+ " místě.")
    #print("Množství veřejných kontejnerů:"+str(len(verejne_kontejnery)))    #Možnost vypsání množství veřejných kontejnerů
    #print("Množství privátních kontejnerů:"+str(len(privatni_kontejnery)))  #Možnost vypsání množství privátních kontejnerů
    return(verejne_kontejnery,privatni_kontejnery)

def WGS_to_JTSK(x,y):                                   #Funkce pro převod souřadnic z WGS84 do S-JTSK
    wgs = Transformer.from_crs(4326, 5514, always_xy = True)    #Pro převod použijeme funkci Transformer
    jtsk = wgs.transform(x,y)                           #Souřadnice ve formátu jtsk se uloží do proměnné jtsk
    return(jtsk)

def typy_adres():                                       #Funkce třídící adresy na adresy s privátním kontejnerm a bez něj
    adresy_s_kon=[]
    adresy_bez_kon=[]
    stoper=0                                            #Nadefinuje se proměnná, která zastaví hledání, když je objeven privátní kontejner
    for a1 in range(len(address)):                      #Cyklus proběhne tolikrát, kolik máme adres 
        adresa_a1=address[a1]                           #Jedna adresa se nahraje do proměnné
        try:                           
            ulice_a = str(adresa_a1["properties"]["addr:street"])           #Do proměnné se uloží jméno ulice adresy
            dom_cislo_a = str(adresa_a1["properties"]["addr:housenumber"])  #Do proměnné se uloží domovní číslo adresy
        except:                                         #Ošetření chyby vstupních dat
            print("Nepodařilo se načíst údaje o ulici a domovním čísle "+int(a1)+". adresy.")
            quit()
        stoper=0                                        #Hodnota proměnné pro zastavení hledání se vrátí na nulu
        for a2 in range(len(privatni_kontejnery)):
            if stoper!=1:                               #Pokud se stoper nerovná nule proběhnou následující řádky které hledají jestli...
                                                        #...nemá dům privátní kontejner. Pokud je stoper 1 znamená to, že privátní...
                                                        #...kontejner byl již nalezen a není ho potřeba dále hledat
                kontejner_a2=bins[a2]
                ulice_b = str(kontejner_a2["properties"]["STATIONNAME"]) #Nahraje do promněnné údaje o umístění kontejneru
                if (ulice_b.find(ulice_a)!=-1):         #Zjištuje zda-li se shoduje jméno ulice adresy s umístěním kontejneru
                    if (ulice_b.find(dom_cislo_a)!=-1): #Zjištuje zda-li se shoduje číslo domu adresy s umístěním kontejneru
                        adresy_s_kon.append(adresa_a1)  #Nalezená adresa s privátním kontejnerem se nahraje do seznamu adres s priv. kont.
                        stoper=1
        if stoper !=1:                                  #Pokud není nalezena privátní adresa...
            adresy_bez_kon.append(adresa_a1)            #...dojde k zapsání do seznamu adres nez privátního kontejneru
    #print("Množství adres závyslých na veřejných kontejnerech:"+str(len(adresy_bez_kon)))    #Možnost vypsání množství adres... 
                                                                                              #...bez privátního kontejneru
    #print("Množství adres s privátním kontejnerem:"+str(len(adresy_s_kon)))     #Možnost vypsání množství adres s privátním kontejnerem
    return(adresy_s_kon, adresy_bez_kon)

def vzdalenost(xa,ya,xb,yb):                            #Funkce pro výpočet vzdálenosti dvou bodů
                                                        #xa..x-ová souřadnice adresy, ya..y-ová souřadnice adresy
                                                        #xb..x-ová souřadnice kontejneru, yb..y-ová souřadnice kontejneru
    vzdal=math.sqrt((xa-xb)**2+(ya-yb)**2)              #Vypočteno jako přepona pravoúhlého trojúhelniku, nahráno jako proměnná vzdal
    return(vzdal)


address, bins = nacti_data("adresy.geojson", "kontejnery.geojson")
verejne_kontejnery, privatni_kontejnery = typy_kontejneru(bins)
adresy_s_kon, adresy_bez_kon = typy_adres()


list_vzdalenosti=[]
max_vzdal=0                                             #vytvoření proměnné pro největší vzdálenost

for b1 in range (len(adresy_bez_kon)):                  #počet opakování rovný počtu adres domů bez privátního kontejneru
    adresa_b1 = adresy_bez_kon[b1]                      #každé opakování se vytvoží proměnná s jednou adresou
    try:
        jtsk_sou = WGS_to_JTSK(*adresa_b1["geometry"]["coordinates"])   #provede se převod soužadnic adresy na jtsk
        adresa_b1["geometry"]["coordinates"] = jtsk_sou     #převedené soužadnice se uloží do adresy, nahradí WGS souřadnice
    except KeyError:
        print("Soubor adres neobsahuje souřadnice s polohou adres nebo jsou špatně zařazené")
        quit()
    min_vzdal=1000000                                   #vytvoření neznámé pro vzdálenost jedné adresy od nejbližšího kontejneru
    for b2 in range (len(verejne_kontejnery)):          #cyklus s počtem opakování rovným počtu veřejně dostupných kontejnerů...
        kontejner_b2 = verejne_kontejnery[b2]           #každé opakování se vytvoží proměnná s jedním kontejnerem
        vzdal=vzdalenost(*adresa_b1["geometry"]["coordinates"], *kontejner_b2["geometry"]["coordinates"]) #výpočet vzdálenosti...
                                                        #...mezi kontejnerem a adresou
        if min_vzdal>vzdal:                             #vyhledání nejbližšího kontejneru
            min_vzdal=int(vzdal)
    if max_vzdal<min_vzdal:                             #vyhledání největší vzdálenosti adresy od kontejneru
        max_vzdal=min_vzdal
        adresa_max_vzdal= {adresa_b1["properties"]["addr:street"],adresa_b1["properties"]["addr:housenumber"]} #uložení...
                                                                        #...adresy s největší vzdáleností od kontejneru
    list_vzdalenosti.append(min_vzdal)                  #list se vzdálenostmi adres od nejbližších kontejnerů

avg_vzdal=sum(list_vzdalenosti)/len(list_vzdalenosti)   #výpočet aritmetického průměru hodnot vzdáleností
avg_vzdal_zaok=round(avg_vzdal, 1)                      #zapkrouhlení průměru na desetiny
print("Průměrná vzdálenost ke kontejneru je: "+str(avg_vzdal_zaok)+" m.")
print("Nejdéle ke kontejneru je z adresy "+str(adresa_max_vzdal)+" a to "+ str(max_vzdal)+" m.")        
median=statistics.median(list_vzdalenosti)              #hledání mediánu
print("Median vzdáleností je: "+str(median)+" m.")
print("DONE")  