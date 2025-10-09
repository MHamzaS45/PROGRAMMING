#A4 TASK 3 #class ver.
print ("Program starting.")
Feed = input("\nInsert starting value: ")
StartingValue = int(Feed)
Feed = input("Insert stopping value: ")
StoppingValue = int(Feed) + 1
print ("")
print ("Starting while-loop:")
current = StartingValue
while current != StoppingValue:
    if (current == (StoppingValue)):
        print (current)
    else:
        print (current, end=' ')
    current += 1
print ("")
print ("\n\nProgram ending.")
