import random
import sys
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #TODO Notice "1" is not listed here

def calculate_score():
    new_card = random.choice(cards)
    player_cards.append(new_card)
    global player_sum
    player_sum= sum(player_cards)
    return player_sum, player_cards
gaming = True
while gaming:
    play_blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_blackjack == 'y':
        hit_me = True
        print(art.logo)
        player_cards = [random.choice(cards), random.choice(cards)]
        player_sum = sum(player_cards)
        computer_first_card = [random.choice(cards)]
        computer_score = sum(computer_first_card) # This needs to be changed from first card
        player_status = f"Your cards: {player_cards}, current score: {player_sum}"
        print(player_status)
        print(f"Computer's first card: {computer_first_card}")
        while hit_me:
            add_player_card = input("type 'y' to get another card, type 'n' to pass: ")
            if add_player_card == 'y':
               calculate_score()
               print(player_cards)
               print(player_sum)
               if player_sum > 21:
                   hit_me = False
                   print(f"Your final hand: {player_cards}, final score: {player_sum}. \nComputer's final hand {computer_first_card}, final score: {computer_score} \nYou went over. You lose 😭")

            elif add_player_card == 'n':
                hit_me = False
                # TODO: Input what should happen after you settle with your cards - The computer needs to hit or stand
                # TODO: And start doing the calculations and comparisons
            else:
                print("Invalid input. Please type 'y' or 'n': ")


    elif play_blackjack == 'n':
        gaming = False
        sys.exit()
    else:
        print("You have two options, buddy... Please type 'y' or 'n': ")
        gaming = True

# TODO: The Ace can count as 11 or 1.
# TODO: If dealer ends up with a hand smaller than 17, they must take another card.
# TODO: ask player for another card.
