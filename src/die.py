""" Die Module """
import random

class Die():
    """
    Die class
    """
    MIN_ROLL_VALUE = 1
    MAX_ROLL_VALUE = 6

    def __init__(self, value = None):
        """
        Init
        """
        if value is None:
            self.roll()

        elif value > 6:
            self._value = Die.MAX_ROLL_VALUE

        elif value < 1:
            self._value = Die.MIN_ROLL_VALUE

        else:
            self._value = value

    def get_name(self):
        """
        Get value name
        """
        value_string = ""
        if self._value == 1:
            value_string = "one"

        elif self._value == 2:
            value_string = "two"

        elif self._value == 3:
            value_string = "three"

        elif self._value == 4:
            value_string = "four"

        elif self._value == 5:
            value_string = "five"

        else:
            value_string = "six"

        return value_string

    @property
    def value(self):
        """Get value"""
        return self._value

    def roll(self):
        """Roll dice"""
        self._value = random.randint(Die.MIN_ROLL_VALUE, Die.MAX_ROLL_VALUE)

    def __str__(self):
        """Resturn value in string"""
        return str(self._value)

    def __eq__(self, value):
        """ Check if value/die is the same value as the other value/die """
        if isinstance(value, object) is True:
            return bool(self._value == value)

        return bool(self._value == value)
