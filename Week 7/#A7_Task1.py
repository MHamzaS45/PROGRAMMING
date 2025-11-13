#A7_Task1
def askPositiveInteger () -> int:
    PositiveInt = -1
    Feed = input("Insert a positive integer (negative stops): ")
    if Feed.isnumeric(): #To ENSURE input is numeric and not string or something else
        PositiveInt = int(Feed)
    return PositiveInt

def displayIntegers(Numbers: list[int]):
    if len(Numbers) == 0: #If the list is empty
        print("No integers to display.")
    else:
        print(f"Displaying  {len(Numbers)}  positive integers:")
        for i in range (len(Numbers)):
            print (f" - Index {i}", end="") 
            print (f" => Ordinal {i+1} ", end="")
            print (f" => Integer {Numbers[i]}")

           
    return None

def main ():
    print("Program starting.")
    print("Collect positive integers")
    PositiveIntegers: list[int] = []
    CurrentInteger = askPositiveInteger() # Dump to ask first positive integer
    while CurrentInteger >= 0: 
        PositiveIntegers.append(CurrentInteger)
        CurrentInteger = askPositiveInteger()
    print ("Stopped collecting positive integers.")
    displayIntegers(PositiveIntegers)
    return None

if __name__ == "__main__":
    main()
