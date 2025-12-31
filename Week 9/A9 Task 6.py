########################################################
# Task A9_T6
# Developer Hamza Sahqani
# Date 2025-12-20
########################################################

def saveLines(Lines: list[str], Filename: str) -> None:
    with open(Filename, "w", encoding="utf-8") as file:
        for line in Lines:
            file.write(line + "\n")

def main() -> None:
    Lines: list[str] = []
    print("Program starting.")
    try:
        while True:
            print("Options:")
            print("1 - Insert line")
            print("2 - Save lines")
            print("0 - Exit")
            choice = input("Your choice: ")
            if choice == "1":
                text = input("Insert text: ")
                Lines.append(text)
            elif choice == "2":
                if len(Lines) == 0:
                    print("No lines to save.")
                else:
                    filename = input("Insert filename: ")
                    saveLines(Lines, filename)

            elif choice == "0":
                break

            else:
                print("Invalid option.")

    except KeyboardInterrupt: # Catch keyboard interrupt
        print("Keyboard interrupt and unsaved progress!")
        if len(Lines) == 0:
            print("Program ending.")
            return
        answer = input("Save before quit(y/n)?: ").lower()
        if answer == "y":
            filename = input("Insert filename: ")
            saveLines(Lines, filename)


if __name__ == "__main__":
    main()
    print("\nProgram ending.")
