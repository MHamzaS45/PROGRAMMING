########################################################
# Task A10_T6 
# Developer Hamza Sahqani
# Date 2025-12-30
########################################################
import sys
import copy
import time
from typing import Callable, List

def loadNumbers(filename: str, numbers: List[int]) -> None: # Load integers onto number list
    numbers.clear()
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if stripped:
                    numbers.append(int(stripped))
    except FileNotFoundError:
        print(f"Error! File '{filename}' not found.")
        sys.exit(1)


def bubble_sort(arr: List[int]) -> List[int]: # Algorithm 
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr: List[int]) -> List[int]: # Algorithm
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def time_sorting(algorithm: Callable, dataset: List[int]) -> int: #Algorithm
    start = time.perf_counter_ns()
    algorithm(dataset)
    end = time.perf_counter_ns()
    return end - start


def menuDisplay() -> None: # Display menu
    print("Options:")
    print("1 - Load dataset")
    print("2 - Measure sorting times")
    print("3 - Save measurement results")
    print("0 - Exit")


def main() -> None: # Central function hub
    dataset: List[int] = []
    measurements: List[str] = []
    current_file: str = ""

    print("Program starting.\n")

    while True:
        menuDisplay()
        choice = input("Your choice: ").strip()

        if choice == "0":
            print("Exiting program.")
            break
        elif choice == "1":
            current_file = input("Enter dataset filename: ").strip()
            load_numbers(current_file, dataset)
        elif choice == "2":
            if not dataset:
                print("No dataset loaded. Please load a dataset first.")
                continue
            print(f"Measuring sorting times for dataset '{current_file}':")

            built_in_ns = time_sorting(sorted, copy.deepcopy(dataset))
            bubble_ns = time_sorting(bubble_sort, copy.deepcopy(dataset))
            quick_ns = time_sorting(quick_sort, copy.deepcopy(dataset))
            print(f" - Built-in sorted: {built_in_ns} ns")
            print(f" - Bubble sort: {bubble_ns} ns")
            print(f" - Quick sort: {quick_ns} ns")
            measurements.clear()
            measurements.append(f"Sorting times for dataset '{current_file}':")
            measurements.append(f" - Built-in sorted: {built_in_ns} ns")
            measurements.append(f" - Bubble sort: {bubble_ns} ns")
            measurements.append(f" - Quick sort: {quick_ns} ns")
        elif choice == "3":
            if not measurements:
                print("No results to save. Measure sorting times first.")
                continue
              
            output_file = input("Enter filename to save results: ").strip()
            try:
                with open(output_file, "w", encoding="utf-8") as f:
                    for line in measurements:
                        f.write(line + "\n")
                print(f"Results successfully saved to '{output_file}'.")
            except Exception as e:
                print(f"Error saving results: {e}")
        else:
            print("Invalid option. Try again.")
    dataset.clear()
    measurements.clear()      



if __name__ == "__main__":
    main()
   print("Program ending.")

