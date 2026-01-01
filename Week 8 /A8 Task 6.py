#A8 Task 6.py

import svgwrite
from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle

def drawSquare(PDwg: Drawing) -> None:
    print("Insert square")
    x = float(input("- Left edge position: "))
    y = float(input("- Top edge position: "))
    side = float(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")

    PDwg.add(
        Rect(
            insert=(x, y),
            size=(side, side),
            fill=fill,
            stroke=stroke
        )
    )

def drawCircle(PDwg: Drawing) -> None:
    print("Insert circle")
    cx = float(input("- Center x position: "))
    cy = float(input("- Center y position: "))
    radius = float(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    PDwg.add(
        Circle(
            center=(cx, cy),
            r=radius,
            fill=fill,
            stroke=stroke
        )
    )

def saveSvg(PDwg: Drawing) -> None:
    filename = input("Insert filename: ").strip()
    print(f'Saving file to "{filename}"')
    proceed = input("Proceed (y/n)?: ").strip().lower()
    if proceed == "y":
        PDwg.filename = filename
        PDwg.save(pretty=True, indent=2)
        print("Vector saved successfully!")

def showMenu() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")


def main() -> None:
    print("Program starting.")
    dwg = svgwrite.Drawing()
    while True:
        showMenu()
        choice = input("Your choice: ").strip()
        if choice == "1":
            drawSquare(dwg)
        elif choice == "2":
            drawCircle(dwg)
        elif choice == "3":
            saveSvg(dwg)
        elif choice == "0":
            print("Exiting program.")
            break
        else: 
            print("Unknown option")



if __name__ == "__main__":
    main()
    print("Program ending.")

