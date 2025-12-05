#A6 Task4.py
def readAnalyse(filename) -> str:
    file = open(filename, 'r', encoding="utf-8")
    names = []
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        line = line.strip()
        if len(line) == 0:
            continue
        parts = line.split(';')
        for name in parts:
            name = name.strip()
            names.append(name)
    file.close()    
    return names

def main():
 print ("Program starting.")
 print ("This program analyses a list of names from a file.")
 filename = input("Insert file name to read: ")
 if filename == "":
    print("No filename provided. ")
    return
 try:
  OpenFile = open(filename, "r", encoding="utf-8")
  print (f"Reading names from, {OpenFile}")
  names = readAnalyse(filename)
  print ("Analysing names...") 
  print ("Analysis complete!")
  print("#### REPORT BEGIN ####")
  if len(names) == 0:
        print("No names found in file.")
  else:
        # Name count 
        NameCount = len(names)
        # Average name
        TotalLength = sum(len(name) for name in names)
        AverageLength = TotalLength / NameCount
        # Shortest Name Characters 
        ShortestName = min(len(name) for name in names)
        #Longest Name Characters
        LongestName = max(len(name) for name in names)
        print(f"Name count - {NameCount}")
        print(f"Shortest Name - {ShortestName} characters")
        print(f"Longest Name - {LongestName} characters")
        print(f"Average Name - {AverageLength:.2f} characters")
        print("#### REPORT END ####")
 except FileNotFoundError:
  print(f"Error: File not found.")



if __name__ == "__main__":
 main()



print("Program Ending")
