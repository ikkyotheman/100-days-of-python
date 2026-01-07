import random
import art
player_Lives = 0
playing = True #This is for the loop to evaluate the guess

def compare_num():
    global player_Lives
    global playing
    if guess == the_number:
        print(f"You got it! The answer was {the_number}")
        playing = False
        return

    player_Lives -= 1

    if player_Lives == 0:
        print("You've run out of guesses, you lose.")
        playing = False
    # elif guess != integer .... This is where I can't figure out how to
    elif guess < the_number:
        print("Too low. Guess again.")
    elif guess > the_number:
        print("Too high. Guess again.")
    else:
        print("Guess again")

print(art.logo)
print("Welcome to The Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
the_number = random.randint(1, 100) # Number is chosen
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    player_Lives = 10
else:
    player_Lives = 5
while playing:
    print(f"You have {player_Lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    compare_num()

