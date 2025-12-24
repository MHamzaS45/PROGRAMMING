#A1 Task 7
# Fuel consumption
print ("Calculate fuel consumption")
Feed = input("Enter travel distance (kilometers): ")
Distance = int(Feed)
if Distance < 0:
    print("Error: Distance must be a positive integer.")    
else:
    Feed = input("Enter fuel usage (liters): ")
    Fuel = int(Feed)
    if Fuel < 0:
        print("Error: Fuel consumption must be a positive integer.")
    else:
        Consumption = (Fuel / Distance) * 100
        print(f"Total fuel consumption: {Consumption} l per 100 km")
