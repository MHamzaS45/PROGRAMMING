########################################################
# Task A9_T1 
# Developer Hamza Sahqani
# Date 2025-12-25
########################################################

def userInput(): 
    values = []
    while True:
        Feed = input("Insert a floating-point value (0 to stop): ")
        try:
            value = float(Feed)
            if value == 0:
                break
            values.append(value)
        except ValueError:
            print("Error! '{}' couldn't be converted to float.".format(Feed))
    return values


def main():
    print("Program starting.\n")
    values = userInput()
    total = sum(values)
    print("Final sum is {:.2f}".format(total))
  
if __name__ == "__main__":
    main()
    print("Program ending.")
