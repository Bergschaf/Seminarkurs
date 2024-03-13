import csv

bevölkerung = {

}  # [jahr][bundesland] = anzahl
jahreszahlen = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012",
                "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]
rows = []
with open("Bevölkerung.csv", "r", newline="", encoding="cp1252") as file:
    reader = csv.reader(file, delimiter=";")
    header = next(reader)
    print(header)
    for row in reader:
        # throw out the 5th to the 12th column
        jahreszahl = row[0][-4:]
        if jahreszahl not in jahreszahlen:
            continue
        bundesland = row[1]
        anzahl = int(row[-1])
        if jahreszahl not in bevölkerung:
            bevölkerung[jahreszahl] = {}
        bevölkerung[jahreszahl][bundesland] = int(anzahl)

for jahr in bevölkerung:
    # print gesamtbevölkerung, format with 1000s separator
    print(f"{jahr}: {sum(bevölkerung[jahr].values()):_}")

