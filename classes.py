import random
from deck import *

class Deck(List):
    """Parent class used to describe a whole 52-card deck"""
    def __init__(self):
        super().__init__()
        self.total_cards = 52
        self.card_names = {
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
        
        self.card_suits = {
            0: "Hearts",
            1: "Diamonds",
            2: "Clubs",
            3: "Spades"
            }
        self.list = generate_deck_list()

    def total_deck(self):
        print(f"There are {self.total_cards} cards in the deck")

    def generate_deck_list(self):
        """Function to generate a whole deck of cards in form of list"""
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

    def cardname_fromIndex(self, index):
        """Funcion to print a card name when list name and index are known.
        Asks for list name and list index."""
        suit = card_suits.get((list[index])[0])
        number = card_names.get((list[index])[1])
        return f"{number} of {suit}"

    def cardname_fromTuple(list, name):
        """Function to print a card name when only the values are known.
        Asks for list name and card object name."""
        result = cardname_fromIndex(list, list.index(name))
        return result

    def print_deck(self, deck_name):
        """Function to print a whole deck card by card. Mostly used during development."""
        for i in range(len(deck_name)):
            cardname_fromIndex(deck_name, i)

deck = Deck()
print(deck(type))

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


