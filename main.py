import random
import time

from deck import generate_deck_list, cardname_from_index, cardname_from_tuple
from actions import welcome, enter_to_continue, is_natural, deal_cards, print_first_hand, stand_or_hit
from actions import dealer_card, is_bust_dealer, stand_who_won, if_hit, dealer_sum, print_hand, is_bust_player, game_over
from splash_screen import splash_screen


# Used to print the game's logo
splash_screen()

# Let's welcome the player
player_name = welcome()
enter_to_continue()

# Biggest loop for the actual gaming part
while True:
    # If not declared here, they get summed game after game
    deck_list = generate_deck_list()
    played_cards = [] 
    player_hand = []
    dealer_hand = []


    print("Let's start a new game of Python Blackjack.")
    enter_to_continue()

    # FIRST HAND
    deal_cards(player_hand, dealer_hand, deck_list)
    print_first_hand(player_name, player_hand, dealer_hand)
    enter_to_continue()

    if is_natural(player_hand) and is_natural(dealer_hand):
        print(f"The dealer covered card is {cardname_fromTuple(dealer_hand, dealer_hand[1])}.")
        print("Both you and the dealer have 21! IT'S A TIE!")
        enter_to_continue()
        game_over()
        loop = False
        
    elif is_natural(player_hand) and not is_natural(dealer_hand):
        print(f"The dealer covered card is {cardname_fromTuple(dealer_hand, dealer_hand[1])}.")
        print("You have 21 and the dealer not. YOU WON!")
        enter_to_continue()
        game_over()
        loop = False
        
    elif not is_natural(player_hand) and is_natural(dealer_hand):
        print(f"The dealer covered card is {cardname_fromTuple(dealer_hand, dealer_hand[1])}. The dealer's sum is 21...")
        print("Your sum is lower. YOU LOST!")
        enter_to_continue()
        game_over()
        loop = False
    else:
        loop = True

    # HIT OR STAND LOOP
    while loop == True:
        # Let's ask if they're standing or hitting
        round2 = stand_or_hit()
        enter_to_continue()

        # PLAYER STANDS
        if not round2:
            print(f"The dealer covered card is {cardname_fromTuple(dealer_hand, dealer_hand[1])}.")
            enter_to_continue()
            # Let's check if dealer is standing or hitting
            dealer_loop = True
            while dealer_loop == True:
                dealer_action = if_stand(dealer_hand, player_hand)
                enter_to_continue()

                # DEALER HITS
                if dealer_action:
                    print("The dealer is hitting and will receive another card.")
                    enter_to_continue()
                    
                    # Dealer receives one more card
                    new_card = dealer_card(dealer_hand, deck_list)
                    print(f"The dealer received {cardname_fromTuple(dealer_hand, new_card)}.")
                    enter_to_continue()
                    
                    # Let's check if he's bust
                    dealer_bust = is_bust_dealer(dealer_hand)

                    # dealer is bust
                    if dealer_bust:
                        print(f"The dealer's is bust! ({dealer_sum(dealer_hand)}) You WON!")
                        enter_to_continue()
                        
                        game_over()
                        
                        dealer_loop = False
                        loop = False

                    #dealer is not bust
                    elif not dealer_bust:
                        continue
                        # hit again
            
            # DEALER STANDS
                elif not dealer_action:
                    print(f"Dealer is standing and won't receive another card.")
                    enter_to_continue()
                    
                    stand_who_won(dealer_hand, player_hand)
                    enter_to_continue()
                    
                    game_over()
                    
                    dealer_loop = False
                    loop = False
        
        #PLAYER HITS
        if round2:
            if_hit(player_hand, deck_list)
            enter_to_continue()
            
##            # I HAVE TO CHANGE THIS
##            black_jack = is_21(player_hand, player_hand, dealer_hand)
##            if black_jack:
##                enter_to_continue()
##                continue
##            else:
##                pass

            # Check if player is bust
            bust = is_bust_player(player_hand, player_hand, dealer_hand)
            enter_to_continue()
            
            # PLAYER BUST
            if bust:
                # SEE IF DEALER TOO BUST OR NOT
                # Let's check if dealer is standing or hitting
                dealer_loop2 = True
                while dealer_loop2 == True:
                    dealer_action = if_stand(dealer_hand, player_hand)
                    enter_to_continue()

                    # Dealer is hitting
                    if dealer_action:
                        print("The dealer is hitting and will receive another card.")
                        enter_to_continue()
                        
                        # Dealer receives one more card
                        new_card = dealer_card(dealer_hand, deck_list)
                        print(f"The dealer received {cardname_fromTuple(dealer_hand, new_card)}.")
                        enter_to_continue()
                        
                        # Let's check if he's bust
                        dealer_bust = is_bust_dealer(dealer_hand)

                        # dealer is bust
                        if dealer_bust:
                            print(f"The dealer's is bust! ({dealer_sum(dealer_hand)}) You still LOSE!")
                            enter_to_continue()
                            
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
                        enter_to_continue()
                        
                        print("You're bust and the dealer not. You lost!")
                        enter_to_continue()
                        
                        game_over()
                        loop = False
                        dealer_loop2 = False
                    
            
            # PLAYER NOT BUST
            elif not bust:
                # print("The game goes on...")
                # enter_to_continue()
                pass
                # Loops starts all over again
