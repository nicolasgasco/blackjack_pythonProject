"""
This is a file to define the classes needed for the Blackjack project
"""

class Deck(list):
	"""Parent class used to describe a whole 52-card deck"""
	def __init__(self, deck_cards = 52, type = "Poker"):
		self.deck_cards = deck_cards
		self.type = type

	def total_deck(self):
		return f"There are {self.deck_cards} cards in the deck"

	

class Suit:
	"""Class used to describe a single suit of a standard 52-card deck"""
	def __init__(self, suit, suit_cards=13):
  		self.suit = suit
  		self.suit_cards = suit_cards
	
	card_suits = {0: "Hearts", 1: "Diamonds", 2: "Clubs", 3: "Spades"}

	def total_suit(self):
		return self.suit_cards


class Card:
	"""Class used to describe a card of a standard 52-card deck"""
	def __init__(self, suit, number, value):
  		self.suit = suit
  		self.numer = number
  		self.value = value

	card_names = {1: "Ass", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 
  					6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
  					11: "Jack", 12: "Queen", 13: "King"}

	def determine_suit(self):
		"""Determines suit of card"""
		return Suit.card_suits.get(self.suit)

	def determine_number(self):
		"""Determines number of card"""		
		return self.card_names.get(self.value) 

	def card_fullname(self):
		"""Returns full card name"""
		return f"{self.determine_number()} of {self.determine_suit()}"

##
##
##
##spade_9 = Card(3, 9, 9)
##print(spade_9.determine_number())
##print(spade_9.determine_suit())
##print(spade_9.card_fullname())
##
##suit_spade = Suit(3)
##print(suit_spade.total_suit())
##
##deck_poker = Deck()
##print(deck_poker.total_deck())
##
##print(deck_poker.total_deck())
##
##spade_allsuit = []


