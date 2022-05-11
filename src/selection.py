""" Module selection"""
def choise_function(rules, choise, hand, scoreboard):
    """ If not roll  or random choises """
    break_loop = False

    try:
        scoreboard.add_points(rules[choise], hand)
        rule_points = str(scoreboard.get_points(rules[choise]))
        print("\nYou got " + rule_points + " Points\n")

        if scoreboard.finished() is True:
            print(chr(27) + "[2J" + chr(27) + "[;H")
            total_points = str(scoreboard.get_total_points())
            print("Game is over, you got: " + total_points + " Points")
            input("\nThank You for playing :)")

        break_loop = True

    except ValueError:
        print("You have alredy used that rule!")
        input("\nPress enter to go back to rule menu...")

    return break_loop

def roll_checker(rolled, hand, dices):
    """ Roll all / specific dices when player use roll rule"""
    if rolled > 1:
        print("\nYou have used all your rolls, please choose a point rule!")
        input("\nPress enter to go back to rule menu...")
    else:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print("Your dices is: " + dices)
        print("\nEnter wich dices u want to roll:")
        print("\nAll dices = press space")
        print("Specifc dices = Enter number and seperate with , like 1,2,3\n")
        choise_roll = input("--> ")
        roll_dices(choise_roll, hand)
        rolled += 1
    return rolled

def roll_dices(choise, hand):
    """ Roll all / specific dices """
    if len(choise) > 0:
        roll_specific = list(choise.split(","))
        value_specific = len(roll_specific)
        for index in range(value_specific):
            roll_specific[index] = (int(roll_specific[index]) - 1)

        hand.roll(roll_specific)
    else:
        hand.roll()
