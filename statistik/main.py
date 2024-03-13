
# TODO nach geschlechtern aufteilen

import csv

bevölkerung = {

}  # [jahr][bundesland] = anzahl
jahreszahlen = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012",
                "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]
rows = []
with open("Bevölkerung.csv", "r", newline="", encoding="cp1252") as file: # quelle 12411-0011:
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
###############################################################################################
class DataPoint:
    def __init__(self, bundesland, jahr, anzahl):
        self.bundesland = bundesland
        self.jahr = jahr
        self.anzahl = anzahl
        self.per_10000_inhabitants = anzahl / bevölkerung[jahr][bundesland] * 100000

    def __repr__(self):
        return f"{self.bundesland} {self.jahr}: {self.anzahl} ({self.per_10000_inhabitants:.2f} pro 100.000 Einwohner)"

import csv

rows = []
with open("Alkohol_statistik.csv", "r", newline="",encoding="cp1252") as file:
    reader = csv.reader(file, delimiter=";")
    header = next(reader)
    print(header)
    for row in reader:
        # throw out the 5th to the 12th column
        rows.append(row[:4] + row[12:])
        print(rows[-1])

datapoints = []
for row in rows:
    jahreszahl = row[0]
    if jahreszahl not in jahreszahlen:
        continue
    bundesland = row[1]
    diagnose = row[2]
    if diagnose != "ICD10-F10":
        continue

    anzahl = sum([int(x) for x in row[4:-1]])
    datapoint = DataPoint(bundesland, jahreszahl, anzahl)

    datapoints.append(datapoint)
    if bundesland == "Baden-Württemberg":
        print(datapoint)

def plot_bw_over_years():
    data = {}
    for dp in datapoints:
        if dp.bundesland == "Baden-Württemberg":
            data[dp.jahr] = dp.per_10000_inhabitants

    import matplotlib.pyplot as plt
    # create a plot with every fith year at the x-axis and the y-axis from 0 to 50
    plt.plot(data.keys(), data.values(),"ro-")
    plt.xticks(list(data.keys())[::5])
    plt.yticks(range(0, 51, 5))
    # make the line blue color with dots
    plt.xlabel("Jahr")
    plt.ylabel("Krankenhausaufenthalte pro 100.000 Einwohner")
    plt.title("Krankenhausaufenthalte wegen Alkohol in Baden-Württemberg")
    # make the image high resolution
    plt.savefig("Alkohol_BW.png", dpi=300)




plot_bw_over_years()