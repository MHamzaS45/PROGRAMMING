#A2 Task 4.py
print("Program starting.")
print("Estimate how many minutes you spent on programming...\n")

a1_t1 = int(input("A1_T1: "))
a1_t2 = int(input("A1_T2: "))
a1_t3 = int(input("A1_T3: "))
a1_t4 = int(input("A1_T4: "))
a1_t5 = int(input("A1_T5: "))
a1_t6 = int(input("A1_T6: "))
a1_t7 = int(input("A1_T7: "))
print("")
Sum = a1_t1 + a1_t2 + a1_t3 + a1_t4 + a1_t5 + a1_t6 + a1_t7
Average = Sum / 7
RoundedAvg = int(round(Average))

print(f"In total you spent {total} minutes on programming.\n")
print(f"Average per task was {Average} min and same rounded to the nearest integer {RoundedAvg} min.\n")
print("Program ending.")
