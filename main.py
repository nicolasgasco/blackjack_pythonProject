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
    enter_toContinue()

    if isNatural(player_hand) and isNatural(dealer_hand):
        print(f"The dealer covered card is {cardname_fromTuple(dealer_hand, dealer_hand[1])}.")
        print("Both you and the dealer have 21! IT'S A TIE!")
        enter_toContinue()
        game_over()
        loop = False
        
    elif isNatural(player_hand) and not isNatural(dealer_hand):
        print(f"The dealer covered card is {cardname_fromTuple(dealer_hand, dealer_hand[1])}.")
        print("You have 21 and the dealer not. YOU WON!")
        enter_toContinue()
        game_over()
        loop = False
        
    elif not isNatural(player_hand) and isNatural(dealer_hand):
        print(f"The dealer covered card is {cardname_fromTuple(dealer_hand, dealer_hand[1])}. The dealer's sum is 21...")
        print("Your sum is lower. YOU LOST!")
        enter_toContinue()
        game_over()
        loop = False
    else:
        loop = True

    # This loop is for continuing asking for a new card
    while loop == True:
        # Let's ask if they're standing or hitting
        round2 = stand_or_hit()
        enter_toContinue()

        #Player chooses to stand
        if not round2:
            print(f"The dealer covered card is {cardname_fromTuple(dealer_hand, dealer_hand[1])}.")
            enter_toContinue()
            # Let's check if dealer is standing or hitting
            dealer_loop = True
            while dealer_loop == True:
                dealer_action = if_stand(dealer_hand)
                enter_toContinue()

                # Dealer is hitting
                if dealer_action:
                    print("The dealer is hitting and will receive another card.")
                    enter_toContinue()
                    
                    # Dealer receives one more card
                    new_card = dealer_card(dealer_hand, deck_list)
                    print(f"The dealer received {cardname_fromTuple(dealer_hand, new_card)}.")
                    enter_toContinue()
                    
                    # Let's check if he's bust
                    dealer_bust = isBust_dealer(dealer_hand)

                    # dealer is bust
                    if dealer_bust:
                        print(f"The dealer's is bust! ({dealer_sum(dealer_hand)}) You WON!")
                        enter_toContinue()
                        
                        game_over()
                        
                        dealer_loop = False
                        loop = False

                    #dealer is not bust
                    elif not dealer_bust:
                        continue
                        # hit again
            
            # Dealer is standing
                elif not dealer_action:
                    print(f"Dealer is standing and won't receive another card.")
                    enter_toContinue()
                    
                    stand_whoWon(dealer_hand, player_hand)
                    enter_toContinue()
                    
                    game_over()
                    
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
            enter_toContinue()
            
            #if bust
            if bust:
                # SEE IF DEALER TOO BUST OR NOT
                # Let's check if dealer is standing or hitting
                dealer_loop2 = True
                while dealer_loop2 == True:
                    dealer_action = if_stand(dealer_hand)
                    enter_toContinue()

                    # Dealer is hitting
                    if dealer_action:
                        print("The dealer is hitting and will receive another card.")
                        enter_toContinue()
                        
                        # Dealer receives one more card
                        new_card = dealer_card(dealer_hand, deck_list)
                        print(f"The dealer received {cardname_fromTuple(dealer_hand, new_card)}.")
                        enter_toContinue()
                        
                        # Let's check if he's bust
                        dealer_bust = isBust_dealer(dealer_hand)

                        # dealer is bust
                        if dealer_bust:
                            print(f"The dealer's is bust! ({dealer_sum(dealer_hand)}) You still LOSE!")
                            enter_toContinue()
                            
                            game_over()
                            
                            loop = False
                            dealer_loop2 = False

                        #dealer is not bust
                        elif not dealer_bust:
                            continue
                            # hit again
                
                # Dealer is standing
                    elif not dealer_action:
                        print(f"Dealer is standing and won't receive another card.")
                        enter_toContinue()
                        
                        print("You're bust and the dealer not. You lost!")
                        enter_toContinue()
                        
                        game_over()
                        loop = False
                        dealer_loop2 = False
                    
            
            #if not bust
            elif not bust:
                print("The game goes on...")
                enter_toContinue()
                # Loops starts all over again
