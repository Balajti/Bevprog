def isValid(a, b, c):
    if a + b >= c and a + c >= b and c + b >= a:
        print(f"The {a},{b} and {c} sided triangle is valid")
    else:
        print(f"The {a},{b} and {c} sided triangle is NOT valid")


if __name__ == "__main__":
    print("Enter the triangle's sides in cm")
    inputA = int(input("a side: "))
    inputB = int(input("b side: "))
    inputC = int(input("c side: "))
    isValid(inputA, inputB, inputC)