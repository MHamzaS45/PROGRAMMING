########################################################
# Task A10_T3
# Developer Hamza Sahqani
# Date 2025-12-30
########################################################
  # Sort PValues by implementing bubble sort algorithm.
  # Handle PValues list like it is a pointer to memory
  # Sort the list inplace e.g., PValues[CurrentIndex] = PValues[NextIndex]
  # Don't overwrite PValues identifier.
  # Tester expects that the PValues list is modified.
  # It doesn't catch a return value.

import sys
def bubbleSort(PValues: list[int], PAsc: bool = True) -> None: 
    size = len(PValues)
    for pass_index in range(size - 1):
        for current in range(size - pass_index - 1):               # Remaining = Items(n) − Iteration − 1
            if PAsc:
                if PValues[current] > PValues[current + 1]:
                    PValues[current], PValues[current + 1] = (
                        PValues[current + 1],
                        PValues[current],
                    )
            else:
                if PValues[current] < PValues[current + 1]:
                    PValues[current], PValues[current + 1] = (
                        PValues[current + 1],
                        PValues[current],
                    )
     return None

def loadNumbers(PFilename: str, PContainer: list[int]) -> None: # Reads integers from a file into the given list.
    PContainer.clear()
    try:
        with open(PFilename, "r", encoding="utf-8") as file:
            for line in file:
                text = line.strip()
                if text:
                    PContainer.append(int(text))
    except FileNotFoundError:
        print(f"Error! File '{PFilename}' not found.")
        sys.exit(1)

def main() -> None:
    print("Program starting.")
    if len(sys.argv) == 2:     #Decide source
        filename = sys.argv[1]
    else:
        filename = input("Insert filename: ").strip()
    numbers: list[int] = []
    loadNumbers(filename, numbers)
    print(f"Raw '{filename}' -> {', '.join(str(n) for n in numbers)}")
    ascNumbers = numbers.copy()
    bubbleSort(ascNumbers, True)
    print(f"Ascending '{filename}' -> {', '.join(str(n) for n in ascNumbers)}")
    descNumbers = numbers.copy()
    bubbleSort(descNumbers, False)
    print(f"Descending '{filename}' -> {', '.join(str(n) for n in descNumbers)}")
    return None


if __name__ == "__main__":
    main()
    print("Program ending.")

