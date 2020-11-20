import random
import time
from deck import *
from splash_screen import *


# Full deck and cards that are played
deck_list = generate_deck_list()
deck_dict = generate_deck_dict()
played_cards = [] 
player_hand = []
dealer_hand = []


def ask_name():
   user_name = input("Hi! What's your name? Write it here: ")
   print("\n")
   return user_name

def welcome(user_name):
   print(f"Hi, {user_name.title()}! Welcome to Python Blackjack. This is a simple game,"
    	" but it's a lot of fun. You don't need to place a bet to play.\n")
   print("Let's start...\n")

def first_hand(user_name, hand_cards):
	"""Function to deal the first hand of a Blackjack round.
	Player gets dealt two cards face up, dealer only one face up."""

	for i in range(2):
		# One random card to the player
		card_user = random.choice(deck_list)
		deck_list.remove(card_user)
		player_hand.append(card_user)
		# Adding to played cards just in case it's useful in the future
		played_cards.append(card_user)
		

		# One random card to the dealer
		card_dealer = random.choice(deck_list)
		deck_list.remove(card_dealer)
		dealer_hand.append(card_dealer)
		# Adding to played cards just in case it's useful in the future
		played_cards.append(card_user)

	print("Round One\n")
	print(f"{user_name.title()}, you have been dealt..."
		f" {cardname_fromTuple(player_hand, player_hand[0])} and "
		f"{cardname_fromTuple(player_hand, player_hand[1])}.\n")

	# time.sleep(2)

	print(f"The dealer has one covered card and a "
		f"{cardname_fromTuple(dealer_hand, dealer_hand[0])}.\n")

	isBlackJack(hand_cards)

def stand_or_hit():
   """Function used to prompt the user either to stand or hit"""
    
   user_input = input("You can either [s]tand or [h]it. Please type the corrisponding letter to play: ")
   while user_input != "s" and user_input != "h":
      print("\nPlease insert a valid letter.")
      user_input = input("You can either [s]tand or [h]it. Type your answer: " + "\n")
   if user_input.lower() == "s":
      print("You chose to stand.\n")
      return False
   elif user_input.lower() == "h":
      print("You chose to hit.\n")
      return True

def if_stand():
   """Function to play second hand, when player decided to stand"""

   print(f"Belzebù")

def if_hit():
   """Function to play second hand, when player can either receive another card or stand."""
   card_user = random.choice(deck_list)
   deck_list.remove(card_user)
   player_hand.append(card_user)
   # Just in case I need it in the future
   played_cards.append(card_user)
   print(f"You have received a {cardname_fromTuple(player_hand, player_hand[2])}.\n")
   isBust(player_hand)

##        card_dealer = random.choice(deck_list)
##        deck_list.remove(card_dealer)
##        dealer_hand.append(card_dealer)
##        # Just in case I need it in the future
##        played_cards.append(card_dealer)
##        print(f"The dealer has received a {cardname_fromTuple(dealer_hand, dealer_hand[2])}.\n")

def isBust(hand_cards):
      # First I check if there are some 1s
      total_value = 0
      value_1 = 0
      value_11 = 0
      for suit, number, value in hand_cards:
         # Case 1: there are some aces with double values
         if value == 1:
            # Let's put all the extra values asides
            value_1 += 1
            value_11 += 11
         # Case 2: there are no aces
         else:
            total_value += value

      total_value1 = total_value + value_1
      total_value11 = total_value + value_11
      # This is the regular case, without double values
      if value_1 == 0 and value_11 == 0:
         if total_value > 21:
            print("BUST!")
            print(f"Bust_norm. Your sum is {total_value}! A new game will start...")
         else:
            print(f"Nobust_norm. You're sum is {total_value}. You're not bust!")
      # This is when double values are present
      elif value_1 > 0 and value_11 > 0:
         if total_value11 <= 21:
            print(f"NobustDou1. Your sum is either {total_value1} or {total_value11}.")
         elif (total_value + value_11) > 21:
            print(f"NobusDou2. You're sum is {total_value1}. You're not bust!")

def isBlackJack(hand_cards):
   total_value = 0
   value_1 = 0
   value_11 = 0
   for suit, number, value in hand_cards:
      # Case 1: there are some aces with double values
      if value == 1:
         # Let's put all the extra values asides
         value_1 += 1
         value_11 += 11
      # Case 2: there are no aces
      else:
         total_value += value

   if total_value == 21 or total_value + value_1 == 21 or total_value + value_11 == 21:
      print("Blackjack!")
      if hand_cards == player_hand:
         print(f"Congratulations, you won!")
      elif hand_cards == dealer_hand:
         print(f"Ouch! The dealer won!")
   else:
      return False


# splash_screen()
# time.sleep(2)
# user_name = ask_name()
# welcome_player()
# time.sleep(2)
##
##first_hand()
### # time.sleep(2)  
##stand_or_hit()
##
### ##print(f"Player hand: {player_hand}")
### ##print(f"Length of deck is {len(deck_list)}")
##second_hand()
### ##print(f"Length of deck is {len(deck_list)}")
### ##print(f"Player hand: {player_hand}")
##
##isBust(player_hand)
