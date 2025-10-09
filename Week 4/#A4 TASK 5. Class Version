#A4 TASK 5. Class Version
print("Program starting.\n")
Start = int(input("Insert starting point: "))
Stop = int(input("Insert stopping point: "))
Inspect = int(input("Insert inspection point: "))

Run = True
if (Start >= Stop):
    print("\nStarting point value must be less than the stopping point value.")
    Run = False
if ((Inspect < Start) or (Inspect > Stop)):
    print("\nInspection value must be within the range of start and stop.")
    Run = False
if(Run):
    print("\nFirst loop - inspection with break:")
    for i in range(Start, Stop):
        if (i == Inspect):
            break
        else:
          print(f"{i}", end=' ')
    print("")
    print("\nSecond loop - inspection with continue:")
    for i in range(Start, Stop):
        if (i == Inspect):
            continue
        else:
            print(i, end='')
print ("")
print("\n\nProgram ending.")
