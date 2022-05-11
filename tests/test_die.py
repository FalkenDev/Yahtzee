"""
Test_die module
"""
import unittest
import random
from src.die import Die

class TestDie(unittest.TestCase):
    """
    Class TestDie
    """
    def test_create_no_value_argument(self):
        """ Test to create a object without send a argument to the constructor """
        random.seed("dice")
        d = Die()
        self.assertEqual(3, d.value)

    def test_create_with_value_argument(self):
        """Test to create a object with a value on dice to the constructor """
        d = Die(2)
        self.assertEqual(2, d.value)

    def test_create_with_unvaliable_value_argument(self):
        """ Test to create a object with unvaliable value on dice to the constructor"""
        d = Die(100)
        self.assertEqual(6, d.value)

    def test_roll_get_random_value(self):
        """ Test so roll() get a random value """
        random.seed("dice")
        d = Die()
        d.roll()
        self.assertEqual(4, d.value)

    def test_get_name_returns_correct_name(self):
        """ Test get_name() returns correct name """
        d = Die(6)
        self.assertEqual("six", d.get_name())

    def test_str_return_correct_value_and_is_a_string(self):
        """ Test __str__() returns correct value in a string """
        d = Die(2)
        self.assertEqual(print("2"), print(d.value))


class TestDie2(unittest.TestCase):
    """
    Class TestDie2 ( Kmom02 )
    """
    def test_eq_returns_true_when_compare_to_another_die(self):
        """ Test if __eq__ returns ture when compare to another die object """
        random.seed("test")
        d = Die()
        c = Die()
        self.assertEqual(True, d == c)
