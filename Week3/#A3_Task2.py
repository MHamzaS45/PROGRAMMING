#A3_Task2
print ("Program Starting")
print ("String comparisons.")
Word1 = input("Insert first word: ")
Character = input("Insert a character: ")
if (Character in Word1):
    print (f"Word \"{Word1}\" contains character \"{Character}\"")
else:
    print (f"Word \"{Word1}\" does not character \"{Character}\"")
Word2 = input("Insert second word: ")
if (Word2 > Word1):
    print (f"The first word \"{Word1}\" is before the second word \"{Word2}\" alphabetically.")
elif (Word1 > Word2):
    print (f"The second word \"{Word2}\" is before the first word \"{Word1}\" alphabetically.")
else:
    print ("Both inserted words are the same alphabetically, ")
print ("Program ending.")