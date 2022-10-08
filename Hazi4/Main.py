def division(a, b):
    try:
        d = a / b
    except ZeroDivisionError:
        print("Division by 0 is not allowed")
    else:
        print(d)
    finally:
        print("Out of try except block")

if __name__ == "__main__":
    c = 0
    while c == 0:
        inputA = float(input("Enter 'a' value"))
        inputB = float(input("Enter 'b' value"))
        division(inputA, inputB)