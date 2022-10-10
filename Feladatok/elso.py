number = int(input("Adj meg egy szamot"))

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "nem prím")
            break
    else:
        print(number, " prím")
else:
    print(number, "nem prím")