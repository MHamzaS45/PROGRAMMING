#A9 Task 5.py
def getRGB() -> bool:
    global R, G, B, hexColor                       #So it can be used in the main function
    try:
        R = int(input("Insert red: "))
        if not (0 <= R <= 255):                #Better to find range
            raise Exception                    #Continue the program execution to the end normally skipping the RGB displaying part. One way to achieve this is to use “try-except” for the whole process and then any incorrect value being collected raises exception
        G = int(input("Insert green: "))
        if not (0 <= G <= 255):             
            raise Exception
        B = int(input("Insert blue: "))
        if not (0 <= B <= 255):
            raise Exception
        hexColor = "#{:02x}{:02x}{:02x}".format(R, G, B)
        return True
    except Exception:
        print("Couldn't perform the designed task due to the invalid input values.")
        return False

def main() -> None:
    print("Program starting.")
    if getRGB():
        print("RGB Details:")
        print(f"- Red {R}")
        print(f"- Green {G}")
        print(f"- Blue {B}")
        print(f"- Hex {hexColor}")
    return None

if __name__ == "__main__":
    main()
    print("Program ending.")

