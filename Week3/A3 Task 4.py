#3_T4 More menu options
#Extend the previous menu program by adding three more options to the menu.
#Options:
#Print the name backwards
#Your name backwards is "{NameBackwards}"
#Print the first character
#The first character in name "{Name}" is "{FirstChar}"
#Show the amount of characters in the name
#There are {NameLength} characters in the name "{Name}"

print ("Program starting...")
print ("This is a program with simple menu, where you can choose which operation the program performs.")
Name = input("Before the menu, please insert your name: ")
print ("Options: \n1 - Print welcome message \n 2 - Print the name backwards \n 3 - Print the first character \n 4 - Show the amount of characters in the name \n 0 - Exit ") 
Choice = int(input("Your choice: "))
if Choice == 1:
    print (f"Welcome {Name}!")
elif Choice == 2:
    BackwardsName = Name[::-1]
    print (f"Your name backwards is \"{BackwardsName}\" ")
elif Choice == 3:
    FirstCharacter = Name[0]
    print (f"The first character in your \"{Name}\" is \"{FirstCharacter}\" ")
elif Choice == 4:
    AmountCharacters = len(Name)
    print (f"There are {AmountCharacters} characters in the name \"{Name}\" ")
elif Choice == 0:
    print ("Exiting...")
else:
    print ("Unknown option.")   

print ("\nProgram ending.")

