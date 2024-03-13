
# TODO nach geschlechtern aufteilen

# quelle https://www.demografie-portal.de/DE/Fakten/bevoelkerung-laender.html
Bevölkerung = {
    "Nordrhein-Westfalen": 18140000,
    "Bayern": 13370000,
    "Baden-Württemberg": 11280000,
    "Niedersachsen": 8140000,
    "Hessen": 6390000,
    "Rheinland-Pfalz": 4160000,
    "Sachsen": 4090000,
    "Berlin": 3760000,
    "Schleswig-Holstein": 2950000,
    "Brandenburg": 2570000,
    "Sachsen-Anhalt": 2190000,
    "Thüringen": 2130000,
    "Hamburg": 1890000,
    "Mecklenburg-Vorpommern": 1630000,
    "Saarland": 990000,
    "Bremen": 680000
}

class DataPoint:
    def __init__(self, bundesland, jahr, anzahl):
        self.bundesland = bundesland
        self.jahr = jahr
        self.anzahl = anzahl
        self.per_10000_inhabitants = anzahl / Bevölkerung[bundesland] * 100000

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

jahreszahlen = ["2019","2020", "2021", "2022"]
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