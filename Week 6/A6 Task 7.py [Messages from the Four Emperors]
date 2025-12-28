#A6 Task 7.py 
#Messages from the Four Emperors game
#import pygame 

PROGRESS_FILE = "player_progress.txt"

LOCATIONS = {
    0: "home",
    1: "Galba's palace",
    2: "Otho's palace",
    3: "Vitellius' palace",
    4: "Vespasian's palace" # No comma to be added at the end
}
 
def rot13(text): # Caesar cipher
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += ch
    return result

def previousSave(name):
    try:
        open(name, "r").close()
        return True
    except:
        return False

def initializeProgress():
    if not previousSave(PROGRESS_FILE):
        f = open(PROGRESS_FILE, "w")
        f.write("current_location;next_location;passphrase\n")
        f.write("0;1;qvfpvcyvar\n")
        f.close()

def readProgress():
    f = open(PROGRESS_FILE, "r")
    lines = f.read().strip().split("\n")
    f.close()
    return lines[-1].split(";")

def appendProgress(line):
    f = open(PROGRESS_FILE, "a")
    f.write("\n" + line)
    f.close()

def runGame():
    initialize_progress()

    last = read_last_progress()

    # If this is a normal progress row
    if len(last) == 3:
        current_id = int(last[0])
        next_id = int(last[1])
        cipher_pass = last[2]
    else:
        # Last line was a message, so read the row before it
        f = open(PROGRESS_FILE, "r")
        rows = f.read().strip().split("\n")
        f.close()
        prev = rows[-2].split(";")
        current_id = int(prev[0])
        next_id = int(prev[1])
        cipher_pass = prev[2]

    if next_id > 4:
        print("All emperors visited. Journey complete.")
        return

    print("Travel starting.")
    print("Currently at " + LOCATIONS[current_id] + ".")
    print("Travelling to " + LOCATIONS[next_id] + "...")
    print("...Arriving to the " + LOCATIONS[next_id] + ".")
    print("Passing the guard at the entrance.")

    plain_pass = rot13(cipher_pass)
    print("\"" + plain_pass.capitalize() + "!\"")

    print("Looking for the message in the palace...")

    gkgfile = str(next_id) + "_" + cipher_pass + ".gkg"
    try:
        f = open(gkgfile, "r")
        cipher_message = f.readline().strip()
        f.close()
    except:
        print("Message file missing:", gkgfile)
        return

    print("Ah, there it is! Seems cryptic.")

    appendProgress(cipher_message)
    print("[Game] Progress autosaved!")

    print("Deciphering Emperor's message...")
    plain_message = rot13(cipher_message)

    output_file = str(next_id) + "-" + plain_pass + ".txt"
    f = open(output_file, "w")
    f.write(plain_message)
    f.close()

    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")

    if next_id < 4:
        appendProgress(
            str(next_id) + ";" +
            str(next_id + 1) + ";" +
            rot13(plain_pass)
        )

if __name__ == "__main__":
    main()
