########################################################
# Task A9_T3
# Developer Hamza Sahqani
# Date 2025-12-25
########################################################
import sys

def requestFilename() -> str: #checks  to see if text file exists
    while True:
        Feed = input("Insert filename: ").strip()
        try:
            with open(Feed, "r", encoding="utf-8") as file:
                return Feed
        except FileNotFoundError:
            print(f"Couldn't read file '{Feed}'. ")

def printFileContents(filename: str) -> None: 
    print(f"## {filename} ##")
    with open(filename, "r", encoding="utf-8") as file:
        for row in file:
            print(row.strip()) #Should print "File exists" in the case of A3 T3 D1.txt
    print(f"## {filename} ##")

def main() -> None:
    print("Program starting.")
    filename = requestFilename()
    printFileContents(filename)
    print("Program ending.")


if __name__ == "__main__":
    main()
