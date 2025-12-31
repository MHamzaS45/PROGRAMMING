#A7 Task 6.py 
#Featured Project - RPS
import random
random.seed(1234)

def optionsRPS(choice: int) -> str:
    if choice == 1:  # Rock Option
        return """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
    elif choice == 2:  # Paper Option
        return """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
    elif choice == 3:  # Scissors Option
        return """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


def choice_to_string(choice: int) -> str:
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    elif choice == 3:
        return "scissors"
    return ""


def determine_winner(player_choice: int, bot_choice: int) -> int:
    # return 0 = draw, 1 = player wins, -1 = bot wins
    if player_choice == bot_choice:
        return 0
    if (player_choice == 1 and bot_choice == 3) or \
       (player_choice == 2 and bot_choice == 1) or \
       (player_choice == 3 and bot_choice == 2):
        return 1

    return -1


def main() -> None:
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    player_name = input("Insert player name: ")
    bot_name = "RPS-3PO"

    print(f"Welcome {player_name}!")
    print(f"Your opponent is {bot_name}.")
    print("Game starts...\n")
    player_wins = 0
    player_losses = 0
    player_draws = 0
    bot_wins = 0
    bot_losses = 0
    bot_draws = 0

    while True:
        print("Options:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("0 - Quit game")
        choice = input("Your choice: ")
        if choice == "0":
            break
        if choice not in ("1", "2", "3"):
            print("Invalid choice.\n")
            continue

        player_choice = int(choice)
        bot_choice = random.randint(1, 3)
        print("Rock! Paper! Scissors! Shoot!\n")
        print("#" * 25)
        print(f"{player_name} chose {choice_to_string(player_choice)}.")
        print(optionsRPS(player_choice))
        print("#" * 25)
        print(f"{bot_name} chose {choice_to_string(bot_choice)}.")
        print(optionsRPS(bot_choice))
        print("#" * 25)

        result = determine_winner(player_choice, bot_choice)

        player_choice_str = choice_to_string(player_choice)
        bot_choice_str = choice_to_string(bot_choice)

        if result == 0:
            print(f"Draw! Both players chose {player_choice_str}.")
            player_draws += 1
            bot_draws += 1
        elif result == 1:
            print(f"{player_name} {player_choice_str} beats {bot_name} {bot_choice_str}.")
            player_wins += 1
            bot_losses += 1
        else:
            print(f"{bot_name} {bot_choice_str} beats {player_name} {player_choice_str}.")
            bot_wins += 1
            player_losses += 1
        print()
    print("\nResults:")
    print(f"{player_name} - wins ({player_wins}), losses ({player_losses}), draws ({player_draws})")
    print(f"{bot_name} - wins ({bot_wins}), losses ({bot_losses}), draws ({bot_draws})")


if __name__ == "__main__":
    main()
    print("\nProgram ending.")

