from unittest import mock
import unittest
import re
from deck import generate_deck_list
from actions import is_natural, get_username, deal_cards, stand_or_hit, if_stand, dealer_sum



class TestingIsNatural(unittest.TestCase):
    """Test to check if the function can catch that two cards make 21 (10 + ace)"""

    def test_is_natural_true(self):
        """This is testing a card of value 10 plus an ace. Other parameters don't value"""
        test_hand = (("x", "x", 10), ("x", "x", 1))
        test = is_natural(test_hand)
        self.assertTrue(test)

    def test_is_natural_false_ace(self):
        """This is testing a card of value other than 10 plus an ace. Other parameters don't value"""
        test_hand = (("x", "x", 5), ("x", "x", 1))
        test = is_natural(test_hand)
        self.assertFalse(test)

    def test_is_natural_false_ten(self):
        """This is testing a card of value other than 10 plus a 10. Other parameters don't value"""
        test_hand = (("x", "x", 5), ("x", "x", 10))
        test = is_natural(test_hand)
        self.assertFalse(test)

class TestingGetUsername(unittest.TestCase):
    """Test to check if only valid user input is stored"""

    def test_username_spaces(self):
        """Test if white spaces are stripped correctly and if name is capitalized"""

        with mock.patch('builtins.input', return_value="\t user\n"):
            self.assertEqual(get_username(), "User")


class TestingDealCards(unittest.TestCase):
    """Test to check if deal_cards works fine"""

    def test_cards_not_in_deck(self):
        """Test if the two cards dealt are missing from the deck"""
        deck_test = generate_deck_list()
        player_hand_test = []
        dealer_hand_test = []
        self.dealer_hand_test = []

        deal_cards(player_hand_test, dealer_hand_test, deck_test)

        # Test for player cards
        self.assertNotIn(player_hand_test[0], deck_test)
        self.assertNotIn(player_hand_test[1], deck_test)

        # Test for dealer cards
        self.assertNotIn(dealer_hand_test[0], deck_test)
        self.assertNotIn(dealer_hand_test[1], deck_test)

    def test_hand_length(self):
        """Test if exactly two cards are dealt"""
        deck_test = generate_deck_list()
        player_hand_test = []
        dealer_hand_test = []
        self.dealer_hand_test = []

        deal_cards(player_hand_test, dealer_hand_test, deck_test)

        # Test hands' length
        self.assertEqual(len(player_hand_test), 2)
        self.assertEqual(len(dealer_hand_test), 2)


class TestingStandorHit(unittest.TestCase):
    """Test to check  works fine"""

    def test_returns_false(self):
        """Check if 's' returns False"""

        with mock.patch('builtins.input', return_value="s"):
            self.assertEqual(stand_or_hit(), False)

    def test_returns_true(self):
        """Check if 'h' returns True"""

        with mock.patch('builtins.input', return_value="h"):
            self.assertEqual(stand_or_hit(), True)


class TestingIfStand(unittest.TestCase):
    """Testing if if_stand works as intended"""

    def test_if_stand_17_false(self):
        """Check if it returns false with 17"""
        player_hand = ((0, 0, 2), (0, 0, 2))
        dealer_hand = ((0, 0, 10), (0, 0, 7))
        self.assertEqual(if_stand(dealer_hand, player_hand), False)

    def test_if_stand_21_false(self):
        """Check if it returns true with 21 (natural)"""
        player_hand = ((0, 0, 2), (0, 0, 2))
        dealer_hand = ((0, 0, 1), (0, 0, 10))
        self.assertEqual(if_stand(dealer_hand, player_hand), False)

    def test_if_stand_lots_cards_false(self):
        """Check if it returns true with big number composed by many small cards"""
        player_hand = ((0, 0, 2), (0, 0, 2))
        dealer_hand = ((0, 0, 2), (0, 0, 2), (0, 0, 3), (0, 0, 4), (0, 0, 5), (0, 0, 6), (0, 0, 7), (0, 0, 8))
        self.assertEqual(if_stand(dealer_hand, player_hand), False)

    def test_if_stand_16_true(self):
        """Check if it returns true with 16"""
        player_hand = ((0, 0, 2), (0, 0, 2))
        dealer_hand = ((0, 0, 10), (0, 0, 6))
        self.assertEqual(if_stand(dealer_hand, player_hand), True)

    def test_if_stand_2_true(self):
        """Check if it returns true with two aces"""
        player_hand = ((0, 0, 2), (0, 0, 2))
        dealer_hand = ((0, 0, 1), (0, 0, 1))
        self.assertEqual(if_stand(dealer_hand, player_hand), True)

    def test_if_stand_lots_cards_true(self):
        """Check if it returns true with a small number composed by many small cards"""
        player_hand = ((0, 0, 2), (0, 0, 2))
        dealer_hand = ((0, 0, 2), (0, 0, 2), (0, 0, 2), (0, 0, 2), (0, 0, 2), (0, 0, 2), (0, 0, 2), (0, 0, 2))
        self.assertEqual(if_stand(dealer_hand, player_hand), True)







# def if_stand(dealer_hand, player_hand):
#    """Function to play second hand, when player decided to stand"""
#    # Sum is already calculated precisely
#    sum_hand = dealer_sum(dealer_hand)
#
#    # Print all dealer's cards
#    print_hand(dealer_hand, dealer_hand, player_hand)
#    print("\n")
#    print(f"The dealer current sum is {sum_hand}.")
#    if sum_hand >= 17:
#       #In this case stand
#       return False
#    else:
#       #In this case hit
#       return True


if __name__ == '__main__':
    unittest.main()

