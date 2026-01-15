from art import logo
from art import vs
import game_data
import random
print(logo)
USERSCORE = 0
selectionFirst = random.choice(game_data.data)
game_data.data.remove(selectionFirst)
selectionSecond = random.choice(game_data.data)
game_data.data.remove(selectionSecond) # Two choices are randomly selected and removed from the dictionary


# TODO Create a function that compares the follower_count of the two choices.
def compare(selection):
    print(selectionFirst['name'], selectionFirst['follower_count']) #This is for checking it's mathing correctly
    print(selectionSecond['name'], selectionSecond['follower_count'])
    if selection == "A":
        if selectionFirst['follower_count'] > selectionSecond['follower_count']:
            USERSCORE += 1
            print("You win!")
            print(f"Your score is: {USERSCORE}")
        else:
            print("You lose!")
            print(f"Your score is: {USERSCORE}")
    elif selection == "B":
        if selectionSecond['follower_count'] > selectionFirst['follower_count']:
            print("You Win!")
            USERSCORE += 1
            print(f"Your score is: {USERSCORE}")
        else:
            print("You Lose!")
            print(f"Your score is: {USERSCORE}")


# TODO the it asks "A, Name, Description and Country of Origin"
print(f"Compare A: {selectionFirst['name']}, a {selectionFirst['description']}, from {selectionFirst['country']}.")


print(vs) # This prints the vs sign between the two options
print(f"Against B: {selectionSecond['name']}, a {selectionSecond['description']}, from {selectionSecond['country']}.")
# TODO It asks to select A or B.
compare(input("Who has more follower_count? Type 'A' or 'B': ").upper())
# if userGuess == 'A':

# TODO When answered correctly, that selection becomes "A" and the B is a new choice.
# TODO losing will give you the art and below saying "Sorry, that's wrong. Final score: X" with "x" being how far you got (2 or whatever)