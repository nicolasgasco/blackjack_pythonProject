import random
import time
from actions import *
from deck import *
from splash_screen import *


# Used to print the game's logo
splash_screen()

# Let's welcome the player
player_name = welcome()
enter_toContinue()

# Biggest loop for the actual gaming part
big_loop = True
while True:
    # If not declared here, they get summed game after game
    deck_list = generate_deck_list()
    played_cards = [] 
    player_hand = []
    dealer_hand = []
    stand = 0
    hit = 0
    # Let's deal cards
    first_hand(player_name, player_hand, dealer_hand, deck_list)

    if isNatural(player_hand) and isNatural(dealer_hand):
        print("The dealer can show his cards now...")
        print("You both have 21! It's a TIE!")
        big_loop = False
    elif isNatural(player_hand) and not isNatural(dealer_hand):
        print("You have 21. You won!")
        big_loop = False
    elif not isNatural(player_hand) and isNatural(dealer_hand):
        print("The dealer can show his cards now...")
        print("The dealer has 21. You lost!")
        big_loop = False
    else:
        pass

    enter_toContinue()
    # This loop is for continuing asking for a new card
    loop = True
    while loop == True:
        # Let's ask if they're standing or hitting
        round2 = stand_or_hit()
        enter_toContinue()

        #Player chooses to stand
        if not round2:
            print(f"The dealer covered card is {cardname_fromTuple(dealer_hand, dealer_hand[1])}")
            enter_toContinue()
            # Let's check if dealer is standing or hitting
            dealer_loop = True
            while dealer_loop == True:
                dealer_action = if_stand(dealer_hand)

                # Dealer is hitting
                if dealer_action:
                    print("Dealer is hitting")
                    # Dealer receives one more card
                    dealer_card(dealer_hand, deck_list)
                    # Let's check if he's bust
                    dealer_bust = isBust_dealer(dealer_hand)

                    # dealer is bust
                    if dealer_bust:
                        print("The dealer is bust! You won!")
                        print("\n\n\n\n\n\n\n\n\n\n")
                        dealer_loop = False
                        loop = False

                    #dealer is not bust
                    elif not dealer_bust:
                        continue
                        # hit again
            
            # Dealer is standing
                elif not dealer_action:
                    print(f"Dealer is standing.")
                    stand_whoWon(dealer_hand, player_hand)
                    print("\n\n\n\n\n\n\n\n\n\n")
                    dealer_loop = False
                    loop = False
        
        #Player chooses to hit
        if round2:
            if_hit(player_hand, deck_list)
            enter_toContinue()
            
            
            black_jack = isBlackJack(player_hand, player_hand, dealer_hand)
            if black_jack:
                break
                loop == False
            else:
                pass

            # Check if player is bust
            bust = isBust(player_hand)
            
            #if bust
            if bust:
                print("BUST!")
                # SEE IF DEALER TOO BUST OR NOT
                # Let's check if dealer is standing or hitting
                dealer_loop2 = True
                while dealer_loop2 == True:
                    dealer_action = if_stand(dealer_hand)
                    
                    # Dealer is hitting
                    if dealer_action:
                        print("Dealer is hitting")
                        # Dealer receives one more card
                        dealer_card(dealer_hand, deck_list)
                        # Let's check if he's bust
                        dealer_bust = isBust_dealer(dealer_hand)
                        
                        # dealer is bust
                        if dealer_bust:
                            print("BUST! Still, the dealer won!")
                            print("\n\n\n\n\n\n\n\n\n\n")
                            dealer_loop2 = False
                            loop = False

                        #dealer is not bust
                        elif not dealer_bust:
                            print("You're bust and the dealer not. You lost!")
                            print("Game Over!")
                            dealer_loop2 = False
                            loop = False
            
            #if not bust
            elif not bust:
                print("The game goes on...")
                enter_toContinue()
                # Loops starts all over again
