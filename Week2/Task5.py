print("Program starting.\n")

Word = input("Insert a closed compound word: ")
length = len(Word)
lastword = Word[-1]
reversedword = Word[::-1]

print(f"The word you inserted is '{Word}' and in reverse it is '{reversedword}'.")
print(f"The inserted word length is {length}")
print(f"Last character is '{lastword}'\n")

print("Take substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))

substring = Word[start:end:step]

print(f"The word '{Word}' sliced to the defined substring is '{substring}'.")
print("Program ending.")
