print("Adj meg egy mondatot!")
mondat = input()
betuk = set()

for betu in mondat:
    betuk.add(betu)

betuk = list(dict.fromkeys(betuk))
counter = 0
numberOfWords = {}

for x in betuk:
    for i in mondat:
        if i == x:
            counter += 1
    if x.isalpha():
        numberOfWords[x] = counter
    counter=0

print("A betuk gyakorisaga: ", end=" ")
print(numberOfWords)

print("Fordítva: ", end=" ")
print(mondat[::-1])

szavak = mondat.split(' ')

print("A szavak listába rendezve:", end=" ")
print(szavak)
