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

# Biggest loop for the actual gaming part
# while True:
# Let's deal cards
first_hand(player_name, player_hand, dealer_hand)

if isNatural(player_hand) and isNatural(dealer_hand):
    print("You both have 21! It's a TIE!")
elif isNatural(player_hand) and not isNatural(dealer_hand):
    print("You have 21. You won!")
elif not isNatural(player_hand) and isNatural(dealer_hand):
    print("The dealer has 21. You lost!")
else:
    pass


##
##
### This loop is for continuing asking for a new card
##loop = True
##while loop == True:
##    # Let's ask if they're standing or hitting
##    round2 = stand_or_hit()
##    
##    #Player chooses to stand
##    if not round2:
##        if_stand()
##        break
##    
##    #Player chooses to hit
##    if round2:
##        if_hit(player_hand)
##        isBlackJack(player_hand)
##
##        # Check if player is bust
##        bust = isBust(player_hand)
##        
##        #if bust
##        if bust:
##            print("Game over.")
##            print("Prepare. A new game will start...\n\n\n")
##            break
##        
##        #if not bust
##        elif not bust:
##            print("The game goes on...")
##            # Loops starts all over again
