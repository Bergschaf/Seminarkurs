
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

bevölkerung_gesamt = { jahr: sum(bevölkerung[jahr].values()) for jahr in bevölkerung }
###############################################################################################
class DataPoint:
    def __init__(self, bundesland, jahr, anzahl):
        self.bundesland = bundesland
        self.jahr = jahr
        self.anzahl = anzahl
        self.per_10000_inhabitants = anzahl  / bevölkerung[jahr][bundesland] * 100000

    def __repr__(self):
        return f"{self.bundesland} {self.jahr}: {self.anzahl} ({self.per_10000_inhabitants:.2f} pro 100.000 Einwohner)"

import csv

rows = []
with open("Alkohol_statistik_alle_Altersgruppen.csv", "r", newline="",encoding="cp1252") as file:
    reader = csv.reader(file, delimiter=";")
    header = next(reader)
    print(header)
    for row in reader:
        # throw out the 5th to the 12th column
        #rows.append(row[:4] + row[12:])
        rows.append(row)
        print(rows[-1])

datapoints = []
for row in rows:
    jahreszahl = row[0]
    if jahreszahl not in jahreszahlen:
        continue
    bundesland = row[1]
    #diagnose = row[2]
    #if diagnose != "ICD10-F10":
    #    continue

    #anzahl = sum([int(x) for x in row[4:-1]])
    anzahl = int(row[2])
    datapoint = DataPoint(bundesland, jahreszahl, anzahl)

    datapoints.append(datapoint)
    if bundesland == "Baden-Württemberg":
        pass
        #print(datapoint)

years = ["2022", "2021", "2020", "2019", "2018", "2017"]
for year in years:
    i = 0
    for dp in datapoints:
        if dp.jahr == year:
            i += dp.anzahl
            print(dp)
    print(year, i)


def bar_chart_avg_bundesländer_avg_more():
    """
    Durchschnitt über die letzten 15
    :return:
    """
    data = {}
    used_years = ["2022", "2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008"]
    for dp in datapoints:
        if dp.bundesland not in data:
            data[dp.bundesland] = []
        if dp.jahr not in used_years:
            continue
        data[dp.bundesland].append(dp.per_10000_inhabitants)

    for bundesland in data:
        data[bundesland] = sum(data[bundesland]) / len(data[bundesland])

    #insgesamt
    i = 0
    for bundesland in data:
        i += data[bundesland]
    print(i)

    # sort by value
    data = dict(sorted(data.items(), key=lambda item: item[1]))
    import matplotlib.pyplot as plt
    # make the bars horizontal
    # make the grid appear in the background
    plt.grid(axis="x")
    # use .set_axisbelow(True) to make the grid appear in the background
    plt.gca().set_axisbelow(True)

    plt.barh(list(data.keys()), data.values())
    plt.xlabel("Krankenhausaufenthalte pro 100.000 Einwohner\n"
               "Durchschnitt der letzten 15 Jahre")
    plt.title("Alkoholbedingte Krankenhausaufenthalte")
    # make the labels readable
    plt.tight_layout()
    # add average line
    avg = sum(data.values()) / len(data)
    plt.axvline(avg, color="r", linestyle="--")
    plt.text(avg, 0, f"Ø: {avg:.2f}", color="r", verticalalignment="center")

    # add grid
    #plt.show()
    # make the image high resolution
    plt.savefig("Alkohol_Bundesländer_avg_15_Jahre.png", dpi=500)

#plot_bw_over_years()
#plot_ges_and_bw_over_years()
#bar_chart_avg_bundesländer()
bar_chart_avg_bundesländer_avg_more()
