#A5 Task 6
#This menu-driven program must contain a maintainable program structure with the following requirements:
#main function which represents the main program logic including menu cycle.
#showOptions function which takes no arguments, shows the available options in the standard output and returns None.
#askChoice function which takes no arguments, prompts user to insert choice and returns an integer regardless of the user feed.
def showOptions() -> None:
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None
    
def askChoice() -> int:
    choice = input("Your choice: ")
    if choice.isnumeric():
        return int(choice)
    else:
        return None 
 
def main() -> None:
    print ("Program starting.")
    count = 0
    while True:
        showOptions()
        choice = askChoice()
        if choice == 1:
            print(f"Current count - {count}\n")
        elif choice == 2:
            print("Count increased!\n")
            count += 1
        elif choice == 3:
            print("Cleared count!\n")
            count = 0
        elif choice == 0:
            print("Exiting program.\n")
            print("Program ending.")
            break
        else:
            print("Unknown option!\n")
    return None

    
main()