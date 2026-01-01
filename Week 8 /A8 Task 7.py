#A8 Task 7.py
# refer to a8 task 6 for svgwrite documentation
import math 
import svgwrite
from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle, Polygon

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
        Circle(                    #Circle shape
            center=(cx, cy),
            r=radius,
            fill=fill,
            stroke=stroke
        )
    )


def drawHexagon(PDwg: Drawing) -> None:
    print("Insert hexagon details:")
    cx = float(input("Middle point X: "))
    cy = float(input("Middle point Y: "))
    apothem = float(input("Apothem length: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")
    circumradius = apothem / math.cos(math.radians(30))
    points = []
    angles = [330, 30, 90, 150, 210, 270]
    for angle in angles:
        x = cx + circumradius * math.cos(math.radians(angle))
        y = cy + circumradius * math.sin(math.radians(angle))
        points.append((round(x), round(y)))
    PDwg.add(
        Polygon(              #Polygon shape
            points=points,
            fill=fill,
            stroke=stroke
        )
    )

def saveSvg(PDwg: Drawing) -> None:               #Function to save svg file
    filename = input("Insert filename: ").strip()
    if not filename.lower().endswith(".svg"):
        filename += ".svg"
    print(f'Saving file to "{filename}"')
    proceed = input("Proceed (y/n)?: ").strip().lower()
    if proceed == "y":
        PDwg.filename = filename
        PDwg.save(pretty=True, indent=2)
        print("Vector saved successfully!")

def displayMenu() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Draw hexagon")
    print("4 - Save svg")
    print("0 - Exit")

def main() -> None:
    print("Program starting.")           
    dwg = svgwrite.Drawing()
    while True:                        #Same menu loop as previous tasks
        displayMenu()
        choice = input("Your choice: ").strip()
        if choice == "1":
            drawSquare(dwg)
        elif choice == "2":
            drawCircle(dwg)
        elif choice == "3":
            drawHexagon(dwg)
        elif choice == "4":
            saveSvg(dwg)
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Unknown option")


if __name__ == "__main__":
    main()
    print("Program ending.")

