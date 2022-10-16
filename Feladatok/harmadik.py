num = int(input())

n1, n2 = 0, 1
szamlalo = 0

while szamlalo < num:
    print(n1)
    kovetkezo = n1 + n2
    n1 = n2
    n2 = kovetkezo
    szamlalo += 1