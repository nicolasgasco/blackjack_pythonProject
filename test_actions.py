from unittest import mock
import unittest
import re
from deck import generate_deck_list
from actions import is_natural, get_username, deal_cards



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


#
# def deal_cards(player_hand, dealer_hand, deck_list):
#    """Function to deal two cards both to the player and the dealer"""
#    for i in range(2):
#    # One random card to the player
#       card_user = random.choice(deck_list)
#       deck_list.remove(card_user)
#       player_hand.append(card_user)
#
#
#       # One random card to the dealer
#       card_dealer = random.choice(deck_list)
#       deck_list.remove(card_dealer)
#       dealer_hand.append(card_dealer)


if __name__ == '__main__':
    unittest.main()

