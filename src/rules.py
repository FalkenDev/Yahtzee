""" Rule Module """

from abc import ABC, abstractmethod

class Rule(ABC):
    """ Class Rule: The main rule for all rules """
    @abstractmethod
    def points(self, hand):
        """ Abstract method Points"""

class SameValueRule(Rule):
    """ Inherit from Rule Class """
    def __init__(self, value, name):
        """ Init value and name"""
        self.value = value
        self.name = name

    def points(self, hand):
        """ Check how many dices is the same value"""
        dice_list = hand.to_list()
        total_points = 0
        for index in range(0, 5, 1):
            if self.value == dice_list[index]:
                total_points += self.value

        return total_points

class ThreeOfAKind(Rule): #klar
    """ Three Of A Kind Rule Class"""
    def __init__(self):
        self.name = "Three Of A Kind"

    def points(self, hand):
        """ Three Of A Kind points check method """
        dice_list = hand.to_list()
        count = 0
        total_points = 0
        sorted_hand = sorted(dice_list, key = dice_list.count, reverse=True)
        last_number = sorted_hand[0]

        for number in sorted_hand:
            if number == last_number:
                count += 1
                last_number = number

        if count >= 3:
            for number in dice_list:
                total_points += number

        return total_points

class SmallStraight(Rule): #klar
    """ Small Straight Rule Class """
    def __init__(self):
        self.name = "Small Straight"

    def points(self, hand):
        """ Small Straight points check method """
        dice_list = hand.to_list()
        count = 0
        controll_list = []
        total_points = 0

        for index in range(0, 5, 1):
            if dice_list[index] not in controll_list:
                controll_list.append(dice_list[index])

        controll_list = sorted(controll_list)

        rule_number_first_test = controll_list[0]
        rule_number_second_test = controll_list[1]

        for number in controll_list:
            if number == rule_number_first_test:
                rule_number_first_test += 1
                count += 1

            elif number == rule_number_second_test + 1:
                rule_number_second_test += 1
                count += 1

        if count == 4:
            total_points = 30

        return total_points

class LargeStraight(Rule): #klar
    """ Large Straight Rule Class """
    def __init__(self):
        self.name = "Large Straight"

    def points(self, hand):
        """ Large Straight points check method """
        dice_list = hand.to_list()
        sorted_hand = sorted(dice_list)
        rule_number = sorted_hand[0]
        count = 0
        total_points = 0

        for number in sorted_hand:
            if int(number) == rule_number:
                rule_number += 1
                count += 1

        if count == 5:
            total_points = 40

        return total_points

class FullHouse(Rule):
    """ Full House Rule Class """
    def __init__(self):
        self.name = "Full House"

    def points(self, hand):
        """ Full House points check method """
        dice_list = hand.to_list()
        sorted_hand = sorted(dice_list, key = dice_list.count, reverse=True)
        rule_number_three = sorted_hand[0]
        rule_number_two = sorted_hand[3]
        count_three = 0
        count_two = 0
        total_points = 0

        for number in sorted_hand:
            if int(number) == rule_number_three:
                count_three += 1

        for number in sorted_hand:
            if int(number) == rule_number_two:
                count_two += 1

        if count_three == 3 and count_two == 2:
            total_points = 25

        return total_points

class FourOfAKind(Rule): #klar
    """ Four Of A Kind Rule Class """
    def __init__(self):
        self.name = "Four Of A Kind"

    def points(self, hand):
        """ Four Of A Kind points check method """
        dice_list = hand.to_list()
        sorted_hand = sorted(dice_list, key = dice_list.count, reverse=True)
        rule_number = sorted_hand[0]
        count = 0
        total_points = 0

        for number in sorted(dice_list):
            if number == rule_number:
                count += 1

        if count >= 4:
            for number in dice_list:
                total_points += number

        return total_points

class Yahtzee(Rule): #klar
    """ Yahtzee Rule Class """
    def __init__(self):
        self.name = "Yahtzee"

    def points(self, hand):
        """ Yahtzee points check method """
        dice_list = hand.to_list()
        count = 0
        total_points = 0

        for index in range(0, 5, 1):
            if dice_list[index] == dice_list[0]:
                count += 1

        if count == 5:
            total_points = 50

        return total_points

class Chance(Rule): #klar
    """ Chance Rule Class """
    def __init__(self):
        self.name = "Chance"

    def points(self, hand):
        """ Chance points check method """
        dice_list = hand.to_list()
        total_points = 0

        for index in range(0, 5, 1):
            total_points += dice_list[index]

        return total_points


class Ones(SameValueRule):
    """ All the One Dices Class """
    def __init__(self):
        super().__init__(1, "Ones")

class Twos(SameValueRule):
    """ All the Two Dices Class """
    def __init__(self):
        super().__init__(2, "Twos")

class Threes(SameValueRule):
    """ All the Three Dices Class """
    def __init__(self):
        super().__init__(3, "Threes")

class Fours(SameValueRule):
    """ All the Four Dices Class """
    def __init__(self):
        super().__init__(4, "Fours")

class Fives(SameValueRule):
    """ All the Five Dices Class """
    def __init__(self):
        super().__init__(5, "Fives")

class Sixes(SameValueRule):
    """ All the Six Dices Class """
    def __init__(self):
        super().__init__(6, "Sixes")
