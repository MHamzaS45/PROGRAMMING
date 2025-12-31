#  A7 Task 7.py
# Featured Project - Enigma Machine Simulator

# Enigma Machine – A7 Assignment (CamelCase variables)

ALPHABET = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def LoadConfig(Filename: str):
    Rotors = []
    ReflectorStr = ""
    with open(Filename, "r", encoding="utf-8") as File:
        for Line in File:
            Line = Line.strip()
            if Line.startswith("Rotor"):
                Rotors.append(Line.split(":")[1])
            elif Line.startswith("Reflector"):
                ReflectorStr = Line.split(":")[1]
    return Rotors, ReflectorStr


def BuildReflector(ReflectorStr: str) -> dict:
    Reflector = {}
    for Index in range(26):
        Reflector[ALPHABET[Index]] = ReflectorStr[Index]
    return Reflector

def BuildReverseRotor(Rotor: str) -> dict:
    ReverseRotor = {}
    for Index, Letter in enumerate(Rotor):
        ReverseRotor[Letter] = ALPHABET[Index]
    return ReverseRotor


def RotatePositions(Positions: list[int]) -> None:
    Positions[0] = (Positions[0] + 1) % 26
    if Positions[0] == 0:
        Positions[1] = (Positions[1] + 1) % 26
        if Positions[1] == 0:
            Positions[2] = (Positions[2] + 1) % 26


def ForwardPass(Letter: str, Rotor: str, Position: int) -> str:
    Index = (ALPHABET.index(Letter) + Position) % 26
    Scrambled = Rotor[Index]
    return ALPHABET[(ALPHABET.index(Scrambled) - Position) % 26]


def ReversePass(Letter: str, ReverseRotor: dict, Position: int) -> str:
    Index = (ALPHABET.index(Letter) + Position) % 26
    Mapped = ReverseRotor[ALPHABET[Index]]
    return ALPHABET[(ALPHABET.index(Mapped) - Position) % 26]


def ProcessCharacter(Char: str, Rotors: list[str], ReverseRotors: list[dict], Reflector: dict, Positions: list[int]) -> str: 
    RotatePositions(Positions)
    for I in range(3):
        Char = ForwardPass(Char, Rotors[I], Positions[I])
    Char = Reflector[Char]
    for I in range(2, -1, -1):
        Char = ReversePass(Char, ReverseRotors[I], Positions[I])
    return Char


def main() -> None:
    ConfigFile = input("Insert config(filename): ")
    Rotors, ReflectorStr = LoadConfig(ConfigFile)
    PlugChoice = input("Insert plugs (y/n)?: ")
    print("No extra plugs inserted.")
    Reflector = BuildReflector(ReflectorStr)
    ReverseRotors = []
    for Rotor in Rotors:
        ReverseRotors.append(BuildReverseRotor(Rotor))
    print("Enigma initialized.\n")
    while True:
        Row = input("Insert row (empty stops): ").upper()
        if Row == "":
            print("\nEnigma closing.")
            break
        Positions = [0, 0, 0]
        Result = ""
        for Char in Row:
            if Char not in ALPHABET:
                continue
            Illuminated = ProcessCharacter(Char, Rotors, ReverseRotors, Reflector, Positions)
            print(f'Character "{Char}" illuminated as "{Illuminated}"')
            Result += Illuminated
        print(f'Converted row - "{Result}".\n')


if __name__ == "__main__":
    main()  
    print("Program ending.") 

