#Prompt user to insert value as an integer.
print ("Program starting...")
print ("Testing decision structures.")
Feed = input("Insert an integer: ")
Value = int(Feed)
#Display menu
#option 1 - In one multi-branched decision
#option 2 - Independent if-statement decisions
#option 0 - Exit
print ("Options: \n 1 - In one multi-branched decision \n 2 - In multiple independent if-statements \n 0 - Exit ")
Feed = input("Your choice: ")
Choice = int(Feed)
#One multi-branched decision structure:
#Value is 400 or more => add 44 to the existing value
#Value is 200 or more => add 22 to the existing value
#Value is 100 or more => add 11 to the existing value
if Choice == 1:
    print ("You chose option 1.")
    if (Value >= 400):
        Value1 = Value + 44
        #Can also do Value+=44
        print (f"Using one multi-branched decision structure. \nResult is {Value1}.")
    elif (Value >= 200):
        Value2 = Value + 22
        print (f"Using one multi-branched decision structure. \nResult is {Value2}.")
    elif (Value >= 100):
        Value3 = Value + 11
        print (f"Using one multi-branched decision structure. \nResult is {Value3}.")
#Independent if-statement decisions one after another:
#At the end of the options 1 & 2, show the results like in the example program runs.       
#Value is 400 or more => add 44 to the existing value
#Value is 200 or more => add 22 to the existing value
#Value is 100 or more => add 11 to the existing value
#Exit: “Exiting…
elif (Choice == 2):
    print ("You chose option 2.")
if (Value >= 400):
    Value += 44
if (Value >= 200):
    Value += 22
if (Value >= 100):
    Value += 11
    print (f"Using one multiple independant if statement structure. \nResult is {Value}.") 
elif (Choice == 0):  
    print ("Exiting. ")
else:
    print ("Unknown option. ")
#End Program
print ("\nProgram ending.")

