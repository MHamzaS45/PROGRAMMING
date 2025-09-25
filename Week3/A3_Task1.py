#A3_Task1
print ("Program-Starting. \n Insert two integers")
Feed1 = int(input("Insert first integer: "))
Feed2 = int(input("Insert second integer: "))
print ("Comparing inserted integers.")
if (Feed1 > Feed2):
    print ("The first integer is larger than the second integer") 
elif Feed1 == Feed2:  
    print ("Both integers are the same") 
else:
    print ("The first integer is smaller than the second integer")
#Adding integers together
print ("Adding integers together")
Sum = Feed1 + Feed2
print (f"{Feed1} + {Feed2} = {Sum}")
print ("Checking the parity of the sum...")
#Parity check
Remainder = Sum % 2
if (Remainder == 0):
    print ("Sum is even. ")
else: 
    print("Sum is odd. ")
print ("Program ending.")
