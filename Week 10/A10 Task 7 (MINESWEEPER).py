########################################################
# Task A10_T7--Minesweeper Field 
# Developer Hamza Sahqani
# Date 2025-12-28
########################################################

import random
random.seed(1234)

def layMines(PMineField: list[list[int]], PMines: int): # Mine Command. The "PMineField" is pre-initialized 2d matrix with zeros.
    rows = len(PMineField) 
    cols = len(PMineField[0])
    positions = []
    for r in range(rows):
        for c in range(cols):
            positions.append((r, c))
    random.shuffle(positions)
    for i in range(min(PMines, rows * cols)):
        r, c = positions[i]
        PMineField[r][c] = 9
    return None

def calculateNearbys(PMineField: list[list[int]]) -> None:
    rows = len(PMineField)
    cols = len(PMineField[0])
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    for r in range(rows):
        for c in range(cols):
            if PMineField[r][c] == 9:
                continue
            count = 0
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if PMineField[nr][nc] == 9:
                        count += 1
            PMineField[r][c] = count

def generateMinefield(
        PMineField: list[list[int]],
        PRows: int,
        PCols: int,
        PMines: int) -> None:
    PMineField.clear()
    for i in range(PRows):
        PMineField.append([])
        for _ in range(PCols):
            PMineField[i].append(0)
    layMines(PMineField, PMines)
    calculateNearbys(PMineField)


def printBoard(PMineField: list[list[int]]) -> None:
    if not PMineField:
        print("No board generated.")
        return

    for row in PMineField:
        print(row)


def saveBoard(PMineField: list[list[int]], filename: str) -> None:
    with open(filename, "w") as f:
        for row in PMineField:
            line = ",".join(str(value) for value in row)
            f.write(line + "\n")


def main() -> None:
    print("Program starting.")
    minefield = []

    while True:
        print("\nOptions:")
        print("1 - Generate minesweeper board")
        print("2 - Show generated board")
        print("3 - Save generated board")
        print("0 - Exit")

        choice = input("Your choice: ")

        if choice == "1":
            try:
                rows = int(input("Insert rows: "))
                cols = int(input("Insert columns: "))
                mines = int(input("Insert mines: "))

                if rows <= 0 or cols <= 0 or mines < 0:
                    print("Invalid values.")
                    continue

                if mines > rows * cols:
                    print("Too many mines.")
                    continue

                generateMinefield(minefield, rows, cols, mines)
            except ValueError:
                print("Invalid input.")
        elif choice == "2":
            printBoard(minefield)
        elif choice == "3":
            if not minefield:
                print("No board to save.")
                continue
            filename = input("Insert filename: ")
            saveBoard(minefield, filename)
            print("Board saved.")
        elif choice == "0":
            print("\nExiting program.")
            break
        else:
            print("Invalid option.")
    print("\nProgram ending.")

if __name__ == "__main__":
    main()

