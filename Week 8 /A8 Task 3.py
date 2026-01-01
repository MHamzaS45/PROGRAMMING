#A8 Task 3.py
# Menu Driven No. files

import sys


def readValues(PFilename: str, PValues: list[float]) -> None: # Values can be stored into a list[float] data structure
    """Read floating-point values from file into list."""
    PValues.clear()
    try:
        with open(PFilename, "r", encoding="utf-8") as file:
            for line in file:
                row = line.strip()
                if row != "":
                    PValues.append(float(row))
    except FileNotFoundError:
        print(f"Error! File '{PFilename}' not found.")

def calculateSum(PValues: list[float]) -> float:
    return round(sum(PValues), 1)

def calculateAverage(PValues: list[float]) -> float:
    if len(PValues) == 0:
        return 0.0
    return round(sum(PValues) / len(PValues), 1)

def displayMenu() -> None:
    print("Options:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")


def main() -> None:               #Provide output for displayed menu as well.
    print("Program starting.")
    values: list[float] = []           # Values can be stored into a list[float] data structure
    while True:
        displayMenu()
        choice = input("Your choice: ").strip()
        if choice == "1":
            filename = input("Insert filename: ")
            readValues(filename, values)
        elif choice == "2":
            print(f"Amount of values {len(values)}")
        elif choice == "3":
            result = calculateSum(values)
            print(f"Sum of values {result}")
        elif choice == "4":
            result = calculateAverage(values)
            print(f"Average of values {result}")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")
    values.clear()
    print("Program ending.")


if __name__ == "__main__":
    main()

