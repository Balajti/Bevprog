def calculator(unit, number):
    conversionRate = 2.54
    if unit == "cm" or unit == "inch":
        if unit == "inch":
            print(round(number * conversionRate, 2), " cm")
        if unit == "cm":
            print(round(number / conversionRate, 2), " inches")
    else:
        print("Not correct unit!")


if __name__ == "__main__":
    print("Enter a number and a unit of measure  cm/inch")
    inputNumber = float(input())
    unitOfMeasure = input()
    calculator(unitOfMeasure, inputNumber)


