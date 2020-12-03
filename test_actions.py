import unittest
import re
from actions import is_natural


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


class TestingDealCards(unittest.TestCase):
    """Test to check if the function deals two cards to the player and the dealer"""






def deal_cards(player_hand, dealer_hand, deck_list):
   """Function to deal two cards both to the player and the dealer"""
   for i in range(2):
   # One random card to the player
      card_user = random.choice(deck_list)
      deck_list.remove(card_user)
      player_hand.append(card_user)


      # One random card to the dealer
      card_dealer = random.choice(deck_list)
      deck_list.remove(card_dealer)
      dealer_hand.append(card_dealer)

if __name__ == '__main__':
    unittest.main()

