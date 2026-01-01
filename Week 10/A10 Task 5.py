########################################################
# Task A10_T5 - Recursive Factorial
# Developer Hamza Sahqani
# Date 2025-12-30
########################################################

#Create a CLI program which can calculate factorial recursively. Collect factorial from the user input.

def recursiveFactorial(PNum: int) -> int:
    if PNum == 0 or PNum == 1:
        return 1
    else:
        return PNum * recursiveFactorial(PNum - 1) # Factorial formula (recursive):n! = n × (n − 1)!

def main() -> None:
    print("Program starting.")
    try:
        Feed = int(input("Insert factorial: "))
        if Feed < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"Factorial {Feed}!")
            answer = recursiveFactorial(Feed)
            print(f"{Feed} = {answer}")
    except ValueError:
        print("Invalid input. Please insert an integer value.")

    print("Program ending.")


if __name__ == "__main__":
    main()

