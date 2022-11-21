print(f"  \t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12")
print(" :",end='')
for l in range(1, 25):
    print("----",end='')
print("\n")
for i in range(1, 13):
    #sor
    print(f"{i}:\t",end='')
    for j in range(1, 13):
        #oszlop
        c = i * j
        print(f"{c}\t",end='')
    print(f"\n")
