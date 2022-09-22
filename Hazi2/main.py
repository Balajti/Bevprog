def calculator(unit, number):
    conversionRate = 2.54
    if unit == "cm" or unit == "inch":
        if unit == "inch":
            print(round(number * conversionRate, 2), " cm")
        if unit == "cm":
            print(round(number / conversionRate, 2), " inches")


if __name__ == "__main__":
    isItStarted = 0
    while isItStarted == 0:
        print("Enter a number and a unit of measure  cm/inch")
        try:
            inputNumber = float(input())
            unitOfMeasure = input()
        except ValueError:
            print("You didn't enter a number")
            print("Please try again!!")
        except Exception as e:
            print(e)
            print("Please try again!!")
        else:
            if unitOfMeasure.isalpha() and unitOfMeasure == "cm" or unitOfMeasure == "inch":
                calculator(unitOfMeasure, inputNumber)
                isItStarted = 1
            else:
                print("You entered the unit of measure incorrectly")
                print("Please try again!!")


