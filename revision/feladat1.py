
def elso(lista):
    with open("revision\playlist.csv", "r") as f:
        for rows in f:
            row = rows.split(";")
            lista.append({"eloado": row[0], "cim": row[1], "mufaj": row[2], "hossz": int(row[3])})

def masodik(lista):
    seconds = 0
    for item in lista:
        seconds += item["hossz"]
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print("%d:%02d:%02d" % (hour, minutes, seconds))

def harmadik(lista):
    hosszak = []
    for item in lista:
        hosszak.append(int(item["hossz"]))
    maximum = max(hosszak)
    with open("03_leghosszabb_rock.txt", 'w', encoding="utf-8") as ki:
        for item in lista:
            if item["hossz"] == maximum:
                ki.write(item["eloado"] + item["cim"] + item["mufaj"] + str(item["hossz"]))

def negyedik(lista):
    dicts = dict()
    for item in lista:
        dicts[item["eloado"]] = dicts.get(item["eloado"], 0) +1
    inverse = [(value, key) for key, value in dicts.items()]
    print(max(inverse)[1])
    
def otodik(lista):
    d = dict()
    for item in lista:
        d[item["eloado"]] = d.get(item["eloado"], 0) + item["hossz"]
    sortedDict = dict( sorted(d.items(), key=lambda x: x[0].lower()) )
    with open("05_osszegzes.txt", "w", encoding="utf-8") as ki:
        for item, value in sortedDict.items():
            ki.write(item + "\t" + str(value) + "\n")
        
def hatodik(lista):
    with open("06_eloadonev_dalok.txt", "w") as ki:
        for item in lista:
            name = item["eloado"]
            name.lower()
            newName =""
            for c in name:
                if c.isalpha():
                    newName = f"{newName}{c}"
                    


            ki.write( ) 



if __name__ == "__main__":
    lista = []
    elso(lista)
    masodik(lista)
    harmadik(lista)    
    negyedik(lista)
    otodik(lista)
    hatodik(lista)

