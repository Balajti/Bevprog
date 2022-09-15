print("Adj meg egy szamot es egy mertekegyseget  cm/inch")
szam = float(input())
mertekegyseg = input()
valtoszam = 2.54


if mertekegyseg == "cm" or mertekegyseg == "inch":
    if mertekegyseg == "inch":
        print(round(szam * valtoszam, 2), " cm")
    if mertekegyseg == "cm":
        print(round(szam / valtoszam, 2), " inches")
else:
    print("Not correct unit!")