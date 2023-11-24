import urllib.request
import matplotlib.pyplot as plt
POCET = 30
staty = ["Czechia", "Austria", "Slovakia", "Germany", "Poland", "Zimbabwe"]
with urllib.request.urlopen('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/weekly_cases_per_million.csv') as response:
    data = response.read().decode("utf-8").split("\n")
dny = [line.split(',') for line in data if len(line)>10]
datumy = [d[0] for d in dny[-POCET:]]
for stat in staty:
    index = dny[0].index(stat)
    plt.plot( datumy, [0 if d[index]=="" else float(d[index]) for d in dny[-POCET:]] )
plt.legend(staty)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()