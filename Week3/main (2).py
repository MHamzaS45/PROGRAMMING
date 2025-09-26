#A3 Task 6
print("Program starting...")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below. \nOptions:\n1 - Length\n2 - Weight\n0 - Exit")
Choice = int(input("Your choice: "))

if Choice == 1:
    print("Length options: \n1 - Meters to kilometers\n2 - Kilometers to meters\n0 - Exit")
    Choice2 = int(input("Your choice: "))
    if Choice2 == 1:
        MetersInput = float(input("Insert meters: "))
        MeterstoKm = MetersInput / 1000
        KmOutput = round(MeterstoKm, 1)
        print(f"{MetersInput} m is {KmOutput} km")
    elif Choice2 == 2:
        KmInput = float(input("Insert kilometers: "))
        KmtoMeters = KmInput * 1000
        MetersOutput = round(KmtoMeters, 1)
        print(f"{KmInput} km is {MetersOutput} m")
    elif Choice2 == 0:
        print("Exiting...")
    else:
        print("Unknown option.")
elif Choice == 2:
    print("Weight options: \n1 - Grams to pounds\n2 - Pounds to grams\n0 - Exit")
    Choice2 = int(input("Your choice: "))
    if Choice2 == 1:
        GramsInput = float(input("Insert grams: "))
        PoundsOutput = round(GramsInput * 0.002205, 1)
        print(f"{GramsInput} g is {PoundsOutput} lb")
    elif Choice2 == 2:
        PoundsInput = float(input("Insert pounds: "))
        GOutput = round(PoundsInput * 453.6, 1)
        print(f"{PoundsInput} lb is {GOutput} g")
    elif Choice2 == 0:
        print("Exiting...")
    else:
        print("Unknown option.")
elif Choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")
