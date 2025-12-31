#A7 Task 4.py

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)
class TIMESTAMP:
    weekday: str
    price: float

# Constants
DELIMITER = ";"
  # iterate over lines

def readFile(PFilename: str, PRows: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))
    print("Electricity usage:")
    PRows.clear()
    try:
        with open(PFilename, 'r', encoding = "utf-8" ) as file:
         FirstLine = True 
         for line in file:
            if FirstLine: 
                FirstLine = False
                continue
            if line == "\n":
                continue
            PRows.append(line.strip())
        file.close()    
    except FileNotFoundError:                         # To catch the error and print a message in response
     print (f"Error! File {PFilename} not found")
    return None

def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    PResults.clear()
    WeekdayTimestampAmount: list[int] = [0, 0, 0, 0, 0, 0, 0]
    for row in PRows:
        for i in range(len(WEEKDAYS)):
            if row.startswith(WEEKDAYS[i]):
                WeekdayTimestampAmount[i] += 1
                break
    for i in range(len(WEEKDAYS)):
        result = f" - {WEEKDAYS[i]} {WeekdayTimestampAmount[i]} stamps"
        PResults.append(result)
    return None

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for line in PResults:
       print(line)
       Row = Line.rstrip()                 # Remove newline
       Columns = Row.split(DELIMITER)      # Splits the row into a list
       Timestamp = TIMESTAMP()             # Create object
       Timestamp.weekday = Columns[0]      # Collect the first column
       Timestamp.weekday = Columns[1]      # Collect rest of the columns...
    Timestamp.price = float(Columns[3])    # Collect the fourth column and convert datatype
    Columns.clear()
    print("### Timestamp analysis ###")
    return None

def main() -> None:
    print("Program Starting.")
    PRows: list[str] = []
    PResults: list[str] = []
    Filename = input("Insert filename: ")
    readFile(Filename, PRows)
    analyseTimestamps(PRows, PResults)
    displayResults(PResults)
    PRows.clear()
    PResults.clear()
    return None



if __name__ == "__main__":
    main()  
    print("Program ending.") 
