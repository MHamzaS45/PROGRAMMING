#A9 Task 2.py
# Exit Codes

import sys


def getExitCodeMessage() -> int:
    global Feed
    while True:
        Feed = input("Insert exit code (0-255): ")
        try:
            Feed = int(Feed)
            if 0 >= Feed and Feed <= 255:
                return print("Clean exit")
            elif Feed >= 1 and Feed <= 254:
                return print("Error code")
            else:
                return print("Unknown value")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        
def main() -> None:
    print("Program starting.")
    getExitCodeMessage()
    sys.exit(Feed)
    
if __name__ == "__main__":
    main()
    
