""" Module Scoreboard.py """
from src.rules import Ones, Twos, Threes, Fours, Fives, Sixes, ThreeOfAKind, SmallStraight
from src.rules import LargeStraight, FullHouse, FourOfAKind, Yahtzee, Chance

class Scoreboard:
    """ Class scoreboard """
    _scoreboard_rules = {
        "Ones" : -1,
        "Twos" : -1,
        "Threes" : -1,
        "Fours" : -1,
        "Fives" : -1,
        "Sixes" : -1,
        "Three Of A Kind" : -1,
        "Small Straight" : -1,
        "Large Straight" : -1,
        "Full House" : -1,
        "Four Of A Kind" : -1,
        "Yahtzee" : -1,
        "Chance" : -1,
    }

    point_rule = {
        "Ones": Ones().points,
        "Twos": Twos().points,
        "Threes": Threes().points,
        "Fours": Fours().points,
        "Fives": Fives().points,
        "Sixes": Sixes().points,
        "Three Of A Kind": ThreeOfAKind().points,
        "Small Straight": SmallStraight().points,
        "Large Straight": LargeStraight().points,
        "Full House": FullHouse().points,
        "Four Of A Kind": FourOfAKind().points,
        "Yahtzee": Yahtzee().points,
        "Chance": Chance().points,
    }

    _total_points = 0

    @staticmethod
    def get_total_points():
        """ Get total points for all rules together"""
        return Scoreboard._total_points

    @staticmethod
    def add_points(rule_name, hand):
        """ Add points from rule and hand"""
        if Scoreboard._scoreboard_rules[rule_name] == -1:
            Scoreboard._scoreboard_rules[rule_name] = Scoreboard.point_rule[rule_name](hand)
            Scoreboard._total_points += Scoreboard._scoreboard_rules[rule_name]
        else:
            raise ValueError

    @staticmethod
    def get_points(rule_name):
        """ return points from specifik rule """
        return Scoreboard._scoreboard_rules[rule_name]

    @staticmethod
    def finished():
        """ Check if the game is finnished """
        for value in Scoreboard._scoreboard_rules.items():
            if value[1] == -1:
                return False
        return True

    @classmethod
    def from_dict(cls, points_dict: dict):
        """ Takes a dict with rule name and points to create a new scoreboard object"""
        Scoreboard._total_points = 0
        for key in points_dict:
            Scoreboard._scoreboard_rules[key] = points_dict[key]
            if points_dict[key] != -1:
                Scoreboard._total_points += points_dict[key]

        return Scoreboard()

    @staticmethod
    def get_scoreboard_list():
        """ Prints the scoreboard """
        scoreboard_string = []
        for value in Scoreboard._scoreboard_rules.items():
            if value[1] == -1:
                points = "-"
            else:
                points = value[1]

            scoreboard_string.append(points)

        return scoreboard_string
