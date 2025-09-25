#Program starting.
#What is your name: John
#Enter a floating point number: 3.1
#Enter second floating point number: 5.3
#John gave you numbers 3.1 and 5.3
#Multiplying first and second number will result in product 16.43
print("Program Starting")
Name = input("What is Your name?: ")
First_number = float(input("Enter a floating point number: "))
Second_number = float(input("Enter a second floating point number: "))
print(f"{Name} gave you numbers {First_number} and {Second_number}")
Product = First_number * Second_number
print(f"Multiplying first and second number will result in {round(Product, 2)}")
print("End Program")
#Program ending