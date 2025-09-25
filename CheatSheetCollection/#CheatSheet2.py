#CheatSheet2
print ("Welcome to the app")
Temp = int(input("What is the temperature of your own CPU? "))

if Temp > 80: 
    print ("Warning! The temperature is too high!")
else : 
    print("Everything is cool! Keep going :) ")

# > greater
# < less
# >= greator or equal
# <= less than or equal
# == equal to
# != not equal to

# Make a program which, which tests if the user input is odd or even. hint: % 
print ("Hello")
UserInput = float(input("Enter a number: "))

if UserInput % 2 == 0:
    print (f"The number {UserInput} is even. ")
else: 
    print (f"The number {UserInput} is odd. ")

if Temp > 80:
    if Temp > 90:
        print("Cooked CPU lmao.")
    else:
        print("Warning! The temperature is too high. ")
else: 
    print("All good, go ahead.")
# elif 
if Temp > 90:
    print ("Cooked CPU lmao.")
elif Temp > 80:
    print ("Warning! The temperature is too high. ")
else: 
    print ("All good, go ahead.")

#Make a program which asks the user for 2 names and then tests if the length of the first name is longer, shorter or equal 
# length to the second name. Hint: len()

print ("Program Starting....")
FirstName = len(input("Hello! \n Type in your first name here: ")) 
SecondName = len(input("\n Type in your second name here: "))
if FirstName > SecondName:
    print ("The first name is longer than the second name in length")
elif FirstName == SecondName:
    print ("The first name is equal to the second name in length ")
else:
    print ("The first name is shorter than the second name in length")

# Another one
Town = "Tampere"
Street = "Kiverionkatu"
Building = 21


if (Town == "Lahti" and Street == "Mukkulankatu" and Building == 19):
    print ("You are at LAB!")
elif (Town == "Lahti" and Street != "Mukkulankatu" and Building != 19):
    print ("You are in the correct town, but check the street address.")
elif not(Town == "Lahti" and Street == "Mukkulankatu" and Building == 19):
    print ("You are completely lost.")

import random 

print(random.random())
RandomInteger = random.randomint(1,10)
print(RandomInteger)