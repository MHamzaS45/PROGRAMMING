#a4 task 5.py
print("Program starting.\n")
Start = int(input("Insert starting point: "))
Stop = int(input("Insert stopping point: "))
Inspect = int(input("Insert inspection point: "))

if Start >= Stop:
    print("\nStarting point value must be less than the stopping point value.")
if Inspect < Start or Inspect > Stop:
    print("\nInspection value must be within the range of start and stop.")
else:
    print("\nFirst loop - inspection with break:")
    for i in range(Start, Stop + 1):
        if i == Inspect:
            break
        print(i, end=" " if i < Inspect - 1 else "")

    print("\nSecond loop - inspection with continue:")
    first = True
    for i in range(Start, Stop + 1):
        if i == Inspect:
            continue
        if not first:
            print(" ", end="")
        print(i, end="")
        first = False

print("\n\nProgram ending.")
