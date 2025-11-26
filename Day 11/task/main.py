import random
import sys
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def player_hit():
    global hit_me
    new_card = random.choice(cards)
    player_hand.append(new_card)
    global player_score
    player_score= sum(player_hand)
    print(f"Your new card {new_card} is added to your hand: {player_hand} which is {player_score}")
    if player_score > 21:
        hit_me = False
    return player_score, player_hand

def computer_hit():
    new_card = random.choice(cards)
    computer_hand.append(new_card)
    global computer_score
    computer_score= sum(computer_hand)
    print(f"Computer's new card {new_card} is added to hand: {computer_hand} which is {computer_score}")
    if computer_score < 16:
        computer_hit()
    return computer_score, computer_hand

gaming = True
while gaming:
    play_blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_blackjack == 'y':
        hit_me = True
        print(art.logo)
        player_hand = [random.choice(cards), random.choice(cards)]
        player_score = sum(player_hand)
        computer_hand = [random.choice(cards)]
        computer_score = sum(computer_hand) # This needs to be changed from first card
        player_status = f"Your cards: {player_hand}, current score: {player_score}"
        print(player_status)
        computer_status = f"Computer card: {computer_hand}, current score: {computer_score}"
        print(f"Computer's card is: {computer_hand}")
        while hit_me:
            add_player_card = input("type 'y' to get another card, type 'n' to pass: ")
            if add_player_card == 'y':
               player_hit()
               # print(player_hand)
               # print(player_score)
               # if player_score > 21:
               #     hit_me = False
            elif add_player_card == 'n':
                hit_me = False
                print(f"Your score {player_score}")
            else:
                print("Invalid input. Please type 'y' or 'n': ")
        if player_score > 21:
            print(f"Your final hand: {player_hand}, final score: {player_score}. \nComputer's final hand {computer_hand}, final score: {computer_score} \nYou went over. You lose 😭")
        elif computer_score < 16:
            computer_hit()
            print(f"Computer score {computer_score}")
            if computer_score > player_score and computer_score <= 21:
                print('You Lose, Computer Wins! 😞')
            elif computer_score > 21:
                print('Computer Busts!, You Win! 😄')
            elif player_score > computer_score and player_score <= 21:
                print("You Win!!! 😄")
            elif computer_score == player_score:
                print("It's a Draw 😑")

    elif play_blackjack == 'n':
        gaming = False
        sys.exit()
    else:
        print("You have two options, buddy... Please type 'y' or 'n': ")
        gaming = True

# TODO: The Ace can count as 11 or 1.
# TODO: If dealer ends up with a hand smaller than 17, they must take another card.
# TODO: ask player for another card.
