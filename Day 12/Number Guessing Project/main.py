import random
import art
player_Lives = 0
playing = True #This is for the loop to evaluate the guess
# TODO create comparison function that evaluates the guess and tells the user "Too low. Guess again."
def compare_num():
    global player_Lives
    global playing
    if guess == the_number:
        print("You guessed the number!")
        playing = False
        return # What should I be returning here
    elif guess < the_number:
        print("Too low. Guess again.")
        player_Lives -= 1
        return
    elif guess > the_number:
        print("Too high. Guess again.")
        player_Lives -= 1
        return

print(art.logo)
print("Welcome to The Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
the_number = random.randint(1, 100) # Number is chosen
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
# TODO Easy mode will have 10 attempts and hard will be 5.
if difficulty == "easy":
    player_Lives = 10
else:
    player_Lives = 5
while playing:
    print(f"You have {player_Lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    compare_num()
# TODO create lose when player_Lives becomes 0



#TODO Tell them if they've won or lost "You've run out of guesses, you lose."
