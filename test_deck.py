import unittest
from deck import cardname_from_index, cardname_from_tuple, generate_deck_list

deck_test = generate_deck_list()
card_names = {
	1: "Ace",
	2: "Two",
	3: "Three",
	4: "Four",
	5: "Five",
	6: "Six",
	7: "Seven",
	8: "Eight",
	9: "Nine",
	10: "Ten",
	11: "Jack",
	12: "Queen",
	13: "King"
	}

card_suits = {
	0: "Hearts",
	1: "Diamonds",
	2: "Clubs",
	3: "Spades"
	}

class TestCardNameFromIndex(unittest.TestCase):
    """Test for cardname_from_index. I'm testing for first and last card of every suit"""

    def test_card_name_from_index_first_of_hearts(self):
        cardname = cardname_from_index(deck_test, 0)
        self.assertEqual(cardname, "Ace of Hearts")

    def test_card_name_from_index_last_of_hearts(self):
        cardname = cardname_from_index(deck_test, 12)
        self.assertEqual(cardname, "King of Hearts")

    def test_card_name_from_index_first_of_diamonds(self):
        cardname = cardname_from_index(deck_test, 13)
        self.assertEqual(cardname, "Ace of Diamonds")

    def test_card_name_from_index_last_of_diamonds(self):
        cardname = cardname_from_index(deck_test, 25)
        self.assertEqual(cardname, "King of Diamonds")

    def test_card_name_from_index_first_of_clubs(self):
        cardname = cardname_from_index(deck_test, 26)
        self.assertEqual(cardname, "Ace of Clubs")

    def test_card_name_from_index_last_of_clubs(self):
        cardname = cardname_from_index(deck_test, 38)
        self.assertEqual(cardname, "King of Clubs")

    def test_card_name_from_index_first_of_spades(self):
        cardname = cardname_from_index(deck_test, 39)
        self.assertEqual(cardname, "Ace of Spades")

    def test_card_name_from_index_last_of_spades(self):
        cardname = cardname_from_index(deck_test, 51)
        self.assertEqual(cardname, "King of Spades")

    def test_card_name_from_index_last_of_deck(self):
        cardname = cardname_from_index(deck_test, -1)
        self.assertEqual(cardname, "King of Spades")


class TestCardNameFromIndex(unittest.TestCase):
    """Test for cardname_from_tuple. I'm testing for first and last card of every suit"""

    def test_card_name_from_tuple_first_hearts(self):
        cardname = cardname_from_tuple(deck_test, (0, 1, 1))
        self.assertEqual(cardname, "Ace of Hearts")

    def test_card_name_from_tuple_last_hearts(self):
        cardname = cardname_from_tuple(deck_test, (0, 13, 10))
        self.assertEqual(cardname, "King of Hearts")

    def test_card_name_from_tuple_first_diamonds(self):
        cardname = cardname_from_tuple(deck_test, (1, 1, 1))
        self.assertEqual(cardname, "Ace of Diamonds")

    def test_card_name_from_tuple_last_diamonds(self):
        cardname = cardname_from_tuple(deck_test, (1, 13, 10))
        self.assertEqual(cardname, "King of Diamonds")

    def test_card_name_from_tuple_first_clubs(self):
        cardname = cardname_from_tuple(deck_test, (2, 1, 1))
        self.assertEqual(cardname, "Ace of Clubs")

    def test_card_name_from_tuple_last_clubs(self):
        cardname = cardname_from_tuple(deck_test, (2, 13, 10))
        self.assertEqual(cardname, "King of Clubs")

    def test_card_name_from_tuple_first_spades(self):
        cardname = cardname_from_tuple(deck_test, (3, 1, 1))
        self.assertEqual(cardname, "Ace of Spades")

    def test_card_name_from_tuple_last_spades(self):
        cardname = cardname_from_tuple(deck_test, (3, 13, 10))
        self.assertEqual(cardname, "King of Spades")

if __name__ == '__main__':
    unittest.main()

