import csv

with open("QD_082700_Data.csv", encoding= "utf-8") as csvinfile:
    reader = csv.reader(csvinfile, delimiter = ",")
    for row in reader:
        print(row[1])
