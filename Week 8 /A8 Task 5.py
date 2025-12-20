#A8 Task 5 
#hashlib module
import hashlib
CREDENTIALS_FILE = "credentials.txt"

def menu() -> int:
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")
    return int(input("Your choice: "))

def idMenu():
    """Menu created when selecting and fulfilling conditions for Option 2"""
    print("User menu:")
    print("1 - View profile")
    print("2 - Change password")
    print("0 - Logout")
    return int(input("Your choice: "))

def hashPassword(password: str) -> str:
    md5 = hashlib.md5(password.encode())
    return md5.hexdigest()

def loadCredentials() -> list[list[str]]:
    users = []
    try:
        with open(CREDENTIALS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(";")
                if len(parts) == 3:
                    users.append(parts)
    except FileNotFoundError:
        return []
    return users

def saveCredentials(users: list[list[str]]):
    with open(CREDENTIALS_FILE, "w", encoding="utf-8") as file:
        for user in users:
            file.write(";".join(user) + "\n")

def userRegister():
    print("Register selected.")
    UserName = input("Insert new username: ")
    PassWord = input("Insert new password: ")
    hashed = hashPassword(PassWord)
    users = loadCredentials()
    new_id = len(users)
    users.append([str(new_id), UserName, hashed])
    saveCredentials(users)
    print(f"User '{UserName}' registered successfully!\n")

def userlogin() -> tuple[bool, str, str]:
    print("Login selected.")
    UserName = input("Insert username: ")
    PassWord = input("Insert password: ")
    hashed = hashPassword(PassWord)
    users = loadCredentials()
    for user in users:
        user_id, stored_username, stored_hash = user
        if stored_username == UserName and stored_hash == hashed:
            return True, user_id, UserName
    return False, "", ""


def main():
    print("Program starting.")
    while True:
        choice = menu()
        if choice == 2:
            userRegister()
        elif choice == 1:
            success, uid, uname = userlogin()
            if success:
                print("Authentication successful!\n")
                while True:
                    userChoice = idMenu()
                    if userChoice == 1:
                        print(f"Profile ID {uid} - {uname}\n")
                    elif userChoice == 2:
                        print("Change password not implemented.\n")
                    elif userChoice == 0:
                        print("Logging out...\n")
                        break
                    else:
                        print("Invalid choice.\n")
            else:
                print("Authentication failed!\n")
        elif choice == 0:
            print("Exiting program.\n")
            break
        else:
            print("Invalid choice. Try again.\n")
    print("Program ending.")


if __name__ == "__main__":
    main()
