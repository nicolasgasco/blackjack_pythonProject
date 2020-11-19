import random

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

discarted_carts = []

def generate_deck():
	"""Function to generate a whole deck of cards as list"""
	deck_list = []
	for num in range(0,4):
		for i in range(1, 14):
			suit = num
			number = i
			value = 0 
			if i == 1:
				# This used to be a tuple before
				value = (1)
			elif i > 10:
				value = 10
			else:
				value = i
			deck_list.append((suit, number, value))
	return deck_list


def cardname_fromIndex(list, index):
	"""Funcion to print a card name when list name and index are known.
	Asks for list name and list index."""

	suit = card_suits.get((list[index])[0])
	number = card_names.get((list[index])[1])
	return f"{number} of {suit}"
	
def print_deck(deck_name):
	for i in range(0, len(deck_name)):
		cardname_fromIndex(deck_name, i)


def cardname_fromTuple(list, name):
	"""Function to print a card name when only the values are known.
	Asks for list name and card object name."""

	result = cardname_fromIndex(list, list.index(name))
	return result


def remove_randomCard(card_deck, discarted_deck):
	"""Function to remove one random cart from the deck and print it"""

	random_card = random.choice(card_deck)
	card_deck.remove(random_card)
	discarted_deck.append(random_card)
	discarted_name = cardname_fromTuple(discarted_deck, random_card)
	print(discarted_name)


# full_deck = generate_deck()

# print(len(full_deck))

# remove_randomCard(full_deck, discarted_carts)
# remove_randomCard(full_deck, discarted_carts)
# remove_randomCard(full_deck, discarted_carts)

# print(len(full_deck))
