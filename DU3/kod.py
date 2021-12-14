import json
from pyproj import Transformer


def nacti_data(adresy, kontejnery):
    try:
        with open(adresy, encoding="utf-8") as adresa:
            address_l = json.load(adresa)
            address = address_l["features"]
    except:
        print("Nepodařilo se načíst data adres.")
    try:
        with open(kontejnery, encoding="utf-8") as kontejner:
            bins_l = json.load(kontejner)
            bins = bins_l["features"]
        #with open("test.geojson","w", encoding="utf-8") as testS:
            #json.dump(address, testS, indent=4)
    except:
        print("Nepodařilo se načíst data kontejnerů.")
    return(address, bins)

def WGS_to_JTSK(x,y):
    wgs = Transformer.from_crs(4326, 5514, always_xy = True)
    jtsk = wgs.transform(x,y)
    print(jtsk)
    return(jtsk)

def typy_kontejneru(bins):
    verejne_kontejnery = []
    privatni_kontejnery = []
    
    for i in range (len(bins)):  
        bins_i = bins[i]
        if bins_i["properties"]["PRISTUP"] == "volně": 
            verejne_kontejnery.append(bins_i)

        elif bins_i["properties"]["PRISTUP"] == "obyvatelům domu":
            privatni_kontejnery.append(bins_i)
        
        else:
            print("V datech je chyba v určení přístupu k kontejnerům, program uznává pouze typy: volně nebo obyvatelům domu.")
    return(verejne_kontejnery,privatni_kontejnery)


nacti_data("adresy.geojson", "kontejnery.geojson")
WGS_to_JTSK(0,0)
