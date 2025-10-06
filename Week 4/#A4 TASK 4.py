#A4 TASK 4.py
print ("Program starting.\n")
WordCount = 0
CharCount = 0
while True:
    word = input("Insert word (empty stops): ")
    if word == "":
        break
    WordCount += 1
    CharCount += len(word)

print ("\nYou inserted:")
print (f"- {WordCount} words")
print (f"- {CharCount} characters")

print("\nProgram ending.")
