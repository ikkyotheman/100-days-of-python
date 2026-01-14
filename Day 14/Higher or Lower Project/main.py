from art import logo
from art import vs
import game_data
import random
print(logo)
# Here we select the two people
# TODO need to make it so once a choice is selected from the pool, it can't be selected again (A and B were cardi B)
selectionFirst = random.choice(game_data.data)
game_data.data.remove(selectionFirst)
selectionSecond = random.choice(game_data.data)
game_data.data.remove(selectionSecond)
print(selectionFirst)
print(selectionSecond)
print(game_data.data) # This shows that the selections have been removed.

# TODO Create a function that compares the followers of the two choices.
def compare(selectionFirst, ):
#     if selectionFirst['followers'] > selectionSecond['followers']:
#
# # TODO the it asks "A, Name, Description and Country of Origin"
# print(f"Compare A: {selectionFirst['name']}, a {selectionFirst['description']}, from {selectionFirst['country']}.")
#

#
# # TODO between A and B there is a large "VS." logo
# print(vs)
# print(f"Against B: {selectionSecond['name']}, a {selectionSecond['description']}, from {selectionSecond['country']}.")
# # TODO It asks to select A or B.
# userGuess = input("Who has more followers? Type 'A' or 'B': ")
# # if userGuess == 'A':
#
# # TODO When answered correctly, that selection becomes "A" and the B is a new choice.
# # TODO losing will give you the art and below saying "Sorry, that's wrong. Final score: X" with "x" being how far you got (2 or whatever)