import random
import sys
import art

user_cards = []
computer_cards = []

def deal_card(hand):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hand = random.choice(cards)
    print(hand)
    return hand

def calculate_score(hand):
    calculation = sum(hand)
    if 11 and 1 in hand:
        print(hand)
        print("BLACKJACK IN CALCULATION")
        sys.exit(0)
    elif 11 in hand and calculation > 21:
        hand.remove(11)
        hand.append(1)
        calculation = sum(hand)
    return calculation

def compare(u_score, p_score):

# def play_game():