#Create a temperature unit conversion program
print ("Program starting.")
print ("Options: \n1 - Celsius to Fahrenheit \n2 - Fahrenheit to Celsius \n0 - Exit")

Choice =  (input("Your choice: "))
if Choice == "1":
    Celsius = float(input("Insert the amount of Celsius: "))
    Convert = (1.8 * Celsius) + 32
    Fahrenheit = round(Convert, 1)
    print (f"{Celsius} °C equals to {Fahrenheit} °F")
elif Choice == "2":
    Fahrenheit2 = float(input("Insert the amount of Fahrenheit: "))
    Convert2 = (Fahrenheit2 - 32) / 1.8
    Celsius2 = round(Convert2, 1)
    print (f"{Fahrenheit2} °F equals to {Celsius2} °C ")
elif Choice == "0":
    print ("Exiting...")
else:
    print ("Unknown option.")

print ("Program ending.")
    

