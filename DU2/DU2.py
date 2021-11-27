import csv
from os import execlp, write

def AvgW():
    with open(soubo, encoding= "utf-8") as csvinfile:
        reader = csv.reader(csvinfile, delimiter = ",")
        iw=0
        ow=0
        jeden_tyden = float(0)
        with open("AvgW.csv",'w', encoding= "utf-8") as AvgW_Vystup:
            csv.register_dialect("dialect1", delimiter="/")
            writer = csv.writer(AvgW_Vystup, dialect="dialect1")
            for row in reader:
                #print(row[5])
                iw=iw+1
                jeden_tyden += float(row[5])
                if iw%7==1:
                    datum = (row[2] + row[3] + row [4])
                    writer.writerow(datum)   
                if iw%7==0:
                    prumer_tyden = round(jeden_tyden/7, 3)
                    jeden_tyden = 0
                    ow=ow+1
                    print(prumer_tyden)
                    #writer.writerow(str(datum))
                    writer.writerow(str(prumer_tyden))
            print(iw)
            print(ow)
    return()

def AvgY():
    with open("QD_082700_Data.csv", encoding= "utf-8") as csvinfile:
        reader = csv.reader(csvinfile, delimiter = ",")
        iy=0
        oy=0
        jeden_rok = float(0)
        for row in reader:
            #print(row[5])
            iy=iy+1
            jeden_rok += float(row[5])
            #if i%7==1:    
            if iy%365==0:
                prumer_rok = round(jeden_rok/365, 3)
                jeden_rok = 0
                oy=oy+1
                print(prumer_rok)
        print(iy)
        print(oy)
    return()

def kontrola():
    try:
        with open("test_soubor.csv", encoding= "utf-8") as csvinfile:
            reader = csv.reader(csvinfile, delimiter = ",")
            it=0
            for row in reader:
                it=it+1
                try:
                    test1=float(row[5])
                except ValueError:
                    print("Údaje o průtoku v csv souboru jsou poškozená (řádek "+str(it)+")")
    except PermissionError:
        print("Program nemá oprávnění číst vstupní soubor")
    except FileNotFoundError:
        print("Program nemůže najít vstupní soubor, zkontrolujte, že jste zadali jeho jméno (případně cestu k němu) správně")

    return()

AvgW()
#AvgY()
