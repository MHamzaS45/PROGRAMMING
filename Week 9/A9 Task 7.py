########################################################
# Task A9_T4
# Developer Hamza Sahqani
# Date 2025-12-29
########################################################
import sys
import os

def showHelp() -> None:
    print("Invalid amount of arguments.")
    print(f"Usage: python {sys.argv[0]} <src_file> <dst_file>")

def copyFile(PSrcFile: str, PDstFile: str) -> None:
    proceed = True                     #Not using false statement
    print(f'Source file "{PSrcFile}"')
    print(f'Destination file "{PDstFile}"')
    print(f'Copying file "{PSrcFile}" to "{PDstFile}".')
    if os.path.exists(PDstFile):
        print(f'Destination file "{PDstFile}" already exists.')
        answer = input("Do you want to overwrite it? (y/n): ").strip().lower()
        if answer != "y":
            proceed = False
            sys.exit(1)
        elif answer = "y"
             proceed = True
             sys.exit(0)
    if proceed:
        try:
            with open(PSrcFile, "r", encoding="utf-8") as src:
                content = src.read()
            with open(PDstFile, "w", encoding="utf-8") as dst:
                dst.write(content)
        except Exception as error:
            print(f'Could not copy "{PSrcFile}" to "{PDstFile}".')
            print("Exiting program")
            sys.exit(-1)

   def main() -> None:
    print("Program starting.")
    if len(sys.argv) != 3:
        showHelp()
        print("Program ending.")
        sys.exit(0)
    srcFile = sys.argv[1]
    dstFile = sys.argv[2]
    copyFile(srcFile, dstFile)


if __name__ == "__main__":
    main()
    print("Program ending.")

