#A3 Task 3.py
def menuDisplay():
    Feed = input("Before the menu, please insert your name: ")
    if Feed.isnumeric():
        print("Invalid name, please try again.")
    else:
      print("")
      print("Options:")
      print("1 ---- Print welcome message")
      print("0 ---- Exit")
    return Feed 

def userChoice():
    Name = menuDisplay()
    Choice = int(input("Your choice: "))
    if Choice == 1:
        print(f"Welcome {Name}!")
    elif Choice == 0:
        print("Exiting...")
    else:
        print("Unknown option")
    return None



def main():
    print("Program starting.")
    print("This is a program with simple menu, where you can choose which operation the program performs.")
    userChoice()
    return None   

if __name__ == "__main__":
    main()
    print ("Program ending.")
