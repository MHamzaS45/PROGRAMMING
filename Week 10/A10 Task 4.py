########################################################
# Task A10_T4 - Merge Sort
# Developer Hamza Sahqani
# Date 2025-12-30
########################################################
import sys

def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(PLeft) and rightIndex < len(PRight):
        if PAsc:
            if PLeft[leftIndex] <= PRight[rightIndex]:
                PMerge.append(PLeft[leftIndex])
                leftIndex += 1
            else:
                PMerge.append(PRight[rightIndex])
                rightIndex += 1
        else:
            if PLeft[leftIndex] >= PRight[rightIndex]:
                PMerge.append(PLeft[leftIndex])
                leftIndex += 1
            else:
                PMerge.append(PRight[rightIndex])
                rightIndex += 1

    # Add remaining values
    PMerge.extend(PLeft[leftIndex:])
    PMerge.extend(PRight[rightIndex:])

# Merge sort function
def mergeSort(PValues: list[int], PAsc: bool = True) -> None: # Sort PValues.
    if len(PValues) <= 1:                                      # PAsc: in ascending order by default. False will sort in descending order.
        return
     middle = len(PValues) // 2
    leftPart = PValues[:middle]
    rightPart = PValues[middle:]
    mergeSort(leftPart, PAsc)
    mergeSort(rightPart, PAsc)
    PValues.clear()
    merge(leftPart, rightPart, PValues, PAsc)
    return None

def loadData(PFilename: str, PData: list[int]) -> None:
    PData.clear()
    try:
        with open(PFilename, "r", encoding="utf-8") as file:
            for line in file:
                text = line.strip()
                if text:
                    PData.append(int(text))
    except FileNotFoundError:
        print(f"Error! File '{PFilename}' not found.")
        sys.exit(1)

def main() -> None:
    print("Program starting.")
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Insert filename: ").strip()
    numbers: list[int] = []
    loadData(filename, numbers)
    print(f"Raw '{filename}' -> {', '.join(str(n) for n in numbers)}")
    ascending = numbers.copy()
    mergeSort(ascending, True)
    print(f"Ascending '{filename}' -> {', '.join(str(n) for n in ascending)}")
    descending = numbers.copy()
    mergeSort(descending, False)
    print(f"Descending '{filename}' -> {', '.join(str(n) for n in descending)}")

    

if __name__ == "__main__":
    main()
    print("Program ending.")
