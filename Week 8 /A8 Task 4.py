#A8 Task 4.py

#Recommended things to implement into the library file:
#MONTHS: list[str] containing month names
#WEEKDAYS: list[str] containing weekday names
#def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
#def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
#def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
#def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:

import sys
from datetime import datetime                            #For handling the timestamps 
MONTHS = ( 
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
)

WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
    PTimestamps.clear()
    try:
        with open(PFilename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    ts = datetime.strptime(line, "%Y-%m-%dT%H:%M")
                    PTimestamps.append(ts)
    except FileNotFoundError:                                         #If the file is not found, print an error and exit
        print(f"File '{PFilename}' not found.")
        sys.exit(1)

def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
    count = 0
    for ts in PTimestamps:
        if ts.year == PYear:
            count += 1
    return count

def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
    monthIndex = MONTHS.index(PMonth) + 1
    count = 0
    for ts in PTimestamps:
        if ts.month == monthIndex:
            count += 1
    return count

def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
    count = 0
    for ts in PTimestamps:
        if WEEKDAYS[ts.weekday()] == PWeekday:
            count += 1
    return count

def displayMenu() -> None: 
    print("Options:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")

def main() -> None:
    print("Program starting.")
    timestamps: list[datetime] = []
    filename = input("Insert filename: ").strip()
    readTimestamps(filename, timestamps)
    while True:
        displayMenu()
        choice = input("Your choice: ").strip()
        if choice == "0":
            print("Exiting program.")
            break
        elif choice == "1":
            year = int(input("Insert year: "))
            result = calculateYears(year, timestamps)
            print(f"Amount of timestamps during year '{year}' is {result}")
        elif choice == "2":
            month = input("Insert month: ").strip().title()
            if month not in MONTHS:
                print("Invalid month.")
                continue
            result = calculateMonths(month, timestamps)
            print(f"Amount of timestamps during month '{month}' is {result}")
        elif choice == "3":
            weekday = input("Insert weekday: ").strip().title()
            if weekday not in WEEKDAYS:
                print("Invalid weekday.")
                continue
            result = calculateWeekdays(weekday, timestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {result}")
        else:
            print("Invalid choice.")
    return None

if __name__ == "__main__":
    main()
    print("Program ending.")

