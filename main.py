"""
Main.py
"""
from src.hand import Hand
from src.menu import menustart, menurule
from src.selection import choise_function, roll_checker
from src.scoreboard import Scoreboard

def main():
    """
    Main
    """
    while True:
        menustart()

        choice = input("--> ")

        if choice == "r":
            count_roll = 0
            scoreboard = Scoreboard()
            user_hand = Hand()
            loop = False

            while True:
                d_print = ""
                for value in user_hand.to_list():
                    d_print += " [" + str(value) + "] "

                print(chr(27) + "[2J" + chr(27) + "[;H")
                print("Your have rolled: " + d_print)
                menurule(user_hand, scoreboard)

                choise = input("Choose a rule: ")

                rules = {
                    "1": "Ones",
                    "2": "Twos",
                    "3": "Threes",
                    "4": "Fours",
                    "5": "Fives",
                    "6": "Sixes",
                    "a": "Three Of A Kind",
                    "b": "Small Straight",
                    "c": "Large Straight",
                    "d": "Full House",
                    "e": "Four Of A Kind",
                    "f": "Yahtzee",
                    "g": "Chance",
                }
                try:
                    if choise == "roll":
                        count_roll = roll_checker(count_roll, user_hand, d_print)
                    else:
                        loop = choise_function(rules, choise, user_hand, scoreboard)
                except KeyError:
                    print("\nThat is not a valid choice.")
                    input("\nPress enter to go back to rule menu...")


                if loop is True:
                    break

        elif choice == "q":
            print("The yahtzee game has ended.")
            break

        else:
            print("\nThat is not a valid choice. Please choose from the menu.\n")

if __name__ == "__main__":
    main()
