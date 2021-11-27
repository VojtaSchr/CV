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
        iw=0                                                    #založení veličiny pro počítadlo množství zpracovávaných záznamů v csv
        ow=0                                                    #založení veličiny pro počítadlo množství 7denních průměrů
        jeden_tyden = float(0)                                  #nastavení veličiny pro součet průtoků za 7 dní na 0 a datový typ float 
        with open("vystup_7dni.csv",'w',newline="", encoding= "utf-8") as AvgW_Vystup:  #otevření souboru pro výstup
            csv.register_dialect("dialect1", delimiter=",")     #nastavení dialektu, údaje odděleny čárkami
            writer = csv.writer(AvgW_Vystup, dialect="dialect1")#proměnná writer pro zápis do souboru výstupu
            for row in reader:                                  #cyklus s počtem opakování rovným počtu řádků v csv souboru
                iw=iw+1                                         #počítadlo množství zpracovávaných záznamů v csv
                jeden_tyden += float(row[5])                    #proměnná do které se vždy posčítá 7dní
                if iw%7==1:                                     #první den 7denního cyklu
                    datumW = ([row[0]] + [row[1]] + [row[2]] + [row[3]] + [row [4]])   #proměnná s datumem prvního měření 7denního cyklu
                if iw%7==0:                                     #poslední den 7denního cyklu
                    prumer_tyden = round(jeden_tyden/7, 4)      #výpočet průměrné hodnoty za 7 dní
                    jeden_tyden = 0                             #proměnná je po sedmi dnech vrácena na hodnotu nula
                    ow=ow+1                                     #počítadlo množství 7denních průměrů
                    writer.writerow(datumW +[prumer_tyden])     #napsání data a průměru do výstupního csv souboru
            print("Počet záznamů v csv: " + str(iw))            #kontrolní výpis do konzole
            print("Počet 7denních průměrů: " + str(ow))         #kontrolní výpis do konzole
    return()

def AvgY(in_csv_Y):                                             #výpočet ročního průměru
    with open(in_csv_Y, encoding= "utf-8") as csvinfile:        #otevření vstupního souboru, nastavení utf-8
        reader = csv.reader(csvinfile, delimiter = ",")
        iy=0                                                    #založení veličiny pro počítadlo množství zpracovávaných záznamů v csv
        oy=0                                                    #založení veličiny pro počítadlo množství ročních průměrů
        jeden_rok = float(0)                                    #nastavení veličiny pro součet průtoků za 365 dní na 0 a datový typ float
        with open("vystup_rok.csv",'w',newline="", encoding= "utf-8") as AvgY_Vystup:   #otevření souboru pro výstup
            csv.register_dialect("dialect1", delimiter=",")     #nastavení dialektu, údaje odděleny čárkami
            writer = csv.writer(AvgY_Vystup, dialect="dialect1")#proměnná writer pro zápis do souboru výstupu
            for row in reader:                                  #cyklus s počtem opakování rovným počtu řádků v csv souboru
                iy=iy+1                                         #počítadlo množství zpracovávaných záznamů v csv
                jeden_rok += float(row[5])                      #proměnná do které se vždy posčítá 365dní
                if iy%365==1:                                   #první den 365denního cyklu
                    datumY = ([row[0]] + [row[1]] + [row[2]] + [row[3]] + [row [4]])   #proměnná s datumem prvního měření 7denního cyklu
                if iy%365==0:                                   #poslední den 365denního cyklu
                    prumer_rok = round(jeden_rok/365, 4)        #výpočet průměrné hodnoty za 365 dní
                    jeden_rok = 0                               #proměnná je po 365 dnech vrácena na hodnotu nula
                    oy=oy+1                                     #počítadlo množství ročních průměrů
                    writer.writerow(datumY+[prumer_rok])        #napsání data a průměru do výstupního csv souboru
            print("Počet záznamů v csv: "+ str(iy))             #kontrolní výpis do konzole
            print("Počet 7denních průměrů: " + str(oy))         #kontrolní výpis do konzole
    return()

def Max(in_csv_max):                                            #funkce pro nalezení maximální hodnoty průtoku
    with open(in_csv_max, encoding= "utf-8") as csvinfile:      #otevření vstupního souboru, nastavení utf-8
        reader = csv.reader(csvinfile, delimiter = ",")
        max=float(0)                                            #nastavení proměnné max na float
        for row in reader:                                      #cyklus s počtem opakování rovným počtu řádků v csv souboru
            if float(row[5])>max:                               #pokud je hodnota průtoku větší než dosud nejvyšší hodnot
                max=float(row[5])                                   #tak je dosut nejvyšší hodnota nahrazena touto hodnotou průtoku
                datum_rok = row[2]                              #rok nejvyššího průtoku
                datum_mesic = row[3]                            #měsíc nejvyššího průtoku
                datum_den = row[4]                              #den nejvyššího průtoku
        print("Největší hodnota průtoku je: "+ str(max) + " a došlo k ní: " + str(datum_den) + "." + str(datum_mesic) + "." + str(datum_rok)) #vypsání do konzole
    return()

def Min(in_csv_min):                                            #funkce pro nalezení minimální hodnoty průtoku
    with open(in_csv_min, encoding= "utf-8") as csvinfile:      #otevření vstupního souboru, nastavení utf-8
        reader = csv.reader(csvinfile, delimiter = ",")
        min=float(1000)                                         #nastavení proměnné min na float
        for row in reader:                                      #cyklus s počtem opakování rovným počtu řádků v csv souboru
            if float(row[5])<min:                               #pokud je hodnota průtoku větší než dosud nejvyšší hodnot
                min=float(row[5])                                   #tak je dosut nejvyšší hodnota nahrazena touto hodnotou průtoku
                datum_rok = row[2]                              #rok nejvyššího průtoku
                datum_mesic = row[3]                            #měsíc nejvyššího průtoku
                datum_den = row[4]                              #den nejvyššího průtoku
        print("Nejmenší hodnota průtoku je: "+ str(min) + " a došlo k ní: " + str(datum_den) + "." + str(datum_mesic) + "." + str(datum_rok)) #vypsání do konzole
    return()

Kontrola("vstup.csv")
AvgW("vstup.csv")
AvgY("vstup.csv")
Max("vstup.csv")
Min("vstup.csv")
