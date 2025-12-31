########################################################
# Task A10_T2
# Developer Hamza Sahqani
# Date 2025-12-29
########################################################

import sys
def readValues(PFilename: str, PValues: list[int]) -> None:
    try:
        with open(PFilename, "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                PValues.append(int(line))
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    except ValueError:
        print("Error: Invalid data in file.")
        sys.exit(1)

def sumOfValues(PValues: list[int]) -> int:
    total = 0
    for value in PValues:
        total += value
    return total

def productOfValues(PValues: list[int]) -> int:
    product = 1
    for value in PValues:
        product *= value
    return product

def main() -> None:
    # 1. Initialize
    Values: list[int] = []
    # 2. Operate
    print("Program starting.")
    filename = input("Insert filename: ")
    readValues(filename, Values)
    total_sum = sumOfValues(Values)
    total_product = productOfValues(Values)
    # 3. Display
    print("# --- Sum of numbers --- #")
    print(total_sum)
    print("# --- Sum of numbers --- #")
    print("# --- Product of numbers --- #")
    print(total_product)
    print("# --- Product of numbers --- #")
    # 4. Cleanup
    Values.clear()


if __name__ == "__main__":
    main()
    print("\nProgram ending.")

