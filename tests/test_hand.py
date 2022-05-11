"""
Test_Hand module
"""
import unittest
import random
from unittest import mock
from src.hand import Hand

class TestHand(unittest.TestCase):
    """
    class TestHand to test Hand class
    """
    def test_create_object_no_argument(self):
        """ Test to create a object without send a argument to the constructor """
        random.seed("dice")
        h = Hand()
        self.assertEqual("3, 4, 3, 4, 5", str(h))

    def test_create_object_with_listdice_agrument(self):
        """ Test create object with list of dices in agrument """
        h = Hand([1,2,3,4,5])
        self.assertEqual([1, 2, 3, 4, 5], h.to_list())

    def test_roll_list_argument_into_right_dices(self):
        """ Test so Roll() with a list as an argument turns the correct dices position. """
        random.seed("dice")
        h = Hand()
        h.roll([1,3])
        self.assertEqual([3, 6, 3, 2, 5], h.to_list())

    def test_roll_no_argument_into_right_dices(self):
        """ Test so Roll() without argument turns the correct dices position"""
        random.seed("dice")
        h = Hand()
        h.roll()
        self.assertEqual([6, 2, 5, 1, 4], h.to_list())

    def test_tolist_resturns_a_list_with_value(self):
        """ Test so to_list() returns a list with dice values """
        random.seed("dice")
        h = Hand()
        self.assertEqual([3, 4, 3, 4, 5], h.to_list())

class TestHand2(unittest.TestCase):
    """
    Class TestHand2 to test Hand Class ( Kmom03 )
    """
    def test_roll_with_mock(self):
        """
        Test roll method with mock to Die()
        """
        with mock.patch.object(random, "randint") as mock_random:
            mock_random.return_value = 100
            roll = Hand().roll()
            self.assertEqual(roll, [100,100,100,100,100])
