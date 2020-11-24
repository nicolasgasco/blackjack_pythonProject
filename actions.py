import random
import time
from deck import *
spaces = "\n\n\n\n\n"

def welcome():
   user_name = input("Hi! Before we start, write your name here: ")
   while user_name == "" or user_name == " ":
      user_name = input("Please insert a valid name: ")
   user_name = user_name.strip().title()
   print(spaces)
   print(f"\nHi, {user_name}! Welcome to Python Blackjack. This is a simple game,"
         " but it's a lot of fun. You don't need to place a bet to play.")
   return user_name

def enter_toContinue():
   """This is used in place of 'Press any key to continue'"""
   input("Press Enter to continue... ")
   print(spaces)

def first_hand(user_name, player_hand, dealer_hand, deck_list):
   """Function to deal the first hand of a Blackjack round.
   Player gets dealt two cards face up, dealer only one face up."""

   for i in range(2):
   # One random card to the player
      card_user = random.choice(deck_list)
      deck_list.remove(card_user)
      player_hand.append(card_user)


      # One random card to the dealer
      card_dealer = random.choice(deck_list)
      deck_list.remove(card_dealer)
      dealer_hand.append(card_dealer)

   print("Let's start a new game of Python Blackjack.")
   enter_toContinue()

   print(f"{user_name.title()}, you have been dealt..."
   f" {cardname_fromTuple(player_hand, player_hand[0])} and "
   f"{cardname_fromTuple(player_hand, player_hand[1])}.")
   enter_toContinue()

   if isNatural(player_hand):
      print(f"You have 21! Let's see what the dealer has...")
      enter_toContinue()

   print(f"The dealer has one covered card and a "
   f"{cardname_fromTuple(dealer_hand, dealer_hand[0])}.")


def isNatural(card_hand):
    """Function to check if two first cards are a natural (10 plus ace)"""
    if (card_hand[0])[2] == 1 and (card_hand[1])[2] == 10:
        return True
    elif (card_hand[0])[2] == 10 and (card_hand[1])[2] == 1:
        return True
    else:
        return False


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

   # 11 always takes precedence
   # If there is only one ace
   if sum11 == 11:
      if sum_hand + sum11 > 21:
         sum_hand += sum1
      else:
         sum_hand += sum11
      
   # If there are are two aces
   elif sum11 == 22:
      if sum_hand + 11 > 21:
         sum_hand += sum1
      else:
         sum_hand += 11
         sum_hand += 1
      
   # If there are three aces
   elif sum11 == 33:
      if sum_hand + 11 > 21:
         sum_hand += sum1
      else:
         sum_hand += 11
         sum_hand += 2
      
   # If there are four aces
   elif sum11 == 44:
      if sum_hand + 11 > 21:
         sum_hand += sum1
      else:
         sum_hand += 11
         sum_hand += 3

   return sum_hand

def game_over():
   """Simple function to make changing the Game Over text easy"""
   print("GAME OVER!")
   enter_toContinue()
   
def if_stand(dealer_hand):
   """Function to play second hand, when player decided to stand"""
   # Sum is already calculated precisely
   sum_hand = dealer_sum(dealer_hand)

   cards = [cardname_fromTuple(dealer_hand, card) for card in dealer_hand]
   print(f"The dealer's cards are:")
   for card in cards:
      print(f"\t{card}")
   print("\n")
   print(f"The dealer current sum is {sum_hand}.") 
   if sum_hand >= 17:
      #In this case stand
      return False
   else:
      #In this case hit
      return True


def stand_whoWon (dealer_hand, player_hand):
   """Function to determine who won when both the dealer and the player are standing (two cards)"""
   sum_dealer = 0
   for card in dealer_hand:
      # 11 has precedence over 1 when the dealer plays
      if card[2] == 1:
         sum_dealer += 11
      else:
         sum_dealer += card[2]
   if sum_dealer > 21:
      sum_dealer -= 10
   else:
      pass

   sum_player = 0
   for card in player_hand:
      if card[2] == 1:
         # In this case ace must be 11 because player has only two cards
         sum_player += 11
      else:
         sum_player += card[2]
         
  #CHANGE SUM TO INCLUDE 1       
   if sum_player > sum_dealer:
      print(f"Your cards ({sum_player}) are higher than the dealer's ({sum_dealer}). Congratulations, YOU WON!")
   elif sum_player == sum_dealer:
      print(f"You and the dealer have the same total value ({sum_player}). IT'S A TIE!")
   elif sum_player < sum_dealer:
      print(f"Your cards ({sum_player}) are lower than the dealer's ({sum_dealer}). YOU LOST!")

def dealer_card(dealer_hand, deck_list):
   """Function to give one random card to the dealer"""
   # One random card to the dealer
   card_dealer = random.choice(deck_list)
   deck_list.remove(card_dealer)
   dealer_hand.append(card_dealer)
   return card_dealer


def isBust_dealer(dealer_hand):
   """"Function to determine if dealer is bust with current hand"""
   # Sum is already calculed precisely
   sum = dealer_sum(dealer_hand)

   if sum > 21:
      return True
   else:
      return False
   

def if_hit(player_hand, deck_list):
   """Function to play second hand, when player can either receive another card or stand."""
   card_user = random.choice(deck_list)
   deck_list.remove(card_user)
   player_hand.append(card_user)
##   # Just in case I need it in the future
##   played_cards.append(card_user)
   print(f"You have received a {cardname_fromTuple(player_hand, player_hand[-1])}.")


def isBust(hand_cards):
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
      

def isBlackJack(hand_cards, player_hand, dealer_hand):
   """Function to see if the hand of the makes a Blackjack"""
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
         print(spaces)
         return True
      elif hand_cards == dealer_hand:
         print(f"Ouch! The dealer won!")
         print("GAME OVER!")
         print(spaces)
         return True
   else:
      return False

      
      
      

