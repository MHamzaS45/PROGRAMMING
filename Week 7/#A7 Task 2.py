#A7 Task 2.py
#Create a Python program that processes a list of comma-separated integers entered by the user.
#The program will perform the following operations:
#Parse the input, validate that all entries are valid integers.
#If an invalid value is detected, output an error message indicating the invalid value, but still process the valid integers.
#Calculate the sum of the valid integers and determine if the sum is even or odd.
#Display the total count of valid integers, the sum of the integers, and whether the sum is even or odd.
#If no valid integers are provided, display an appropriate message.

def askInput(): 
    Feed = input("Insert a list of comma-separated integers: ")
    ValuesSplit = Feed.split(",")
    ValuesList: list[int] = []
    for i in range(len(ValuesSplit)):
        Value = ValuesSplit[i].strip() 
        if Value.strip('-').isnumeric(): #Account for negative
           ValuesList.append(int(Value))
        else:
            print(f"Invalid value '{Value}' detected.")
    return ValuesList

def analyseValues(ValuesList: list[int]):
    if not ValuesList:
        print("No values to analyse.")
        return
    Total = sum(ValuesList)
    Count = len(ValuesList)
    EvenOdd = "even" if Total % 2 == 0 else "odd"
    print(f"There are {Count} integers in the list\nSum of the integers is {Total} and it's {EvenOdd}")

def main():
    print("Program starting.")
    List = askInput()
    analyseValues(List)
    return None


if __name__ == "__main__":
    main()  
    print("Program ending.") 
