# Program: Read and print file contents with decorative lines
print("Program starting.")
print("This program can read a file.")

# Ask the user for a filename
filename = input("Insert filename: ")

try:
    # Open the specified file for reading
    with open(filename, "r", encoding="utf-8") as file:
        # Print decorative start line
        print(f'#### START "{filename}" ####')

        # Print each line from the file
        for line in file:
            print(line, end="")  # end="" avoids extra blank lines

        # Print decorative end line
        print(f'\n#### END "{filename}" ####')

except FileNotFoundError:
    print(f'Error: File "{filename}" not found.')
file.close()

print("Program ending.")
