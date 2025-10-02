# Create a Python program which prompts user to insert two integers. Use these integers together with the “for-loop” structure to create behaviour like in the example program example run below.
print ("Program starting.")
Feed = (input("Insert starting value: "))
StartingValue = int(Feed)
Feed = (input("Insert stopping value: "))
StoppingValue = int(Feed)

print ("\nStarting for loop: ")
for i in range (StartingValue, StoppingValue + 1):
    print (i)

print ("\nProgram ending.")
