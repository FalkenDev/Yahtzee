"""Menu"""
from src.rules import Ones, Twos, Threes, Fours, Fives, Sixes, ThreeOfAKind, SmallStraight
from src.rules import LargeStraight, FullHouse, FourOfAKind, Yahtzee, Chance


def menustart():
    """Prints the start menu"""
    #print(chr(27) + "[2J" + chr(27) + "[;H")
    print("r) Roll all the dices.")
    print("q) Quit.")

def menurule(hand, scoreboard):
    """ Prints the rule menu """
    scoreboard_list = scoreboard.get_scoreboard_list()
    data = [
        ["Choose", "Worth", "Rule", "Alredy Scored" ],
        ["(1)",  str(Ones().points(hand)), "Ones", str(scoreboard_list[0])],
        ["(2)", str(Twos().points(hand)), "Twos", str(scoreboard_list[1])],
        ["(3)", str(Threes().points(hand)), "Threes", str(scoreboard_list[2])],
        ["(4)", str(Fours().points(hand)), "Fours", str(scoreboard_list[3])],
        ["(5)", str(Fives().points(hand)), "Fives", str(scoreboard_list[4])],
        ["(6)", str(Sixes().points(hand)), "Sixes", str(scoreboard_list[5])],
        ["(a)", str(ThreeOfAKind().points(hand)), "Three Of A Kind", str(scoreboard_list[6])],
        ["(b)", str(SmallStraight().points(hand)), "Small Straight", str(scoreboard_list[7])],
        ["(c)", str(LargeStraight().points(hand)), "Large Straight", str(scoreboard_list[8])],
        ["(d)", str(FullHouse().points(hand)), "Full House", str(scoreboard_list[9])],
        ["(e)", str(FourOfAKind().points(hand)), "Four Of A Kind", str(scoreboard_list[10])],
        ["(f)", str(Yahtzee().points(hand)), "Yahtzee", str(scoreboard_list[11])],
        ["(g)", str(Chance().points(hand)), "Chance", str(scoreboard_list[12])],
    ]

    dash = '-' * 52
    value_pdata = len(data)

    for i in range(value_pdata):
        if i == 0:
            print(dash)
            print('{:<10s}{:>6s}{:>12s}{:>21s}'.format(data[i][0],data[i][1],data[i][2],data[i][3]))
            print(dash)
        else:
            print('{:<10s}{:>4s}{:^24s}{:>5s}'.format(data[i][0],data[i][1],data[i][2],data[i][3]))
    print("\n(roll) - Roll all or specific dices\n")
