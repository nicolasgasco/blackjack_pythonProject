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


def generate_deck_dict():
    """Function to generate a full deck of cards in form of a dictionary. Currently not used"""
    list = []
    # This list first to create the dictionary
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
            list.append((suit, number, value))
    dict = {}
    for card in list:
        # Use another function to generate all the keys
        # dict[cardname_from_tuple(list, card)] = card
        suit = card_suits.get(card[0])
        number = card_names.get(card[1])
        dict[f"{number} of {suit}"] = card
    return dict


def generate_deck_list():
    """Function to generate a whole deck of cards as list"""
    list = []
    for num in range(0,4):
        for i in range(1, 14):
            suit = num
            number = i
            value = 0 
            if i == 1:
                # I'm assigning only 1 for now, it will become 11 later
                value = (1)
            elif i > 10:
                value = 10
            else:
                value = i
            list.append((suit, number, value))
    return list


def cardname_from_index(list, index):
	"""Funcion to print a card name when list name and index are known.
	Asks for list name and list index."""
	suit = card_suits.get((list[index])[0])
	number = card_names.get((list[index])[1])
	return f"{number} of {suit}"

def cardname_from_tuple(list, name):
	"""Function to print a card name when only the values are known.
	Asks for list name and card object name."""
	result = cardname_from_index(list, list.index(name))
	return result
	
def print_deck(deck_name):
    """Function to print a whole deck card by card. Mostly used during development."""
    for i in range(len(deck_name)):
        print(cardname_from_index(deck_name, i))