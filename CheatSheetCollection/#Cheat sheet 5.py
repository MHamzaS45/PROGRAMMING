#Cheat sheet 5
# Functions in programming
# What is a function
# Example function in python

print("")
print("")
#if statement
#For/while loop
#function

print("Hello")
# Print is an example of a function
# Hello in this case is an example of a parameter

len("Hello")
#Another example of a function

def greet(name):
    return f"Hello, {name}"

message = greet("student") #Now it will Call the function and store the result  in name variable
print(message)

message = greet("Heikki") #repeats function with different parameter
print(message)

def greeting (): # defines the function
    print("How do you do") # function content

greeting() # Calls the function that was defined, function call
greeting() 
greeting()

def greeting_airport(person, age): # defines the function with two parameters
    print(f"Person: {person}, age: {age} years old") # function content    
    print(f"How do you do {person}")
    if age >= 18:
        print("Welcome to your flight")
    else:
        print(f"You need to wait for {18 - age} years to fly alone")

greeting_airport("Heikki", 21) # Calls the function that was defined, function call
# Now when printing the defined function, it will see 21, and print "Welcome to your flight"


# Create a program which asks the user for a number. Then check with a function if the number is a prime number.
# Also ask the user if they want to test another number as many times as they want.
# Tip: use function, conditionals and loops....

print ("Program starting.\n")
print ("This program checks if a number is prime or not.\n")
Prime = int(input("Insert a positive integer: "))
if Prime > 1:
    for i in range (2, Prime):
        if (Prime % i) == 0:
            print(f"{Prime} is not a prime number.")
            return False
else:
    Function = Prime % 2
    if Function == 0:
         print(f"{Prime} is not a prime number.")
         return False 
         elif (Function == 1) or (Function == {Prime}):
         print(f"{Prime} is a prime number.")
         return True
        
print ("\nProgram ending.")