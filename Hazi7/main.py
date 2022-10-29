sor = 12  
oszlop = 12 
for i in range(1, sor + 1):
    for j in range(1, oszlop + 1):
        c = i * j
        print("{:2d} ".format(c),end='')
    print(f"\n")