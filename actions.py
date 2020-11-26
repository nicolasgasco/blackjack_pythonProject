import random
import time
import re
from deck import *

# This is global in case I need to change it quickly
spaces = "\n\n\n\n\n"

def welcome():
   """Function used to welcome player and get their name"""
   user_name = input("Hi! Before we start, write your name here: ")
   pattern = re.compile(r"^[^a-zA-z]*$")
   while pattern.match(user_name):
      user_name = input("\nPlease insert a valid name: ")
   user_name = user_name.strip().title()
   
   print(spaces)
   print(f"\nHi, {user_name}! Welcome to Python Blackjack. This is a simple game,"
         " but it's a lot of fun. You don't need to place a bet to play.")
   return user_name


def enter_to_continue():
   """This is used in place of 'Press any key to continue'"""
   input("Press Enter to continue... ")
   print(spaces)


def is_natural(card_hand):
    """Function to check if two first cards are a natural (10 plus ace)"""
    if (card_hand[0])[2] + (card_hand[1])[2] == 11:
        return True
    else:
        return False

def deal_cards(player_hand, dealer_hand, deck_list):
   """Function to deal two cards both to the player and the dealer"""
   for i in range(2):
   # One random card to the player
      card_user = random.choice(deck_list)
      deck_list.remove(card_user)
      player_hand.append(card_user)


      # One random card to the dealer
      card_dealer = random.choice(deck_list)
      deck_list.remove(card_dealer)
      dealer_hand.append(card_dealer)


def print_first_hand(user_name, player_hand, dealer_hand):
   """Function to print the first hand dealt in the game"""
   
   print(f"{user_name.title()}, you have been dealt..."
   f" {cardname_fromTuple(player_hand, player_hand[0])} and "
   f"{cardname_fromTuple(player_hand, player_hand[1])}.")
   enter_toContinue()

   if isNatural(player_hand):
      print(f"You have 21! Let's see what the dealer has...")
      enter_toContinue()

   print(f"The dealer has one covered card and a "
   f"{cardname_fromTuple(dealer_hand, dealer_hand[0])}.")


def stand_or_hit():
   """Function used to prompt the user either to stand or hit"""
    
   user_input = input("You can either [s]tand or [h]it. Please type the corresponding letter to play: ")
   while user_input != "s" and user_input != "h":
      print(spaces)
      print("\nPlease insert a valid letter.")
      user_input = input("You can either [s]tand or [h]it. Type your answer: ")
      
   if user_input.lower() == "s":
      print(spaces)
      print("You chose to stand.")
      
      return False
   elif user_input.lower() == "h":
      print(spaces)
      print("You chose to hit.")
      return True


def if_stand(dealer_hand, player_hand):
   """Function to play second hand, when player decided to stand"""
   # Sum is already calculated precisely
   sum_hand = dealer_sum(dealer_hand)

   # Print all dealer's cards
   print_hand(dealer_hand, dealer_hand, player_hand)
   print("\n")
   print(f"The dealer current sum is {sum_hand}.") 
   if sum_hand >= 17:
      #In this case stand
      return False
   else:
      #In this case hit
      return True


def dealer_card(dealer_hand, deck_list):
   """Function to give one random card to the dealer"""
   # One random card to the dealer
   card_dealer = random.choice(deck_list)
   deck_list.remove(card_dealer)
   dealer_hand.append(card_dealer)
   return card_dealer


def is_bust_dealer(dealer_hand):
   """"Function to determine if dealer is bust with current hand"""
   # Sum is already calculed precisely
   sum = dealer_sum(dealer_hand)

   if sum > 21:
      return True
   else:
      return False


def stand_who_won (dealer_hand, player_hand):
   """Function to determine who won when both the dealer and the player are standing (two cards)"""
   sum_dealer = dealer_sum(dealer_hand)

   sum_player = dealer_sum(player_hand)
         
  #CHANGE SUM TO INCLUDE 1       
   if sum_player > sum_dealer:
      print(f"Your cards ({sum_player}) are higher than the dealer's ({sum_dealer}). Congratulations, YOU WON!")
   elif sum_player == sum_dealer:
      print(f"You and the dealer have the same total value ({sum_player}). IT'S A TIE!")
   elif sum_player < sum_dealer:
      print(f"Your cards ({sum_player}) are lower than the dealer's ({sum_dealer}). YOU LOST!")



def if_hit(player_hand, deck_list):
   """Function to play second hand, when player can either receive another card or stand."""
   card_user = random.choice(deck_list)
   deck_list.remove(card_user)
   player_hand.append(card_user)
   print(f"You have received a {cardname_fromTuple(player_hand, player_hand[-1])}.")


def dealer_sum(dealer_hand):
   """Function to calculate the dealer's sum applying special rules"""
   sum_hand = 0
   sum11 = 0
   sum1 = 0
   for card in dealer_hand:
         if card[2] == 1:
            sum11 += 11
            sum1 += 1
         else:
            sum_hand += card[2]

   # Here we'll include each case from one ace in the hand to four ( sum 11 == 11/22/33/44)
   i = 0
   for num in range(11, 45, 11):
      if sum11 == num:
         if sum_hand + 11 + i > 21:
            sum_hand += sum1
         else:
            sum_hand += 11
            sum_hand += i
      i += 1

   return sum_hand


def print_hand(hand_cards, dealer_hand, player_hand):
   """Function used to print the current hand, both player's and dealer's"""
   
   actor = ""
   if hand_cards == dealer_hand:
      actor = "dealer"
   elif hand_cards == player_hand:
      actor = "player"
   else:
      actor = "current user"
      
   cards = [cardname_fromTuple(hand_cards, card) for card in hand_cards]
   
   print(f"The {actor}'s cards are:")
   for card in cards:
      print(f"\t{card}")


def is_bust_player(hand_cards, player_hand, dealer_hand):
   """Function to check if the current hand exceeds the value of 21"""
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
         
   # Print the player's hand
   print_hand(hand_cards, dealer_hand, player_hand)
   print("\n")
   
   total_value1 = total_value + value_1
   total_value11 = total_value + value_11
   # This is the regular case, without double values
   if value_1 == 0 and value_11 == 0:
      if total_value > 21:
         print(f"With the new card, your sum is {total_value}.")
         print("BUST!")
         return True
      else:
         print(f"With the new card, you're sum is {total_value}.")
         return False

   # This is when double values are present
   elif value_1 > 0 and value_11 > 0:
      if total_value11 <= 21:
         print(f"With the new card, your sum is either {total_value1} or {total_value11}.")
         return False
      elif total_value11 > 21 and total_value1 > 21:
         print(f"With the new card, your sum is {total_value1}.")
         print("BUST!")
         return True
      elif total_value11 > 21 and total_value1 < 21:
         print(f"With the new card, your sum is {total_value1}.")
         return False


##def is_21(hand_cards, player_hand, dealer_hand):
##   """Function to see if the hand of the makes a Blackjack"""
##   total_value = 0
##   value_1 = 0
##   value_11 = 0
##   for suit, number, value in hand_cards:
##      # Case 1: there are some aces with double values
##      if value == 1:
##         # Let's put all the extra values asides
##         value_1 += 1
##         value_11 += 11
##      # Case 2: there are no aces
##      else:
##         total_value += value
##
##   if total_value == 21 or total_value + value_1 == 21 or total_value + value_11 == 21:
##      if hand_cards == player_hand:
##         print("Your sum is 21!")
##         return True
##      
##      elif hand_cards == dealer_hand:
##         print("The dealer's sum is 21!")
##         return True
##      
##      else:
##         return False


def game_over():
   """Simple function to make changing the Game Over text easily"""
   print("GAME OVER!")
   enter_toContinue()
      
      
      

