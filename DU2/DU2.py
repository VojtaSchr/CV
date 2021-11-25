import csv


with open("QD_082700_Data.csv", encoding= "utf-8") as csvinfile:
    reader = csv.reader(csvinfile, delimiter = ",")
    iw=0
    ow=0
    jeden_tyden = float(0)
    for row in reader:
        #print(row[5])
        iw=iw+1
        jeden_tyden += float(row[5])
        #if i%7==1:    
        if iw%7==0:
            prumer_tyden = round(jeden_tyden/7, 3)
            jeden_tyden = 0
            ow=ow+1
            print(prumer_tyden)
    print(iw)
    print(ow)

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
