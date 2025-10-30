#A6 Task 2
print("Program starting.")
FirstName = input("Insert first name: ")
SecondName = input("Insert last name: ")
FileName = input("Insert file name: ")
file = open(FileName, "w")
file.write(FirstName + "\n")
file.write(SecondName + "\n")   
file.close()

