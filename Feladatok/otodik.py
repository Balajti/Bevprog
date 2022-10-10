from random import random

szamok = []
r = int(random()*20)
for i in range(r):
    szamok.append(int(random()*10))
legnagyobb = max(szamok)
print(szamok)

counter = 0
for szam in szamok:
    if legnagyobb == szam:
        counter += 1

print(counter)