# A6 Task 6: Cipher Messages (Caesar Cipher) 
# #Create a Python program which collects plain text rows from user till the user inserts an empty row. 
# Cipher all rows and then ask user to choose between showing the ciphered text or saving it.

LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz" #Listing words that will be used
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shiftCharacter(char, alphabet): # Shift of letters for cipher 
    if char not in alphabet:
        return char
    index = alphabet.index(char)
    return alphabet[(index + 13) % 26]

def rot13(text): #Value of shift
    result = ""
    for ch in text:
        if ch.islower():
            result += shiftCharacter(ch, LOWER_ALPHABETS)
        elif ch.isupper():
            result += shiftCharacter(ch, UPPER_ALPHABETS)
        else:
            result += ch
    return result

def writeFile(filename, content): #To encrypt and write to a file
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(content)

def cipherConversion(shift: int) -> list: #User Input & Conversion Process
    Feed = []
    while True:
        line = input("Insert row (empty stops): ")
        if line == "":
            break
        Feed.append(line)
    ciphered_texts = [rot13(line) for line in Feed]
    return ciphered_texts

def main():
    print("Program starting.\n")
    print("Collecting plain text rows for ciphering.")
    ciphered_texts = cipherConversion(13)
    print("\n#### Ciphered text ####")
    for line in ciphered_texts:
        print(line)
    print("#### Ciphered text ####\n")
    filename = input("Insert filename to save ciphered text (or press Enter to skip): ")
    if filename.strip() == "":
        print("File name not defined.\nAborting save operation.")
        return
    try:
        writeFile(filename, "\n".join(ciphered_texts))
        print(f"Ciphered text saved to {filename}.")
    except Exception as e:
        print("Error saving file:", e)


if __name__ == "__main__":
    main()
    print("Program ending.")
