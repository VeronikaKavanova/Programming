soubor = open("kocky.txt", "a")
soubor.write("\nTlapička je moje druhá kočka.")
soubor.close()


#file = open("data.txt", "r", encoding ="utf-8")

with open("data.txt", "r", encoding ="utf-8") as file:
    for l in file:
        seznam = l.split(",")
#file.close()

for s in seznam:
    print(s + "\n")

file = open("data.txt", "a", encoding ="utf-8")
file.write("\nKarel Obrle,28,Praha,Burgr,8469.4,8644564.1")
file.close()
print(seznam[5])

import json

def write_json(new_data, filename = "records.json"):
    with open(filename, "r+") as file:
        file_data = json.load(file)
        file_data["users"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

y = {"name": "Antoan Finkleoyar",
     "nmbr": 7,
     "IQ": 156,
     "Záliba": "běh",
}