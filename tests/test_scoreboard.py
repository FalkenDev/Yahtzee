""" Scoreboard test module """
import unittest
from src.scoreboard import Scoreboard
from src.hand import Hand


class TestScoreboard(unittest.TestCase):
    """
    class TestHand to test Hand class
    """
    def test_add_points_get_correct_points(self):
        """ Test add_points to get correct points"""
        h = Hand([6,6,6,6,6])
        Scoreboard().add_points("Yahtzee", h)
        f = Scoreboard().get_points("Yahtzee")
        self.assertEqual(f, 50)

    def test_add_points_to_rule_alredy_used(self):
        """ Test add_points to a rule that alredy has been used"""
        h1 = Hand([6,6,6,6,6])

        with self.assertRaises(ValueError):
            Scoreboard().add_points("Yahtzee", h1)
