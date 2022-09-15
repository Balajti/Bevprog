print("Adj meg egy mondatot!")
mondat = input()
betuk = set()

for betu in mondat:
    betuk.add(betu)

counter = 0
numberOfWords = dict()

for betu in betuk:
    for i in mondat:
        if i == betu:
            counter += 1
    if betu.isalpha():
        numberOfWords[betu] = counter
    counter=0

print("A betuk gyakorisaga: ", end=" ")
for elem in numberOfWords:
    print(numberOfWords)

print("Fordítva: ", end=" ")
print(mondat[::-1])

szavak = mondat.split(' ')

print("A szavak listába rendezve:", end=" ")
print(szavak)
