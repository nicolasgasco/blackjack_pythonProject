import random
import time
from actions import *
from deck import *
from splash_screen import *


deck_list = generate_deck_list()
played_cards = [] 
player_hand = []
dealer_hand = []
stand = 0
hit = 0

# Used to print the game's logo
splash_screen()

# Let's welcome the player
player_name = ask_name()

welcome(player_name)

# Let's deal cards
first_hand(player_name, player_hand)
isBlackJack

# Stand or hit after receiving cards?
round2 = stand_or_hit()
if not round2:
    if_stand()
elif round2:
    if_hit()
    # it checks if bust
        if bust:
            game over
        elif not bust:
            another card


