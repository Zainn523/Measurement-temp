import  random

print("[1] Temperature\n[2] Measurements")
choice_1 = float(input("What would you like to convert: "))
if choice_1 == 1:
    print("[1] Celcius\n[2] Farenheit")
    choice_2= float(input("What would you like to convert from?: "))
    if choice_2 == 1:
        choice3 = float(input("Celcius Degrees To Farenheit: "))
        print(choice3*1.8 +32)
    elif choice_2 == 2:
        choice4 = float(input("Farenheit to Celcius Degrees: "))
        print((choice4 - 32) /1.8)

if choice_1 == 2:
    print("[1] Inches\n[2] Centimetres")
    choice_5 = float(input("What would you like to convert from?: "))
    if choice_5 == 1:
        choice_6 = float(input("Inches To Cm: "))
        print(choice_6 * 2.54)
    elif choice_5 == 2:
        choice_7 = float(input("Cm To Inch: "))
        print(choice_7 / 2.54)













