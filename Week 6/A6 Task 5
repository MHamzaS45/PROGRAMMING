#A6 Task 5
#Create a program which can analyse numbers in a text file.

#Required values in analysis:
#Total - integer - Sum of numbers
#Count - integer - Rows that contain values
#Greatest - integer - The greatest number of them all
#Average - decimal - The numbers average

def readValues(filename) -> str:
  # read operations...
  Values: str = ""
  with open(filename, "r", encoding="utf-8") as file:
    for line in file:
      line = line.strip()
      if line:
        Values += line + " "
  return Values

def analyseValues(values) -> str:
   numbers = values
   if len(numbers) == 0:
    print("No numbers found in file.")
   else:
    # Total
    Total = sum(int(num) for num in numbers.split())
    # Count
    Count = len(numbers.split())
    # Greatest
    Greatest = max(int(num) for num in numbers.split())
    # Average
    Average = Total / Count 
    return f"Count;Sum;Greatest;Average\n{Count};{Total};{Greatest};{Average:.2f}\n"

def main():
    print("Program starting")
    filename = input("Insert filename: ")
    if filename == "":
        print("No filename provided. ")
        return
    else:
     try:
         values = readValues(filename)
         print("#### Number analysis - START ####")
         print (f"File "+filename+" results: ")
         result = analyseValues(values)
         print(result)
         print("#### Number analysis - END ####")
     except FileNotFoundError:
         print(f"Error: File not found.")

   

if __name__ == "__main__":
  main()
  print("Program ending.")
