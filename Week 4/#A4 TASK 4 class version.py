#A4 TASK 4 class version
print ("Program starting.\n")
WordCount = 0
CharCount = 0
word = input("Insert word (empty stops): ")
while word != "":
    WordCount += 1
    CharCount += len(word)
    word = input("Insert word (empty stops): ")
print ("")
print ("\nYou inserted:")
print (f"- {WordCount} words")
print (f"- {CharCount} characters")

print("\nProgram ending.")
