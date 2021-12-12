import json

def nacti_data(adresy, kontejnery):
    with open(adresy, encoding="utf-8") as adresa:
        address = json.load(adresa)
    with open(kontejnery, encoding="utf-8") as kontejner:
        bins = json.load(kontejner)
    #with open("test.geojson","w", encoding="utf-8") as testS:
        #json.dump(address, testS, indent=4)
    return(address,bins)

nacti_data("adresy.geojson", "kontejnery.geojson")
