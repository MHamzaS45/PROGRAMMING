#A5 TASK 2.py
def frameWord(PWord):
    length = len(PWord)
    print ("*" * (length + 4))
    print ("* " + PWord + " *")
    print ("*" * (length + 4))
    return None

def main():
    print ("Program Starting.")
    print()
    Feed = input("Insert Word: ")
    print()
    frameWord(Feed)
    print()
    print ("Program Ending.")
    return None 

main ()


