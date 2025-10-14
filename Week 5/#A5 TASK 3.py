#A5 TASK 3
def askname():
    Feed = input("Insert your name: ")
    return Feed
def greetUser(Pname):
    print (f"Hello {Pname}!")
    return None

def main():
    print("Program Starting.")
    Feed = askname()
    greetUser(Feed)
    print("Program ending.")
    return None 
main ()