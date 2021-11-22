import csv
from os import write
a=0
b=0
with open("Parkoviste.csv", encoding= "utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    write = csv.writer(csvoutfile)
    for row in reader:
        #print(len(row))
        #print(row[0])
        print("Jmeno: " +row[1]+ " ...Kapacita: " +row[5])
        try:
            a += int(row[5])
        except ValueError:
            pass
        if row[4]=="True":
            try:
                b += int(row[5])
            except ValueError:
                pass
            
    print(a)
    print(b)
    