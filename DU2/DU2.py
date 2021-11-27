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
                    test1=float(row[5])                         #program zkusí převést údaj o průtoku na float a ověří tak, že se jedná o číslo
                except ValueError:                              #chybová hláška pokud nebude převod na float možný
                    print("Údaje o průtoku v csv souboru jsou poškozená (řádek "+str(it)+")")
    except PermissionError:                                     #chybová hláška pokud chybí oprávnění k souboru
        print("Program nemá oprávnění číst vstupní soubor")
    except FileNotFoundError:                                   #chybová hláška pokud se nepodaří najít vstupní soubor
        print("Program nemůže najít vstupní soubor, zkontrolujte, že jste zadali jeho jméno (případně cestu k němu) správně")
    return()

def AvgW(in_csv_W):                                             #výpočet 7denního průměru
    with open(in_csv_W, encoding= "utf-8") as csvinfile:        #otevření vstupního souboru, nastavení utf-8
        reader = csv.reader(csvinfile, delimiter = ",")
        iw=0                                                    #založení veličiny pro počítání cyklů
        ow=0
        jeden_tyden = float(0)                                  #nastavení veličiny pro součet průtoků za 7 dní na 0 a datový typ float 
        with open("vystup_7dni.csv",'w',newline="", encoding= "utf-8") as AvgW_Vystup:  #otevření souboru pro výstup
            csv.register_dialect("dialect1", delimiter=",")     #nastavení dialektu, údaje odděleny čárkami
            writer = csv.writer(AvgW_Vystup, dialect="dialect1")#proměnná writer pro zápis do souboru výstupu
            for row in reader:                                  #cyklus s počtem opakování rovným počtu řádků v csv souboru
                iw=iw+1
                jeden_tyden += float(row[5])                    #proměnná do které se vždy posčítá 7dní
                if iw%7==1:                                     #první den 7denního cyklu
                    datumW = ([row[0]] + [row[1]] + [row[2]] + [row[3]] + [row [4]])   #proměnná s datumem prvního měření 7denního cyklu
                if iw%7==0:                                     #poslední den 7denního cyklu
                    prumer_tyden = round(jeden_tyden/7, 4)      #výpočet průměrné hodnoty za 7 dní
                    jeden_tyden = 0                             #proměnná je po sedmi dnech vrácena na hodnotu nula
                    ow=ow+1
                    #print(prumer_tyden)
                    #writer.writerow(str(datum))
                    writer.writerow(datumW +[prumer_tyden])     #napsání data a průměru do výstupního csv souboru
            print("Počet záznamů v csv: " + str(iw))
            print("Počet 7denních průměrů: " + str(ow))
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
                    #print(prumer_rok)
                    writer.writerow(datumY+[prumer_rok])
            print("Počet záznamů v csv: "+ str(iy))
            print("Počet 7denních průměrů: " + str(oy))
    return()

Kontrola("vstup.csv")
AvgW("vstup.csv")
AvgY("vstup.csv")
