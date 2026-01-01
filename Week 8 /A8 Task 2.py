#A8 T2.py

import cat
def showOptions() -> int:
    print("Options:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")
    try:
      Feed = int(input("Your choice: "))
    except ValueError:
        print("Unknown option!")
        return
    return Feed

def askChoice() -> int:
    try:
      Choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input!")
        return
    return Choice

def askValue(PPrompt: str) -> float:
    try:
      Value = float(input(Prompt))
    except ValueError:
        print("Invalid input!")
        return
    return Value


def add(PAddend1: float, PAddend2: float) -> float:
    return PAddend1 + PAddend2

def subtract(PMinuend: float, PSubtrahend: float) -> float: 
def multiply(PMultiplicant: float, PMultiplier: float) -> float:
def divide(PDividend: float, PDivisor: float) -> float:

def main() -> None:
     
