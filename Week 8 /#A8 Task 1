#A8 Task 1 
import time

def displayMenu() -> int:
    print("Options:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")
    try:
      Feed = int(input("Your choice: "))
    except ValueError:
        print("Unknown option!")
        return
    return Feed

def main() -> None:
    PauseDuration = []
    print("Program starting.")
    choice = -1
    while True:
        choice = displayMenu()
        if choice == 1:
            try: 
                PauseDuration = float(input("Insert pause duration (s): \n"))
            except ValueError:
                print("Invalid Output. Please enter a number\n")
        elif choice == 2:
                if PauseDuration == []:
                   print("Pause is not set.")
                   print("Set pause first.\n")
                else:
                    print(f"Pausing for {PauseDuration} seconds.")
                    time.sleep(PauseDuration)
                    print("Unpaused.\n")
        elif choice == 0:
            print("Exiting program.\n")
            break
    print("Program ending.")
    return None




if __name__ == "__main__":
    main()  
