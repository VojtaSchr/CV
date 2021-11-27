import csv
from os import execlp, write

def Kontrola(in_csv_k): #kontroluje výskyt chyb ve vstupním souboru
    try:
        with open(in_csv_k, encoding= "utf-8") as csvinfile:    #otevře vstupní soubor
            reader = csv.reader(csvinfile, delimiter = ",")
            it=0                                                #proměnná počítající řádky pro ValueError
            for row in reader:                                  #cyklus s počtem opakování rovným počtu řádků v csv souboru
                it=it+1                                         #hodnota proměnné počítající řádky se zvýší jedna 
                try:
                    test1=float(row[5])
                except ValueError:
                    print("Údaje o průtoku v csv souboru jsou poškozená (řádek "+str(it)+")")
    except PermissionError:
        print("Program nemá oprávnění číst vstupní soubor")
    except FileNotFoundError:
        print("Program nemůže najít vstupní soubor, zkontrolujte, že jste zadali jeho jméno (případně cestu k němu) správně")
    return()

def AvgW(in_csv_W):
    with open(in_csv_W, encoding= "utf-8") as csvinfile:
        reader = csv.reader(csvinfile, delimiter = ",")
        iw=0
        ow=0
        jeden_tyden = float(0)
        with open("vystup_7dni.csv",'w',newline="", encoding= "utf-8") as AvgW_Vystup:
            csv.register_dialect("dialect1", delimiter=",")
            writer = csv.writer(AvgW_Vystup, dialect="dialect1")
            for row in reader:
                iw=iw+1
                jeden_tyden += float(row[5])
                if iw%7==1:
                    datumW = ([row[0]] + [row[1]] + [row[2]] + [row[3]] + [row [4]])   
                if iw%7==0:
                    prumer_tyden = round(jeden_tyden/7, 4)
                    jeden_tyden = 0
                    ow=ow+1
                    print(prumer_tyden)
                    #writer.writerow(str(datum))
                    writer.writerow(datumW +[prumer_tyden])
            print(iw)
            print(ow)
    return()

def AvgY(in_csv_Y):
    with open(in_csv_Y, encoding= "utf-8") as csvinfile:
        reader = csv.reader(csvinfile, delimiter = ",")
        iy=0
        oy=0
        jeden_rok = float(0)
        with open("vystup_rok.csv",'w',newline="", encoding= "utf-8") as AvgY_Vystup:
            csv.register_dialect("dialect1", delimiter=",")
            writer = csv.writer(AvgY_Vystup, dialect="dialect1")
            for row in reader:
                iy=iy+1
                jeden_rok += float(row[5])       
                if iy%365==0:
                    prumer_rok = round(jeden_rok/365, 4)
                    datumY = ([row[0]] + [row[1]] + [row[2]])
                    jeden_rok = 0
                    oy=oy+1
                    print(prumer_rok)
                    writer.writerow(datumY+[prumer_rok])
            print(iy)
            print(oy)
    return()

Kontrola("vstup.csv")
AvgW("vstup.csv")
AvgY("vstup.csv")
