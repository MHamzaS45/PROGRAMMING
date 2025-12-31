########################################################
# A10 Task 1.py
# Developer: Muhammad Hamza Sahqani
# Date: 2025-12-21
########################################################

import sys

def display():
    global filename
    horizontal_box = []
    while True:
        try:
            filename = input("Insert filename: ").strip()
            try:
                with open(filename,"r") as file:
                    #vertically
                    print("#---Vertically---#")
                    for line in file:
                        line = line.strip()
                        if line: 
                            print(line)
                            horizontal_box.append(line)
                    print("#---Vertically---#")
                print("#---Horizontally---#")
                intNum = [int(num) for num in horizontal_box] 
                print_out = " , ".join(str(num) for num in intNum)
                print(print_out)
                print("#---Horizontally---#")
                break
            except FileNotFoundError:
                print(f"File \"{filename}\" not found. Try again!")
            except PermissionError:
                print("You do not have permission to access this file.")
        except ValueError:
            print("Please insert a filename!")
        except KeyboardInterrupt:
            print("User interupt the program.")
            print("Program ending.")
            sys.exit(0)

def main(): # Main function
    print("Program starting.")
    display()
    print("\nProgram ending.")


if __name__ == "__main__":
    main()

