"""
Module Hand
"""
from src.die import Die

class Hand():
    """
    Hand Class
    """
    def __init__(self, dices = None):
        """
        Init
        """
        if isinstance(dices, list):
            self.dice = [Die(dices[0]), Die(dices[1]), Die(dices[2]), Die(dices[3]), Die(dices[4])]
        else:
            self.dice = [Die(), Die(), Die(), Die(), Die()]

    def roll(self, indexes = None):
        """Roll in index position"""
        if indexes is None:
            self.dice = [Die(), Die(), Die(), Die(), Die()]
        else:
            for position in indexes:
                self.dice[position] = Die()

        return self.dice

    def to_list(self):
        """ Make the hand object to a list with int from dice values"""
        int_list = []
        for dice in self.dice:
            int_list.append(dice.value)
        return int_list

    def __str__(self):
        """Return all dices to string"""
        return ", ".join(str(number) for number in self.dice)
