#CheatSheet 3 Loops 
Children = 3
Hometown = "Lahti"

TownsInFinland = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]

RandomInformation = ["Hamza", 20, Children, Hometown, True]

print (TownsInFinland[0])
print (TownsInFinland[-1])
print (TownsInFinland)

TownsInFinland.append("Rovaniemi")
#[TownsInFinland = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere", "Rovaniemi"]
print (TownsInFinland)

NumOfTowns = len(TownsInFinland)
print (NumOfTowns)

print(TownsInFinland[NumOfTowns-1])
# = Rovaniemi
print (TownsInFinland[1])
# = Helsinki
print (TownsInFinland[0])
# = Lahti
print (TownsInFinland[-1])
# = Rovaniemi
num = 3
print (TownsInFinland[num])
Name = len("Hamza") #4
print (TownsInFinland[Name])
Greeting = len("Hi") #2
print (TownsInFinland[Greeting])

Num1 = 4
print (TownsInFinland[Num1])
#Lists
Village = ["Asikkala", "Hollola", "Kärvia", "Kempele"]
Towns = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]
#Table
VillagesAndTowns = [Village,Towns]
print (VillagesAndTowns[1][-2])
print (VillagesAndTowns[0][2])
# if we print (VillagesAndTowns[3][0]) # error as there is no index 3, Index 1 is Village and Index 2 is Towns

Towns.sort()
print(Towns)

#Dictionary
Teacher = {
    'name': 'Hamza',
    'age': 20,
    'city': 'Lahti'

}

print(Teacher['name'])

Empty = {}
Empty['street'] = 'Mukkulankatu 19'

Empty = {}

Teacher["city"] = "Tampere"

for key in Teacher:
    print (key)
    print (Teacher[key])

TownsAgain = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]
for town in TownsAgain:
    print (f"The town of {town}")

for i in range (1, 13):
    print(i)

for i in range (1,10):
    print(i, end=" ")

#Loop + Loop with step value of 3
for i in range (1,10,3):
    print (i)

Total = 0 
for i in range (1,10):
    Total += i
    print (Total)
print(Total)

# For Loop
# While Loop
# Break command in While Loop
# Continue command in While Loop



