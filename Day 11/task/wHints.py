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

def play_game():




gaming = True
while gaming:
    to_game = input("Would you like to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if to_game == 'n':
        gaming = False
        sys.exit()
    elif to_game == 'y':
        print("\n" * 30)
        print(art.logo)
        user_cards = deal_cards()
        computer_cards = deal_cards()
        player_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        if player_score == 21:
            print('Blackjack! You won!')
        elif computer_score == 21:
            print('You Lose! Computer won!')
        elif  player_score > 21:
            if 11 in user_cards:
                user_cards.remove(11)
                user_cards.append(1)
                player_score = calculate_score(user_cards)
                print(f'Your modified Ace score: {player_score}')
                if player_score > 21:
                    print("You went over, you lose!")
                else:
                    add_player_card = input("type 'y' to get another card, type 'n' to pass: ")
                    if add_player_card == 'y':
                        deal_card(user_cards)
                        print(f"player hand now: {user_cards}")
                        if computer_score < 17:
                            computer_cards.append(random.choice(cards))
                            computer_score = calculate_score(computer_cards)
                            print(computer_cards)
                            print(computer_score)
                            if computer_score < 17:
                                deal_card(computer_cards)
                        else:
                            continue
                    elif add_player_card == 'n':
                        if computer_score < 17:
                            computer_cards.append(random.choice(cards))
                            computer_score = calculate_score(computer_cards)
                            if computer_score < 17:
                                deal_card(computer_cards)
            else:
                print('You went over! You lose, Computer wins!')
        elif player_score < 21:
            hit_me = True
        elif computer_score > 21:
            if 11 in computer_cards:
                computer_cards.remove(11)
                computer_cards.append(1)
                computer_score = calculate_score(computer_cards)
                if computer_score < 17:
                        deal_card(computer_cards)
            else:
                print('Computer went over! Computer Loses, You win!')
        print(f"player's hand: {user_cards}")
        print(f"player's score: {player_score}")
        hit_me = True
        while hit_me:
            add_player_card = input("type 'y' to get another card, type 'n' to pass: ")
            if add_player_card == 'y':
                deal_card(user_cards)
                player_score = calculate_score(user_cards)
                print(user_cards)
                print(player_score)
                if player_score < 21:
                    hit_me = True
                elif player_score > 21:
                    print("You went over, you lose!")
                else:
                    hit_me = False
            elif add_player_card == 'n':
                hit_me = False
                computer_check = True
                while computer_check:
                    if computer_score < 17:
                        deal_card(computer_cards)
                        computer_score = calculate_score(computer_cards)
                    else:
                        computer_check = False
        if computer_score > 21:
            print(f'Player hand {user_cards} and Computer hand {computer_cards}')
            print(f'Player score: {player_score} and Computer score: {computer_score}')
            print("Computer went over! Computer Loses, You win!")
        elif player_score > 21:
            print(f'Player hand {user_cards} and Computer hand {computer_cards}')
            print(f'Player score: {player_score} and Computer score: {computer_score}')
            print("You went over! You lose!")
        elif player_score > computer_score:
            print(f'Player hand {user_cards} and Computer hand {computer_cards}')
            print(f'Player score: {player_score} and Computer score: {computer_score}')
            print("Player wins!")
        elif player_score < computer_score:
            print(f'Player hand: {user_cards} and Computer hand {computer_cards}')
            print(f'Player score: {player_score} and Computer score: {computer_score}')
            print("Computer wins!")
        elif player_score == computer_score:
            print(f'Player hand {user_cards} and Computer hand {computer_cards}')
            print(f'Player score: {player_score} and Computer score: {computer_score}')
            print("It's a draw!")